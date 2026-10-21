---
tags: [project, submission]
---

# Submission - Deskripsi

**Bagian dari:** [[00 - Project]] · Kembali: [[START-HERE]] · Item: HNK-14.T2 di [[Backlog]] · Terkait: [[AC-HNK-14 - Submission video deskripsi dan demo URL|AC-HNK-14]] · [[ZECATHON - Aturan dan Deadline]] · [[Threat Model]]

> Draf v2 2026-10-21 (ditulis agent; Hans me-review, D-35). Batas **2.000 karakter**; panjang saat ini **1.838** karakter (`wc -m`). Bahasa Inggris (juri internasional). Mengikuti D-40: hook N-06, N-11, N-09, W-07, W-08, apa yang dibangun (node + konsol D-43, direktori D-47, mandat privat N-15, dana D-49), N-13, W-06, N-12 (W-05), W-04, W-12, label jaringan W-17. Tidak memakai "$2.3B financed twice" (W-15). Perbarui "Real vs mock" kalau mainnet jadi dijalankan (HNK-30.T12).

```text
First Brands' lenders never saw an invoice, never asked the buyer, never controlled the cash. JitsuinFi does all three, and no outsider sees the deal. Zcash stops double-spending; JitsuinFi stops double-financing.

How: the buyer signs the invoice with a passkey. Its fingerprint N goes on a public board: one shielded Zcash address whose viewing key we published on purpose. No server, no admin, no login. Before paying, any lender asks "was N already sold?" and learns nothing else; a second sale yields proof that the supplier signed twice. Advance, assignment seals and repayment all move in the shielded pool.

Why Zcash, not a hash on any chain: on a public chain the registrant, timing and the advance and repayment flows can be linked; here only the parties to a deal can link them. Unlike MonetaGo or ABS's registry, the board has no operator and the proof of double signing is cryptographic.

Built: a web app for suppliers, buyers and fund members; a financier node with a passkey console (no terminal); a directory where suppliers pick financiers; private mandates matched on each node against sealed offers, so order flow meets no order book; pooled funds where members verify their units against a signed root and withdraw at the period's price.

Honest limits: a fake invoice the buyer itself co-signs is out of scope; credit diligence still applies. Detection only protects lenders who check the board, so it is one command, open to anyone. Buyers already sign when required (India's TReDS), and gain a provable payment history. Settlement is in ZEC; a stablecoin leg via CrossPay or NEAR Intents is the production path, not built. Legal recognition is roadmap; proofs are built for auditors and courts.

Real vs mock: everything runs on Zcash testnet, Ironwood pool, with txids in the README; test data starts with TES-.
```

## Cek sebelum submit
- [ ] Panjang ≤ 2.000 karakter (hitung ulang setelah edit).
- [ ] Semua klaim punya bukti di README (txid testnet; mainnet kalau ada).
- [ ] Tautan spesifikasi dan threat model ada di README.

## Draf v1 (2026-10-18, diganti v2)
Usang: menyebut backend financier hanya library dan CLI; belum ada hook N-06, node, direktori, mandat privat, dan dana.

```text
JitsuinFi is private invoice financing on Zcash. Zcash stops double-spending; JitsuinFi stops double-financing.

What it does: each invoice gets a fingerprint N, a hash of the buyer-signed invoice. Financiers register N on a public board (a shielded account with a published viewing key) as a memo signed by the supplier's per-invoice key. A second financier offered the same invoice finds N before paying and gets proof that the supplier signed twice. Deal documents are sealed in order (supplier, buyer, financier); the advance carries the financier's last seal in the same shielded transaction. A repayment counts only once mined, with the buyer's claim and the financier's countersignature. Buyers carry a payment history anchored on the board, so hidden defaults are detected.

Why it does not leak: all money moves in the shielded pool, with no transparent inputs or outputs. The board holds only hashes and signatures that can be checked only with the invoice. Financiers hide behind salted commitments, buyers use a fresh key per invoice from a passkey, and settled entries cannot be linked to registrations. Verification runs in the browser (WASM) under a same-origin CSP. Known leaks (timing, entry counts, a repeated N) are listed in our threat model.

Real vs mock: everything ran on Zcash testnet, in the Ironwood pool: registrations, advances, repayments by ZIP-321 QR, settled entries, double-financing proofs, buyer histories and a fund solvency check. Txids are in the README; test data starts with TES-. The financier backend is a library and CLI, not a hosted service.
```
