---
tags: [flow, backlog]
status: DITETAPKAN
progress: 1/2 SELESAI
updated: 2026-10-20
---

# SEQ-05 - Anggota Dana-backlogs

**Diagram:** [[SEQ-05 - Anggota Dana]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]] · Item: [[AC-HNK-15 - Stretch JitsuinFi Vault|HNK-15]]

Aturan sama dengan [[SEQ-00 - Autentikasi dan Onboarding-backlogs]]: merujuk task backlog DFD, menambah task khusus sequence `BL-S05-xx`.

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Pemetaan per bagian

| Bagian | Langkah di sequence | Task |
|---|---|---|
| Masuk | Peran anggota dana, hanya kotak surat | BL-D21-06 |
| 1. Setor | Daun Merkle sum tree, kuitansi lewat relay | BL-D29-01, BL-D29-02 |
| 2. Dana membiayai invoice | Advance dengan JTN1 | Sudah ada (SEQ-03 bagian 7) |
| 3. Laporan periode | Root dari tree, jalur Merkle per periode | BL-D29-03, BL-D29-04 |
| 4. Uji solvabilitas | UFVK lewat saluran privat | BL-D0-06 |
| 4. Uji solvabilitas | CLI solvabilitas, inklusi, halaman anggota | BL-D29-05, BL-D29-06, BL-D29-07 |

## Task khusus sequence

| ID | Bagian | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-S05-01 | Pendahuluan | Catat batas uji solvabilitas (sisi aset dinyatakan manajer) dan kebocoran nominal setoran + alamat supplier di halaman anggota dan submission | Halaman anggota menampilkan batas ini | SEQ-05 | HNK-29.T3 | Hans | SELESAI (2026-10-21, audit: kartu batas dan privasi di halaman anggota, frontend `f188b1c`) |
| BL-S05-02 | Semua | E2E anggota: setor, terima kuitansi, root, jalur Merkle, verdict solvent dan inklusi | Kasus lulus di TEST-HNK-15 | BL-D29-08 | HNK-17.T4 | Hans | TODO |
