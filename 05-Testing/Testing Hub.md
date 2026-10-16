---
tags: [hub, test]
---

# Testing Hub

**Bagian dari:** [[05 - Testing]] · Kembali: [[START-HERE]] · Terkait: [[Backlog]] · [[Dashboard]]

Tiga lapis test per item (langkah 3 [[Workflow Development]]): **Unit** (logika murni, tanpa DB), **Integrasi** (vs DB/chain sungguhan, artefak `TES-`, bukti pembersihan), **E2E** (panduan checkbox + tabel hasil untuk user). Eksekusi E2E independen oleh Dave di HNK-17. Lihat DEV-01 di [[Backlog]] untuk artefak on-chain.

## Bagian
- [[TEST-HNK-01 - Format invoice kanonik dan tanda tangan buyer]] — lead Hans #hans
- [[TEST-HNK-02 - Nullifier dan entri papan registry]] — lead Hans #hans
- [[TEST-HNK-03 - Wallet backend kirim dan terima memo di mainnet]] — lead Hans #hans
- [[TEST-HNK-04 - Pemindai papan registry]] — lead Hans #hans
- [[TEST-HNK-05 - Alur financier cek registrasi bayar di muka]] — lead Hans #hans
- [[TEST-HNK-06 - Pengalihan hak tagih dan pelunasan]] — lead Hans #hans
- [[TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda]] — lead Hans #hans
- [[TEST-HNK-08 - Indeks suku bunga publik]] — lead Dex #dex
- [[TEST-HNK-09 - Verifier CLI hanko verify]] — lead Dex #dex
- [[TEST-HNK-10 - Web app per peran]] — lead Dave #dave
- [[TEST-HNK-11 - Threat model dan halaman orang luar]] — lead Dave #dave
- [[TEST-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry]] — lead Dave #dave
- [[TEST-HNK-13 - Uji dengan pengguna sungguhan]] — lead Dave #dave
- [[TEST-HNK-14 - Submission video deskripsi dan demo URL]] — lead Dave #dave
- [[TEST-HNK-15 - Stretch JitsuinFi Vault]] — lead Hans #hans
- [[TEST-HNK-16 - CI dan quality gate]] — lead Dex #dex
- [[TEST-HNK-17 - QA E2E lintas item]] — lead Dave #dave
- [[TEST-HNK-18 - Materi pitch dan visual]] — lead Dave #dave

## Status (auto)
```dataview
TABLE WITHOUT ID file.link AS "Test", lead AS "Lead", unit AS "Unit", integrasi AS "Integrasi", e2e AS "E2E"
FROM "05-Testing"
WHERE type = "test"
SORT id ASC
```
