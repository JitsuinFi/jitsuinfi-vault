---
tags: [flow, backlog]
status: DITETAPKAN
progress: 0/3 SELESAI
updated: 2026-10-20
---

# SEQ-01 - Supplier-backlogs

**Diagram:** [[SEQ-01 - Supplier]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Aturan sama dengan [[SEQ-00 - Autentikasi dan Onboarding-backlogs]]: merujuk task backlog DFD, menambah task khusus sequence `BL-S01-xx`.

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Pemetaan per bagian

| Bagian | Langkah di sequence | Task |
|---|---|---|
| Masuk | Masuk sebagai supplier | [[SEQ-00 - Autentikasi dan Onboarding-backlogs]] |
| 1. Siapkan invoice | Key per invoice dari master, `invoice_id` unik | BL-D22-02, BL-D22-03 |
| 1. Siapkan invoice | Terima `invoice_pk(k)` dari buyer | BL-D22-01 |
| 1. Siapkan invoice | Hash file syarat, invoice kanonik, N | Sudah ada; polish BL-D22-04 |
| 2. Tanda tangan buyer | Kirim invoice + PDF syarat, terima tanda tangan | BL-D22-05, BL-D22-08 |
| 2. Tanda tangan buyer | Cek tanda tangan buyer, simpan deal | BL-D22-09, BL-D22-10 |
| 3. Tawarkan | Pilih financier, advance, alamat baru per deal | BL-D23-01 |
| 3. Tawarkan | Terima pembuka komitmen, kelas, surat + PDF surat | BL-D23-06, BL-D24-03 |
| 3. Tawarkan | Terima sertifikat k atau tag (buyer memakai riwayat) | BL-D26-04, BL-D23-10 |
| 3. Tawarkan | Ditolak atau kedaluwarsa | BL-D23-03 |
| 4. Tanda tangani entri | Kartu entri 0x01 / 0x03 dengan kelas | BL-D23-09 |
| 4. Tanda tangani entri | Entri ditolak (`EntryMismatch`) | BL-D23-11 |
| 5. Segel surat | Isi surat, cek PDF surat, segel s0 | BL-D24-04, BL-D24-05 |
| 6. Terima advance | txid dari financier, status advance, cek nominal | BL-D24-11, BL-D24-12, BL-D24-13 |
| 7. Pantau pelunasan | Bundel dari financier, status di papan | BL-D25-08, BL-D25-09 |
| Jalur supplier nakal | Penawaran ditolak, bukti ke pihak berwenang | BL-D27-* (sisi financier) |
| Mode confidential | Roadmap | — |

## Task khusus sequence

| ID | Bagian | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-S01-01 | Semua | Halaman "Daftar deal" supplier: satu timeline per N (tanda tangan buyer, penawaran, entri, surat, advance, pelunasan) dari dokumen deal lokal | Supplier melihat langkah berikutnya untuk tiap deal | C-32 | HNK-24.T9 | Dave | DIKERJAKAN (2026-10-20, `17a01ea`: timeline per N dengan langkah berikutnya ADA, U-HNK-24.4, I-HNK-24.3; langkah pelunasan belum ada karena status `settled` datang lewat relay, HNK-23; HNK-24.T9 PARSIAL) |
| BL-S01-02 | 3 – 5 | Urutan pesan supplier mengikuti SEQ-03: pembuka komitmen dan surat dulu, permintaan entri setelah cek papan | Layar tidak meminta entri sebelum permintaan dari financier tiba | SEQ-03 | HNK-24.T9 | Dave | GAGAL AUDIT (2026-10-20: kartu entri muncul setelah penawaran, belum menunggu permintaan entri dari financier; butuh pesan relay HNK-23) |
| BL-S01-03 | Semua | E2E peran supplier: invoice sampai advance dan status pelunasan lewat relay | Satu siklus `TES-` lulus di HNK-17 | HNK-17 | HNK-17.T4 | Dave | TODO |
