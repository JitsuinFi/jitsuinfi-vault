---
tags: [flow, backlog]
status: DITETAPKAN
progress: 0/3 SELESAI
updated: 2026-10-20
---

# SEQ-02 - Buyer-backlogs

**Diagram:** [[SEQ-02 - Buyer]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Aturan sama dengan [[SEQ-00 - Autentikasi dan Onboarding-backlogs]]: merujuk task backlog DFD, menambah task khusus sequence `BL-S02-xx`.

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Pemetaan per bagian

| Bagian | Langkah di sequence | Task |
|---|---|---|
| Masuk | Master dari passkey | Sudah ada; disesuaikan BL-D21-04 |
| Masuk | `k` otomatis dari rantai yang tertambat, kepala rantai bertanda tangan | BL-D26-03 |
| 1. Bagikan key | `invoice_pk(k)` ke supplier lewat relay | BL-D22-01 |
| 2. Tanda tangani invoice | Terima invoice + PDF, cek hash dan `buyer_pk` di layar | BL-D22-05, BL-D22-06 |
| 2. Tanda tangani invoice | Simpan invoice, tanda tangan, kirim balik | BL-D22-07, BL-D22-08 |
| 3. Ungkap riwayat | Permintaan bertanda tangan, persetujuan, sertifikat k | BL-D26-01, BL-D26-02 |
| 3. Ungkap riwayat | Kirim rantai ke financier, tag ke supplier | BL-D26-04, BL-D23-10 |
| 4. Segel surat | Isi surat, cek PDF surat, segel s1 | BL-D24-04, BL-D24-06 |
| 4. Segel surat | Terima s2 dari financier | BL-D24-11 |
| 5. Bayar | Pengingat jatuh tempo | BL-D25-02 |
| 5. Bayar | QR hanya untuk surat `Sealed` | BL-D25-01 |
| 5. Bayar | Bayar dari Zodl atau `zcash-devtool` | BL-D25-10 |
| 6. Cek status dan riwayat | Status pelunasan, riwayat saya | BL-D25-09, BL-D26-09 |
| Jalur sengketa | Klaim dengan nominal kurang, `Disputed` | BL-D25-04 (sisi financier) |

## Task khusus sequence

| ID | Bagian | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-S02-01 | Semua | Kotak masuk buyer: invoice untuk ditandatangani, permintaan riwayat, surat untuk disegel, tagihan jatuh tempo | Setiap tindakan buyer dimulai dari kotak masuk | C-31, PG-01 | HNK-22.T6 | Hans | TODO |
| BL-S02-02 | 4 – 5 | Setelah s1, layar buyer menunggu s2 dan baru menawarkan QR saat surat `Sealed` | Tombol QR tidak aktif sebelum s2 tiba | BL-D25-01 | HNK-25.T4 | Hans | TODO |
| BL-S02-03 | Semua | E2E peran buyer: tanda tangan, riwayat, segel, bayar, status | Satu siklus `TES-` lulus di HNK-17 | HNK-17 | HNK-17.T4 | Hans | TODO |
