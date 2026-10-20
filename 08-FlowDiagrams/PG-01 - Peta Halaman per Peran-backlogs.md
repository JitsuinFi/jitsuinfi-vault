---
tags: [flow, backlog]
status: DRAF
updated: 2026-10-20
---

# PG-01 - Peta Halaman per Peran-backlogs

**Diagram:** [[PG-01 - Peta Halaman per Peran]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]] · Polish: [[AC-HNK-21 - Polish halaman internal web app|HNK-21]]

Satu baris per halaman di peta. Kolom Task merujuk backlog DFD dan SEQ; halaman tanpa task baru ditandai "polish" (HNK-21).

## Halaman

| Kotak di peta | Halaman | Task fungsi | Polish | Kandidat |
|---|---|---|---|---|
| p1 | Landing `/` | — (ADA) | HNK-18.T4 | Dave |
| p2 | Verify `/app.html#/verify` | BL-D28-04, BL-D28-06, BL-D27-05 | HNK-21.T5 | Dave |
| p3 | Orang luar `/app.html#/outsider` | BL-D28-07 | HNK-21.T6 | Dave |
| p4 | Indeks bunga `/app.html#/index` | BL-D28-05 | — | Dave |
| a1 | Daftar (supplier, buyer, anggota) | BL-D21-01 – BL-D21-04, BL-S00-01 | HNK-21.T1 | Dave |
| a2 | Masuk | BL-D21-04, BL-D21-05, BL-S00-02 | HNK-21.T1 | Dave |
| a3 | Tambah / ganti peran | BL-S00-03 | HNK-21.T1 | Dave |
| a4 | Kunci sesi (overlay) | BL-D21-12 | HNK-21.T7 | Dave |
| a5 | Kartu kontak (QR) | BL-D21-11 | HNK-21.T7 | Dave |
| s1 | Daftar deal supplier (timeline per N) | BL-S01-01 | — | Dave |
| s2 | Invoice baru | BL-D22-02, BL-D22-03, BL-D22-05 | HNK-21.T2 | Dave |
| s3 | Tawarkan ke financier | BL-D23-01 | — | Dave |
| s4 | Tanda tangani entri papan | BL-D23-09 | — | Dave |
| s5 | Segel surat (supplier) | BL-D24-05 | HNK-21.T2 | Dave |
| s6 | Advance diterima | BL-D24-13 | — | Dave |
| b1 | Kotak masuk buyer | BL-S02-01 | — | Dave |
| b2 | Tanda tangani invoice | BL-D22-06 | HNK-21.T3 | Dave |
| b3 | Permintaan riwayat | BL-D26-02 | — | Dave |
| b4 | Segel surat (buyer) | BL-D24-06 | HNK-21.T3 | Dave |
| b5 | Bayar (QR ZIP-321) | BL-D25-01, BL-S02-02 | HNK-21.T3 | Dave |
| b6 | Sertifikat riwayat | BL-D26-03 | HNK-21.T3 | Dave |
| b7 | Riwayat saya | BL-D26-09, BL-D25-09 | — | Dave |
| f1 | Pipeline deal (per state), di origin node | BL-S03-01 | — | Dex |
| f2 | Penawaran masuk | BL-D23-02, BL-D23-03 | — | Dex |
| f3 | Cek riwayat buyer | BL-D26-06, BL-D26-07 | HNK-21.T4 | Dex |
| f4 | Detail deal | BL-S03-01, BL-D23-08, BL-D23-14 | HNK-21.T4 | Dex |
| f5 | Buat surat | BL-D24-02 | HNK-21.T4 | Dex |
| f6 | Penjadwal pelunasan | BL-D25-03, BL-D25-04 | — | Dex |
| f7 | Bundel | BL-D28-03 | HNK-21.T4 | Dex |
| f9 | Bukti ganda | BL-D27-04 | — | Hans |
| f8 | Pengaturan node: pairing, policy, allowlist | BL-D21-16, BL-D26-08, BL-D26-05 | — | Dave |
| m1 | Laporan solvabilitas | BL-D29-07, BL-S05-01 | — | Dave |
| m2 | Setoran saya (bukti inklusi) | BL-D29-05, BL-D29-07 | — | Dave |

## Task khusus peta halaman

| ID | Task | Selesai bila | Ref | Task backlog | Owner |
|---|---|---|---|---|---|
| BL-PG-01 | Router `app.html` per peran: halaman publik tanpa akun, halaman peran hanya setelah masuk; konsol financier tidak ada lagi di jitsuinfi.vercel.app | Tab simulasi Financier hilang dari web app; peran tanpa sesi diarahkan ke Masuk | P-11, HNK-21.T1 | HNK-22.T3, HNK-23.T6 | Dave |
| BL-PG-02 | i18n EN/中文, responsif 390 px, a11y, reduced motion untuk semua halaman baru | Semua halaman lolos cek HNK-21.T7 | HNK-21.T7 | HNK-21.T7 | Dex |
| BL-PG-03 | Regresi siklus `TES-` setelah halaman diganti, deploy ulang Vercel (setelah persetujuan) | Siklus lulus sebelum dan sesudah | HNK-21.T8 | HNK-21.T8 | Dex |
