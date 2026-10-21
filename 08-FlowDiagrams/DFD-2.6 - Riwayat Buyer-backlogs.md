---
tags: [flow, backlog]
status: DITETAPKAN
progress: 2/10 SELESAI
updated: 2026-10-20
---

# DFD-2.6 - Riwayat Buyer-backlogs

**Diagram:** [[DFD-2.6 - Riwayat Buyer]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 6.1 – 6.8. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D26-01 | 6.1, F6.01 – F6.03 | Pesan "permintaan riwayat" dari node, ditandatangani `financier_pk` | Buyer menerima permintaan; permintaan dengan tanda tangan salah ditolak | P-04 | HNK-23.T8 | Hans | TODO |
| BL-D26-02 | 6.2, F6.04 – F6.06 | Layar buyer: permintaan riwayat dengan nama kontak financier, tombol setujui atau tolak | Buyer melihat siapa yang meminta dan untuk invoice apa sebelum menyetujui | C-01, P-04 | HNK-25.T2 | Hans | TODO |
| BL-D26-03 | 6.2, F6.07 – F6.10, D13 | Nomor `k` otomatis dari rantai yang tertambat; sertifikat yang tidak pernah tertambat dibuang; kepala rantai bertanda tangan disimpan terenkripsi di relay | Buyer tidak mengetik `k`; relay yang menghapus sertifikat terakhir terdeteksi | P-09 | HNK-25.T2 | Hans | DIKERJAKAN (2026-10-20, `88af897`, `0e59952`: `k` tidak diketik, sertifikat tak tertambat dibuang, sertifikat terakhir yang hilang terdeteksi lewat tag penerus di papan; kepala rantai bertanda tangan di relay menunggu HNK-23) |
| BL-D26-04 | 6.3, F6.11 – F6.14 | Kirim rantai 0..k + `identity_pk` ke financier yang meminta, dan `history_tag` (atau sertifikat k) ke supplier | Financier dan supplier menerima isi yang dibutuhkan saja | P-04, K-10 | HNK-23.T7 | Hans | DIKERJAKAN |
| BL-D26-05 | 6.4, F6.16, D5 | Registri `identity_pk` buyer hasil KYC di node financier, dipakai saat memeriksa rantai | Rantai dengan `identity_pk` yang tidak terdaftar ditandai | C-02 | HNK-26.T7 | Hans | SELESAI (2026-10-21, lokal, belum merge: `buyers::tests` (tambah, ubah label, hapus, tersimpan; key salah ditolak; rantai tanpa atau dengan `identity_pk` tak terdaftar ditandai); konsol dicek dengan node tiruan) |
| BL-D26-06 | 6.5 – 6.6, F6.18 – F6.26 | API `POST /node/history/check` memanggil `check_buyer` dengan `MinimumStandard`, menyimpan laporan dan `history_tag` di deal | Hasil lulus menyimpan `history_tag`; retry setelah crash memakai tag yang tersimpan tanpa cek ulang | C-11 | HNK-26.T8 | Hans | AUDIT (2026-10-22: `check_buyer` di node dengan standar dari mandat privat, tag disimpan di deal, node `9b83bd7`; diaudit di E2E testnet) |
| BL-D26-07 | 6.5, F6.22 | Alasan penolakan riwayat terbaca (`NotAnchored`, `Equivocation`, `FinancierNotAllowed`, `UndisclosedSuccessor`, di bawah standar) | Tiap alasan punya teks yang menjelaskan artinya | C-13 | HNK-21.T9 | Hans | SELESAI (2026-10-22, audit: penolakan yang disebut baris ini punya kalimat di `explain.ts`, diuji `tests/explain.test.ts`) |
| BL-D26-08 | 6.7, F6.27 – F6.28 | Pengaturan policy di konsol: allowlist financier, standar minimal, tenggang | Operator mengubah policy tanpa mengedit kode; nilai bertahan setelah restart | C-12 | HNK-26.T9 | Hans | TODO |
| BL-D26-09 | 6.8, F6.29 – F6.32 | Kartu "Riwayat saya" di layar buyer (`verifyHistory` dengan allowlist dari sertifikat sendiri + snapshot) | Buyer melihat status tiap invoice tanpa unggah file | C-14, P-06 | HNK-25.T6 | Hans | AUDIT (2026-10-22: kode di layar buyer/supplier; diaudit dengan deal nyata di E2E testnet) |
| BL-D26-10 | Uji | Integrasi testnet: dua invoice berurutan dengan riwayat, invoice kedua lolos standar | Kasus tercatat di TEST-HNK-20 atau HNK-17 | HNK-17 | HNK-17.T4 | Hans | TODO |

## Sudah ada (tanpa task baru)

- 6.2 sertifikat (`buyerHistoryCert`), 6.4 verifikasi rantai (`verify_certs`), 6.5 cocokkan dengan papan (`verify_history`), 6.6 standar minimal (`MinimumStandard::evaluate`, `check_buyer`), struktur `HistoryPolicy`.

## Keputusan yang dibutuhkan

- Griefing `UndisclosedSuccessor` (Spec #1 di [[Pra-review Spesifikasi dan Threat Model]]): belum ada jalur bantahan.
