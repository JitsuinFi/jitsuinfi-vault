---
tags: [flow, backlog]
status: DITETAPKAN
progress: 3/8 SELESAI
updated: 2026-10-20
---

# DFD-0 - Diagram Konteks-backlogs

**Diagram:** [[DFD-0 - Diagram Konteks]] · Turunan: [[DFD-1 - Proses Utama-backlogs]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · Backlog: [[Backlog]]

Level 0 memperlihatkan sistem sebagai satu proses dengan tujuh entitas luar. Task per proses ada di [[DFD-1 - Proses Utama-backlogs]]. Halaman ini memuat task di batas sistem: integrasi dengan entitas luar dan komponen sistem yang belum ada.

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task di batas sistem

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D0-01 | Komponen relay dokumen | Repo `jitsuinfi-backend`: skeleton API, deploy Railway, header CSP, rewrite Vercel `/api/*` (setelah persetujuan deploy) | Relay hidup di URL same-origin web app | HNK-10.T4, HNK-10.T5, P-11 | HNK-23.T3, HNK-23.T5, HNK-23.T6 | Hans | SELESAI (2026-10-20: repo `jitsuinfi-backend`, Railway dari `main`, rewrite Vercel `/api/*`; produksi `jitsuinfi.vercel.app/api/health` 200 lewat origin web app; PR #14 `b05d8e6`) |
| BL-D0-02 | Komponen node financier | Node testnet yang bisa dijalankan juri atau penguji: setup, API, konsol di origin node dengan HTTPS (atau tunnel SSH) | Satu panduan menjalankan node dari nol sampai konsol terbuka | P-05, HNK-05.T3 | HNK-26.T1, HNK-26.T20 | Hans | GAGAL AUDIT (2026-10-21, setup node sudah ada (HNK-26.T1) tetapi kriteria butuh konsol di origin node dan panduan dari nol sampai konsol terbuka: menunggu HNK-26.T2, HNK-26.T3 dan README node) |
| BL-D0-03 | Entitas Authenticator, K1 – K2 | Daftar authenticator yang diuji (platform macOS/iOS, Android, security key) dan dukungan PRF-nya | Tabel dukungan di TEST-HNK-10 | C-03 | HNK-22.T7 | Hans | TODO |
| BL-D0-04 | Entitas Jaringan Zcash, K13 – K14 | Konfigurasi jaringan satu tempat (testnet `testnet.zec.rocks:443`, mainnet `zec.rocks:443`) di web app, node, dan CLI | Ganti jaringan cukup di satu konfigurasi | FD-00 §5 | HNK-26.T19 | Hans | TODO |
| BL-D0-05 | Entitas Verifier, K9 – K10 | UFVK papan dipublikasikan (D-11) dan README juri | Juri bisa memverifikasi tanpa bertanya ke tim | C-26, HNK-09.T3 | HNK-28.T6 | Hans | SELESAI (2026-10-20, I-HNK-28.3 dan langkah E2E 1: wallet baru hanya dengan data README, PASS 4/4; PR #10 `c73009b`) |
| BL-D0-06 | Entitas Anggota dana, K11 – K12 | UFVK operasional diserahkan lewat saluran privat, tidak pernah ke server | Panduan anggota menyebut saluran dan larangan unggah UFVK | P-10 | HNK-29.T3 | Hans | SELESAI (2026-10-21, audit: kartu privasi halaman anggota menyebut saluran privat dan larangan memberi UFVK ke situs, frontend `f188b1c`) |
| BL-D0-07 | Semua entitas | Uji end to end lintas semua entitas di testnet dengan relay dan node (siklus `TES-` lengkap: daftar sampai settled) | Satu siklus lulus dan tercatat di HNK-17 | HNK-17 | HNK-17.T4 | Hans | TODO |
| BL-D0-08 | Batas sistem | Baris Threat Model untuk relay, proxy, dan CSP setelah relay ada ditinjau ulang setelah relay dibangun | Bagian "Tambahan untuk arsitektur target" di [[Threat Model]] sesuai implementasi | P-04, P-11 | HNK-23.T1 | Hans | GAGAL AUDIT (2026-10-20: baris relay di Threat Model ditinjau terhadap skema HNK-23.T1, tetapi relay belum dibangun; tinjau ulang setelah HNK-23.T4) |
