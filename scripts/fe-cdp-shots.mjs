// Usage: node cdp-shots.mjs <base-url> <out-dir> <jobs.json>
// jobs: [{name, path, w, h, reduced, scroll: "css selector" | null, wait: ms}]
// Drives headless Chrome over the DevTools protocol (Node's built-in WebSocket, no packages).
import { spawn } from "node:child_process";
import { mkdtempSync, readFileSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
const [base, out, jobsFile] = process.argv.slice(2);
const jobs = JSON.parse(readFileSync(jobsFile, "utf8"));
const prof = mkdtempSync(join(tmpdir(), "cdp-"));
const port = 9300 + Math.floor(Math.random() * 500);
const chrome = spawn("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", ["--headless=new", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--hide-scrollbars", `--remote-debugging-port=${port}`, `--user-data-dir=${prof}`, "about:blank"], { stdio: "ignore" });
const sleep = (ms) => new Promise((r) => setTimeout(r, ms));
let ws;
for (let i = 0; i < 50 && !ws; i++) {
  try {
    const list = await (await fetch(`http://127.0.0.1:${port}/json`)).json();
    const page = list.find((t) => t.type === "page");
    ws = new WebSocket(page.webSocketDebuggerUrl);
    await new Promise((r, j) => ((ws.onopen = r), (ws.onerror = j)));
  } catch { ws = undefined; await sleep(200); }
}
let id = 0; const pending = new Map(); const events = [];
ws.onmessage = (m) => { const d = JSON.parse(m.data); if (d.id && pending.has(d.id)) { pending.get(d.id)(d); pending.delete(d.id); } else events.push(d); };
const send = (method, params = {}) => new Promise((r) => { const i = ++id; pending.set(i, r); ws.send(JSON.stringify({ id: i, method, params })); });
await send("Page.enable"); await send("Runtime.enable");
// every page records CSP violations and uncaught errors in window.__problems (read by a job's js)
await send("Page.addScriptToEvaluateOnNewDocument", { source: "window.__problems=[];document.addEventListener('securitypolicyviolation',e=>window.__problems.push('CSP '+e.violatedDirective+' '+e.blockedURI));addEventListener('error',e=>window.__problems.push('ERR '+e.message));addEventListener('unhandledrejection',e=>window.__problems.push('REJ '+(e.reason&&e.reason.message||e.reason)));" });
// a virtual passkey with PRF for every job that asks for one (no prompts, user verified)
if (jobs.some((j) => j.webauthn)) {
  await send("WebAuthn.enable", { enableUI: false });
  const a = await send("WebAuthn.addVirtualAuthenticator", { options: { protocol: "ctap2", ctap2Version: "ctap2_1", transport: "internal", hasResidentKey: true, hasUserVerification: true, isUserVerified: true, automaticPresenceSimulation: true, hasPrf: true } });
  globalThis.authenticatorId = a.result.authenticatorId;
  // passkeys made in an earlier run (process.env.CDP_CREDS_IN: a JSON file from CDP_CREDS_OUT)
  if (process.env.CDP_CREDS_IN) for (const credential of JSON.parse(readFileSync(process.env.CDP_CREDS_IN, "utf8"))) await send("WebAuthn.addCredential", { authenticatorId: globalThis.authenticatorId, credential });
}
for (const j of jobs) {
  await send("Emulation.setDeviceMetricsOverride", { width: j.w, height: j.h, deviceScaleFactor: 1, mobile: j.w < 600 });
  await send("Emulation.setEmulatedMedia", { features: [{ name: "prefers-reduced-motion", value: j.reduced ? "reduce" : "no-preference" }] });
  // a fresh document each time: the same URL with a hash would only scroll the old one
  await send("Page.navigate", { url: "about:blank" });
  await sleep(100);
  await send("Page.navigate", { url: base + j.path });
  await sleep(j.wait ?? 3500);
  if (j.scroll) {
    await send("Runtime.evaluate", { expression: `document.querySelector(${JSON.stringify(j.scroll)})?.scrollIntoView({block:"start"})` });
    await sleep(j.after ?? 1500);
  }
  if (j.js) {
    const r = await send("Runtime.evaluate", { expression: `(async () => { ${j.js} })()`, awaitPromise: true, returnByValue: true });
    const ex = r.result.exceptionDetails;
    writeFileSync(join(out, `${j.name}.js.txt`), ex ? `EXCEPTION ${ex.exception?.description ?? ex.text}` : JSON.stringify(r.result.result?.value ?? r.result, null, 1));
  }
  if (j.noShot) continue;
  const shot = await send("Page.captureScreenshot", { format: "jpeg", quality: 70 });
  writeFileSync(join(out, `${j.name}.jpg`), Buffer.from(shot.result.data, "base64"));
  if (j.text) {
    const t = await send("Runtime.evaluate", { expression: "document.body.innerText" });
    writeFileSync(join(out, `${j.name}.txt`), t.result.result.value);
  }
}
if (process.env.CDP_CREDS_OUT && globalThis.authenticatorId) {
  const c = await send("WebAuthn.getCredentials", { authenticatorId: globalThis.authenticatorId });
  writeFileSync(process.env.CDP_CREDS_OUT, JSON.stringify(c.result.credentials));
}
ws.close(); chrome.kill(); await sleep(300); rmSync(prof, { recursive: true, force: true });
