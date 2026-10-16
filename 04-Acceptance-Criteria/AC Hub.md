---
tags: [hub, ac]
---

# AC Hub

**Bagian dari:** [[04 - Acceptance Criteria]] · Kembali: [[START-HERE]] · Terkait: [[Backlog]] · [[Dashboard]]

Sumber kebenaran lulus/tidak setiap item. Status per kriteria `TODO` / `PASS` / `FAIL` / `BLOCKED` + tanggal + bukti (langkah 2 [[Workflow Development]]).

## Bagian
- [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer]] — lead Hans #hans
- [[AC-HNK-02 - Nullifier dan entri papan registry]] — lead Hans #hans
- [[AC-HNK-03 - Wallet backend kirim dan terima memo di mainnet]] — lead Hans #hans
- [[AC-HNK-04 - Pemindai papan registry]] — lead Hans #hans
- [[AC-HNK-05 - Alur financier cek registrasi bayar di muka]] — lead Hans #hans
- [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan]] — lead Hans #hans
- [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda]] — lead Hans #hans
- [[AC-HNK-08 - Indeks suku bunga publik]] — lead Dex #dex
- [[AC-HNK-09 - Verifier CLI hanko verify]] — lead Dex #dex
- [[AC-HNK-10 - Web app per peran]] — lead Dave #dave
- [[AC-HNK-11 - Threat model dan halaman orang luar]] — lead Dave #dave
- [[AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry]] — lead Dave #dave
- [[AC-HNK-13 - Uji dengan pengguna sungguhan]] — lead Dave #dave
- [[AC-HNK-14 - Submission video deskripsi dan demo URL]] — lead Dave #dave
- [[AC-HNK-15 - Stretch JitsuinFi Vault]] — lead Hans #hans
- [[AC-HNK-16 - CI dan quality gate]] — lead Dex #dex
- [[AC-HNK-17 - QA E2E lintas item]] — lead Dave #dave
- [[AC-HNK-18 - Materi pitch dan visual]] — lead Dave #dave

## Status (auto)
```dataview
TABLE WITHOUT ID file.link AS "AC", phase AS "Fase", lead AS "Lead", status AS "Status", updated AS "Update"
FROM "04-Acceptance-Criteria"
WHERE type = "ac"
SORT id ASC
```
