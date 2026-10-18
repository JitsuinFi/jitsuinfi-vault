---
tags: [project, submission]
---

# Submission - Deskripsi

**Bagian dari:** [[00 - Project]] · Kembali: [[START-HERE]] · Item: HNK-14.T2 di [[Backlog]] · Terkait: [[AC-HNK-14 - Submission video deskripsi dan demo URL|AC-HNK-14]] · [[ZECATHON - Aturan dan Deadline]] · [[Threat Model]]

> Draf 2026-10-18 (D-25, ditulis agent; Dave dan Hans me-review). Batas **2.000 karakter**; panjang saat ini **1801** karakter. Bahasa Inggris (juri internasional). Perbarui bagian "Real vs mock" kalau mainnet jadi dijalankan.

```text
JitsuinFi is private invoice financing on Zcash. Zcash stops double-spending; JitsuinFi stops double-financing.

What it does: each invoice gets a fingerprint N, a hash of the buyer-signed invoice. Financiers register N on a public board (a shielded account with a published viewing key) as a memo signed by the supplier's per-invoice key. A second financier offered the same invoice finds N before paying and gets proof that the supplier signed twice. Deal documents are sealed in order (supplier, buyer, financier); the advance carries the financier's last seal in the same shielded transaction. A repayment counts only once mined, with the buyer's claim and the financier's countersignature. Buyers carry a payment history anchored on the board, so hidden defaults are detected.

Why it does not leak: all money moves in the shielded pool, with no transparent inputs or outputs. The board holds only hashes and signatures that can be checked only with the invoice. Financiers hide behind salted commitments, buyers use a fresh key per invoice from a passkey, and settled entries cannot be linked to registrations. Verification runs in the browser (WASM) under a same-origin CSP. Known leaks (timing, entry counts, a repeated N) are listed in our threat model.

Real vs mock: everything ran on Zcash testnet (NU7, Ironwood): registrations, advances, repayments by ZIP-321 QR, settled entries, double-financing proofs, buyer histories and a fund solvency check. Txids are in the README; test data starts with TES-. The financier backend is a library and CLI, not a hosted service.

Disclosure: a team member previously built AVAL (Casper, 2026), a public-chain invoice registry using smart contracts. JitsuinFi shares the problem, not the code: all code was written for Zcash during the build window.
```

## Cek sebelum submit
- [ ] Panjang ≤ 2.000 karakter (hitung ulang setelah edit).
- [ ] Semua klaim punya bukti di README (txid testnet; mainnet kalau ada).
- [ ] Pengungkapan AVAL disetujui user.
- [ ] Tautan spesifikasi dan threat model ada di README.
