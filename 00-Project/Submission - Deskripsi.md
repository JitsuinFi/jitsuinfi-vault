---
tags: [project, submission]
---

# Submission - Deskripsi

**Bagian dari:** [[00 - Project]] · Kembali: [[START-HERE]] · Item: HNK-14.T2 di [[Backlog]] · Terkait: [[AC-HNK-14 - Submission video deskripsi dan demo URL|AC-HNK-14]] · [[ZECATHON - Aturan dan Deadline]] · [[Threat Model]] · [[Submission - Runbook]] · [[Submission - Checklist Publikasi Repo]]

> **Draf v3 2026-10-27** (HNK-14.T2, ditulis agent; Hans me-review, D-35). Batas **2.000 karakter**; panjang v3 **1.978 karakter** (Python `len`, sama dengan hitungan JavaScript `length`), 1.988 byte UTF-8, 1.992 bila form mengubah baris baru menjadi CRLF: semua di bawah 2.000. Bahasa Inggris. Disalin ke form persis seperti blok di bawah (tanpa pagar ```).
>
> **Yang berubah dari v2:** mencerminkan yang live per 27 Okt (app per peran yang bisa dipasang di HP, inbox, konsol passkey, direktori bertanda tangan, mandat privat, dana anggota); bukti dari production testnet (deal `TES-INV-JUDGE3-9161` diklik lewat app live sampai settled, dan `TES-INV-DBL-24689` berhenti `DoubleFinanced`); tautan landing, app, verify, konsol demo, kode. Kalimat ZSA ("shielded stablecoins would remove the swap") dibuang demi ruang; jalur produksi W-04 tetap (USD + swap Zodl).
>
> **Syarat sebelum dipakai:** kalimat "Full txids in the README" baru benar setelah README `jitsuinfi-zcash` diberi tabel txid production (teks siap tempel di [[Submission - Checklist Publikasi Repo]] bagian README). Kalau README tidak diperbarui, ganti kalimat itu dengan txid penuh settled saja, lalu hitung ulang.

## Draf v3 (2026-10-27, dipakai)

```text
First Brands' lenders never saw an invoice, never asked the buyer, never controlled the cash. JitsuinFi does all three, and no outsider sees the deal.

How: the buyer seals the invoice with a passkey. Its fingerprint N goes on a public board: one shielded Zcash address whose viewing key we published on purpose. No server, no admin, no login. Before paying, any lender asks "was N already sold?" and learns nothing else; a second sale yields proof the supplier signed twice. Advance, seals and repayment stay in the shielded pool.

Why Zcash, not a hash on any chain: on a public chain the registrant, timing and money flows link up; here only a deal's parties can link them. Unlike MonetaGo or ABS's registry, the board has no operator and double signing is proven cryptographically.

Live: an app for suppliers, buyers and fund members (installs on a phone); a financier node with a passkey console; a signed financier directory; private mandates matched on each node against sealed offers, so order flow meets no order book; member funds with checkable units.

Evidence, Zcash testnet, Ironwood pool: TES-INV-JUDGE3-9161, clicked through the live app, registered 35ed7469…bd55, settled 208d9d57…35ba; TES-INV-DBL-24689 stopped as DoubleFinanced, entries a2f46ffd…3659, a42152b0…9188. Full txids in the README; test data is TES-.

Limits: a fake invoice the buyer itself co-signs is out of scope; credit diligence still applies. Detection protects only lenders who check the board, so the check is one open command. Buyers already sign when required (India's TReDS) and gain a provable payment history. Settlement is in ZEC today; USD-priced invoices paid via Zodl's USDC-to-shielded-ZEC swap come next. Legal recognition is roadmap; proofs are built for auditors and courts.

jitsuinfi.vercel.app (app /app, verify /verify) · console demo: jitsuinfi-console-demo.vercel.app/console · code: github.com/JitsuinFi

Zcash stops double-spending. JitsuinFi stops double-financing.
```

### Peta v3 ke D-40 dan register judging
| Elemen | Kalimat di v3 |
|---|---|
| Hook N-06 (bukan "$2.3B financed twice", W-15) | Paragraf 1 |
| N-11 viewing key adalah API | "one shielded Zcash address whose viewing key we published on purpose. No server, no admin, no login." |
| N-09 cek kredit tanpa konsorsium | "any lender asks "was N already sold?" and learns nothing else" |
| N-08 bukti tanda tangan ganda | "a second sale yields proof the supplier signed twice" |
| W-07 kenapa bukan hash di chain mana saja | Paragraf "Why Zcash" kalimat 1 |
| W-08 beda dengan MonetaGo / ABS | Paragraf "Why Zcash" kalimat 2 |
| Apa yang dibangun (node + konsol D-43, direktori D-47, mandat privat N-15, dana D-49), PWA dan inbox HNK-34 | Paragraf "Live" |
| Bukti nyata, label jaringan W-17 | Paragraf "Evidence, Zcash testnet, Ironwood pool" |
| N-13 batas | "a fake invoice the buyer itself co-signs is out of scope; credit diligence still applies" |
| W-06 cold start | "Detection protects only lenders who check the board, so the check is one open command." |
| N-12 + W-05 insentif buyer | "Buyers already sign when required (India's TReDS) and gain a provable payment history." |
| W-04 mata uang (D-50) | "Settlement is in ZEC today; USD-priced invoices paid via Zodl's USDC-to-shielded-ZEC swap come next." |
| W-12 hukum = roadmap | "Legal recognition is roadmap; proofs are built for auditors and courts." |
| Real vs mock | "test data is TES-", semua di testnet |
| Penutup N-03 | Baris terakhir |

### Bukti di balik angka v3 (dicek 2026-10-27)
| Klaim | Txid penuh | Blok | Sumber |
|---|---|---|---|
| `TES-INV-JUDGE3-9161` register entry | `35ed74696145f5838188dffe49ef9a51cd5ae054f3de97044ec8855ed859bd55` | 4545839 | `/node/board` production + HNK-34.T13 |
| `TES-INV-JUDGE3-9161` advance | `1de9e9473d3e6b01f9037820908bca77a20891f203d95fe372886abb8343f48f` | — | log E2E HNK-34.T13 |
| `TES-INV-JUDGE3-9161` pelunasan (QR) | `668d0e0f3cca380dff846b936390a9526992de717260012fac6d0efd316d331a` | — | log E2E HNK-34.T13 |
| `TES-INV-JUDGE3-9161` settled entry | `208d9d573bc39e3e80d9771eb22695b5d666622576bffb790369c06f619735ba` | 4545868 | `/node/board` production + HNK-34.T13 |
| `TES-INV-DBL-24689` entry pertama (production) | `a2f46ffdeebef1e0fa4de74b8b2bb26083a48cb9528a72ab7ac26914a7103659` | 4540314 | `/node/board`, BL-S03-03 |
| `TES-INV-DBL-24689` entry kedua (financier lain) → `DoubleFinanced` | `a42152b0ed19b5f54437ddfe61bc44b811dd3d405e78b863f3b060f237709188` | 4540315 | `/node/board`, BL-S03-03 |
| `TES-INV-ALR-71337` entry lebih dulu → `AlreadyFinanced` (tidak dipakai di v3) | `25a78d45bc2ab59a5f48fff8b594cdc0bdc9cf1e218a36bd7ae8cbcb51bf75b5` | 4540347 | `/node/board`, BL-S03-03 |

Papan production saat dicek: 55 entri, tip 4547249 (`https://jitsuinfi-console.vercel.app/node/board`, endpoint publik). Semua tautan di v3 menjawab HTTP 200 pada 2026-10-27, kecuali `github.com/JitsuinFi/jitsuinfi-zcash` (404 saat logout karena repo masih PRIVATE).

## Draf v2 (2026-10-21, diganti v3; disimpan untuk rujukan)

> Draf v2 2026-10-21 (ditulis agent; Hans me-review, D-35). Batas **2.000 karakter**; panjang saat ini **1.951** karakter (`wc -m`, 2026-10-22 setelah D-50). Bahasa Inggris (juri internasional). Mengikuti D-40: hook N-06, N-11, N-09, W-07, W-08, apa yang dibangun (node + konsol D-43, direktori D-47, mandat privat N-15, dana D-49), N-13, W-06, N-12 (W-05), W-04 (D-50: USD + swap shielded Zodl + ZSA), W-12, label jaringan W-17. Tidak memakai "$2.3B financed twice" (W-15). Perbarui "Real vs mock" kalau mainnet jadi dijalankan (HNK-30.T12).

```text
First Brands' lenders never saw an invoice, never asked the buyer, never controlled the cash. JitsuinFi does all three, and no outsider sees the deal. Zcash stops double-spending; JitsuinFi stops double-financing.

How: the buyer signs the invoice with a passkey. Its fingerprint N goes on a public board: one shielded Zcash address whose viewing key we published on purpose. No server, no admin, no login. Before paying, any lender asks "was N already sold?" and learns nothing else; a second sale yields proof that the supplier signed twice. Advance, assignment seals and repayment all move in the shielded pool.

Why Zcash, not a hash on any chain: on a public chain the registrant, timing and the advance and repayment flows can be linked; here only the parties to a deal can link them. Unlike MonetaGo or ABS's registry, the board has no operator and the proof of double signing is cryptographic.

Built: a web app for suppliers, buyers and fund members; a financier node with a passkey console (no terminal); a directory where suppliers pick financiers; private mandates matched on each node against sealed offers, so order flow meets no order book; pooled funds where members verify their units against a signed root and withdraw at the period's price.

Honest limits: a fake invoice the buyer itself co-signs is out of scope; credit diligence still applies. Detection only protects lenders who check the board, so it is one command, open to anyone. Buyers already sign when required (India's TReDS), and gain a provable payment history. Settlement is in ZEC for now; next, invoices priced in USD settle in shielded ZEC at a rate both parties sign, buyers already swap USDC into shielded ZEC in Zodl, and Zcash shielded stablecoins would remove the swap. Legal recognition is roadmap; proofs are built for auditors and courts.

Real vs mock: everything runs on Zcash testnet, Ironwood pool, with txids in the README; test data starts with TES-.
```

## Cek sebelum submit
- [x] Panjang ≤ 2.000 karakter (v3: 1.978, dihitung 2026-10-27; hitung ulang setelah edit).
- [ ] Semua klaim punya bukti di README (txid testnet; mainnet kalau ada). v3: tabel txid production belum ada di README zcash, lihat [[Submission - Checklist Publikasi Repo]].
- [ ] Tautan spesifikasi dan threat model ada di README (spesifikasi ada; threat model publik = bagian Security dan Privacy considerations di spesifikasi, README node masih menunjuk vault private).

## Draf v1 (2026-10-18, diganti v2)
Usang: menyebut backend financier hanya library dan CLI; belum ada hook N-06, node, direktori, mandat privat, dan dana.

```text
JitsuinFi is private invoice financing on Zcash. Zcash stops double-spending; JitsuinFi stops double-financing.

What it does: each invoice gets a fingerprint N, a hash of the buyer-signed invoice. Financiers register N on a public board (a shielded account with a published viewing key) as a memo signed by the supplier's per-invoice key. A second financier offered the same invoice finds N before paying and gets proof that the supplier signed twice. Deal documents are sealed in order (supplier, buyer, financier); the advance carries the financier's last seal in the same shielded transaction. A repayment counts only once mined, with the buyer's claim and the financier's countersignature. Buyers carry a payment history anchored on the board, so hidden defaults are detected.

Why it does not leak: all money moves in the shielded pool, with no transparent inputs or outputs. The board holds only hashes and signatures that can be checked only with the invoice. Financiers hide behind salted commitments, buyers use a fresh key per invoice from a passkey, and settled entries cannot be linked to registrations. Verification runs in the browser (WASM) under a same-origin CSP. Known leaks (timing, entry counts, a repeated N) are listed in our threat model.

Real vs mock: everything ran on Zcash testnet, in the Ironwood pool: registrations, advances, repayments by ZIP-321 QR, settled entries, double-financing proofs, buyer histories and a fund solvency check. Txids are in the README; test data starts with TES-. The financier backend is a library and CLI, not a hosted service.
```
