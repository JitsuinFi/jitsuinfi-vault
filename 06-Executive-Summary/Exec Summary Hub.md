---
tags: [hub, es]
---

# Exec Summary Hub

**Bagian dari:** [[06 - Executive Summary]] · Kembali: [[START-HERE]] · Terkait: [[Backlog]] · [[Dashboard]]

Satu ringkasan per item, ditulis oleh lead item (langkah 4 [[Workflow Development]]): Apa diubah · Hasil vs KPI (angka riil) · Status SELESAI/PARSIAL/BLOCKED · Risiko tersisa · Bukti commit/id tes · persetujuan user untuk push.

## Bagian
- [[ES-HNK-01 - Format invoice kanonik dan tanda tangan buyer]] — lead Hans #hans
- [[ES-HNK-02 - Nullifier dan entri papan registry]] — lead Hans #hans
- [[ES-HNK-03 - Wallet backend kirim dan terima memo di mainnet]] — lead Hans #hans
- [[ES-HNK-04 - Pemindai papan registry]] — lead Hans #hans
- [[ES-HNK-05 - Alur financier cek registrasi bayar di muka]] — lead Hans #hans
- [[ES-HNK-06 - Pengalihan hak tagih dan pelunasan]] — lead Hans #hans
- [[ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda]] — lead Hans #hans
- [[ES-HNK-08 - Indeks suku bunga publik]] — lead Dex #dex
- [[ES-HNK-09 - Verifier CLI hanko verify]] — lead Dex #dex
- [[ES-HNK-10 - Web app per peran]] — lead Dave #dave
- [[ES-HNK-11 - Threat model dan halaman orang luar]] — lead Dave #dave
- [[ES-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry]] — lead Dave #dave
- [[ES-HNK-13 - Uji dengan pengguna sungguhan]] — lead Dave #dave
- [[ES-HNK-14 - Submission video deskripsi dan demo URL]] — lead Dave #dave
- [[ES-HNK-15 - Stretch JitsuinFi Vault]] — lead Hans #hans
- [[ES-HNK-16 - CI dan quality gate]] — lead Dex #dex
- [[ES-HNK-17 - QA E2E lintas item]] — lead Dave #dave
- [[ES-HNK-18 - Materi pitch dan visual]] — lead Dave #dave
- [[ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay]] — lead Hans #hans
- [[ES-HNK-20 - Riwayat pembayaran buyer standar minimal]] — lead Hans #hans

## Status (auto)
```dataview
TABLE WITHOUT ID file.link AS "Exec Summary", phase AS "Fase", lead AS "Lead", status AS "Status"
FROM "06-Executive-Summary"
WHERE type = "es"
SORT id ASC
```
