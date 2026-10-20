---
tags: [flow, backlog]
status: DITETAPKAN
progress: 0/1 SELESAI
updated: 2026-10-20
---

# SEQ-04 - Verifier dan Orang Luar-backlogs

**Diagram:** [[SEQ-04 - Verifier dan Orang Luar]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Aturan sama dengan [[SEQ-00 - Autentikasi dan Onboarding-backlogs]]: merujuk task backlog DFD, menambah task khusus sequence `BL-S04-xx`.

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Pemetaan per bagian

| Bagian | Langkah di sequence | Task |
|---|---|---|
| A. CLI `jitsuin verify` | UFVK + birthday papan dipublikasikan | BL-D28-01, BL-D0-05 |
| A. CLI `jitsuin verify` | Review/merge CLI, Docker, README | BL-D28-02 |
| B. CLI offline | Snapshot `--board` | Sudah ada (BL-D28-02) |
| C. Indeks | Kelas tidak lagi 0/0 | BL-D23-05 |
| C. Indeks | `rateIndex` wasm + halaman indeks | BL-D28-05 |
| D. Layar Verify | Snapshot dari relay | BL-D28-06 |
| D. Layar Verify | Verdict bundel yang benar | BL-D28-04 |
| D. Layar Verify | Bukti diperiksa terhadap papan | BL-D27-05 |
| E. Orang luar | Teks halaman sesuai TM #13 – #14 | BL-D28-07 |

## Task khusus sequence

| ID | Bagian | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-S04-01 | A – D | Juri menjalankan alur A sampai D dari mesin bersih dengan README saja, hasil web dan CLI sama untuk bundel dan bukti contoh | Kasus lulus di TEST-HNK-09 | BL-D28-08 | HNK-17.T4 | Dave | TODO |
