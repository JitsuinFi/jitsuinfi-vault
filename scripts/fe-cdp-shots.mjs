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
    writeFileSync(join(out, `${j.name}.js.txt`), JSON.stringify(r.result.result?.value ?? r.result, null, 1));
  }
  if (j.noShot) continue;
  const shot = await send("Page.captureScreenshot", { format: "jpeg", quality: 70 });
  writeFileSync(join(out, `${j.name}.jpg`), Buffer.from(shot.result.data, "base64"));
  if (j.text) {
    const t = await send("Runtime.evaluate", { expression: "document.body.innerText" });
    writeFileSync(join(out, `${j.name}.txt`), t.result.result.value);
  }
}
ws.close(); chrome.kill(); await sleep(300); rmSync(prof, { recursive: true, force: true });
