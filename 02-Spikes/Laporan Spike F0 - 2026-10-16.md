---
tags: [spike, report]
---

# Laporan Spike F0 - 2026-10-16

**Bagian dari:** [[02 - Spikes]] · Kembali: [[Spikes Hub]] · [[Rencana Fase]] · [[Dashboard]]

Rekap run spike pertama. Detail dan bukti ada di file tiap spike. Dijalankan dari Mac Hans (macOS 26.5.1, arm64).

## Inventaris environment

| Tool | Status |
|---|---|
| Rust (`rustc`, `cargo`, `rustup`) | Run 1: tidak terpasang → **run 2: terpasang** (1.99.1 / 1.99.1 / 1.29.1, lewat rustup resmi) |
| Node / npm | v26.11.1 / 11.20.0 |
| Docker CLI / Colima | 29.9.0 / 0.10.3 — run 2: **berjalan** (server 29.5.2, VM x86_64 diemulasikan, 4 CPU, 6 GB) |
| git / GitHub CLI | 2.50.1 / 2.102.0, login `Shenhan01-sys` (scope `repo`, `workflow`) |
| Railway CLI | Tidak terpasang |
| grpcurl / protoc | Tidak terpasang (diganti curl HTTP/2 untuk uji gRPC) |
| Python | 3.9.6 |
| Video | QuickTime tersedia; OBS, ffmpeg, iMovie tidak ada |
| Obsidian | Terpasang |

## Hasil per spike

| ID | Spike | Owner | Kritis | Status | Ringkasan |
|---|---|---|---|---|---|
| SPK-01 | [[SPK-01 - Toolchain Rust dan crate Zcash stabil\|Toolchain Rust dan crate Zcash stabil]] | Dex #dex | Ya | **PASS** | Rust terpasang lewat rustup resmi: rustc 1.99.1, cargo 1.99.1, rustup 1.29.1 |
| SPK-02 | [[SPK-02 - Endpoint lightwalletd mainnet\|Endpoint lightwalletd mainnet]] | Dex #dex | Ya | **BLOCKED** | `GetLightdInfo` via curl HTTP/2 (tanpa grpcurl): zec.rocks, na/eu/ap/sa.zec.rocks:443 semua HTTP 200 dalam 0,27–0,66 dtk; lightwalletd v0.5. |
| SPK-03 | [[SPK-03 - Kirim dan terima shielded dengan memo di mainnet\|Kirim dan terima shielded dengan memo di mainnet]] | Hans #hans | Ya | **BLOCKED** | Belum bisa dijalankan. |
| SPK-04 | [[SPK-04 - Pembayaran Zodl lewat URI ZIP-321 dengan memo\|Pembayaran Zodl lewat URI ZIP-321 dengan memo]] | Hans #hans | Ya | **TODO** | Tidak bisa dijalankan dari Mac ini. |
| SPK-05 | [[SPK-05 - Pemindaian watch-only dengan viewing key\|Pemindaian watch-only dengan viewing key]] | Hans #hans | Ya | **BLOCKED** | Belum bisa dijalankan. |
| SPK-06 | [[SPK-06 - Kripto inti Ed25519 hash dan layout memo\|Kripto inti Ed25519 hash dan layout memo]] | Hans #hans | Ya | **PASS** | Lintas implementasi: Rust `ed25519-dalek` 2.2.0 + `blake2b_simd` 1.0.5 menghasilkan pk, sig, dan N **identik** dengan Node/Python (test vect |
| SPK-07 | [[SPK-07 - Transaksi multi-output dan fee ZIP-317\|Transaksi multi-output dan fee ZIP-317]] | Hans #hans | — | **BLOCKED** | Belum bisa dijalankan. |
| SPK-08 | [[SPK-08 - Latensi konfirmasi dan urutan entri\|Latensi konfirmasi dan urutan entri]] | Hans #hans | — | **BLOCKED** | Sebagian: Blockchair `blocks_24h` = 1.163 → rata-rata sekitar 74,3 dtk per blok (blok mainnet 75 dtk terkonfirmasi). |
| SPK-09 | [[SPK-09 - Hosting Railway dan hardening web\|Hosting Railway dan hardening web]] | Dex #dex | — | **TODO** | Railway CLI tidak terpasang |
| SPK-10 | [[SPK-10 - Dana mainnet dan keamanan seed\|Dana mainnet dan keamanan seed]] | Hans #hans | — | **TODO** | Estimasi anggaran: sekitar 40 transaksi uji dan demo × 0,0001 ZEC fee = 0,004 ZEC, ditambah saldo putar antar wallet `TES-` sekitar 0,01–0,0 |
| SPK-11 | [[SPK-11 - Distribusi verifier CLI di mesin bersih\|Distribusi verifier CLI di mesin bersih]] | Dex #dex | — | **TODO** | Colima dijalankan (`colima start`): Docker server 29.5.2, VM **x86_64** (diemulasikan di Mac arm64), 4 CPU, 6 GB RAM; `docker run hello-worl |
| SPK-12 | [[SPK-12 - Kepastian aturan dan form ZECATHON\|Kepastian aturan dan form ZECATHON]] | Dave #dave | — | **TODO** | Draf email sudah disiapkan di bagian Catatan. |
| SPK-13 | [[SPK-13 - Dampak NU7 dan versi crate\|Dampak NU7 dan versi crate]] | Dex #dex | — | **PASS** | Per 16 Okt: NU7 aktif di testnet sejak blok 4.465.026 (4 Okt); mainnet ditargetkan 5 Nov, keputusan final 20 Okt; belum ada tinggi aktivasi  |
| SPK-14 | [[SPK-14 - Repo baru lisensi dan originalitas\|Repo baru lisensi dan originalitas]] | Dex #dex | — | **TODO** | GitHub CLI siap (`repo`, `workflow`). |
| SPK-15 | [[SPK-15 - Tooling produksi video\|Tooling produksi video]] | Dave #dave | — | **BLOCKED** | QuickTime Player tersedia |
| SPK-16 | [[SPK-16 - Block explorer untuk demo\|Block explorer untuk demo]] | Dave #dave | — | **BLOCKED** | Akses dari curl: `zecblock.com` HTTP 200; API Blockchair `/zcash/stats` OK (tinggi cocok), web Blockchair 401 dan `mainnet.zcashexplorer.app |
| SPK-17 | [[SPK-17 - Toolchain frontend dan aset offline\|Toolchain frontend dan aset offline]] | Dave #dave | — | **PASS** | Node 26.11.1, npm 11.20.0 |
| SPK-18 | [[SPK-18 - Akses tim dan kesamaan environment\|Akses tim dan kesamaan environment]] | Dex #dex | — | **TODO** | Belum dijalankan. |
| SPK-19 | [[SPK-19 - Testnet NU7 untuk development\|Testnet NU7 untuk development]] | Hans #hans | — | **TODO** | Endpoint `testnet.zec.rocks:443` hidup: chain `test`, tinggi 4.508.756, branch `77190ad9`, node Zebra v7.0.0-rc.0, lightwalletd v0.5.4 |

Total: 7 BLOCKED, 4 PASS, 8 TODO (dari 19 spike).

## Gerbang F0

**Belum lulus.** Spike kritis: SPK-01 `PASS`, SPK-02 `BLOCKED`, SPK-03 `BLOCKED`, SPK-04 `TODO`, SPK-05 `BLOCKED`, SPK-06 `PASS`. Rust dan Docker sudah beres (run 2). Penghalang tersisa: **ZEC untuk wallet `TES-`** (SPK-03, SPK-05, SPK-07, SPK-08, SPK-10), **Zodl di HP** (SPK-04), dan keputusan jaringan (SPK-19).

## Keputusan yang dibutuhkan dari user

| # | Keputusan | Membuka | Owner | Status |
|---|---|---|---|---|
| 1 | Install Rust lewat rustup resmi | SPK-01 | Hans | **Selesai** (run 2) |
| 2 | Jalankan Colima | SPK-11 | Hans | **Selesai** (run 2) |
| 3 | Jaringan development: (A) mainnet saja, (B) hybrid testnet + mainnet demo, (C) testnet saja | SPK-19, D-13 | Hans | Menunggu |
| 4 | Siapkan sekitar 0,02–0,03 ZEC dan Zodl di HP (kalau A atau B) | SPK-03, 04, 07, 10 | Hans | Menunggu |
| 5 | Akses Railway (integrasi GitHub atau Railway CLI) + persetujuan deploy | SPK-09 | Hans → Dex | Menunggu |
| 6 | Kirim email ke organizer (draf di SPK-12) | SPK-12 | Hans | Menunggu |
| 7 | Alat video: QuickTime saja atau install OBS/editor | SPK-15 | Dave | Menunggu |
| 8 | Buat repo publik baru dan undang Dex serta Dave | SPK-14, SPK-18 | Hans | Menunggu |
| 9 | Setujui stack frontend Vite + React + TypeScript | SPK-17 → HNK-10 | Hans | Menunggu |
| 10 | Konfirmasi DEV-01 (pembersihan artefak on-chain) | Uji integrasi | Hans | Menunggu |
| 11 | Setujui DEV-02 (F1 boleh mulai sekarang karena SPK-01 dan SPK-06 sudah PASS) | HNK-01, HNK-02, HNK-16 | Hans | Menunggu |

## Temuan penting
- **Run 2:** crate stabil ter-build dan mengenal Ironwood; `ed25519-dalek` harus 2.x (3.0.0 bentrok `sha2`); test vector cocok lintas implementasi (Node/Python/Rust).
- **Testnet ada, tapi sudah NU7:** crate stabil tidak bisa bertransaksi di testnet; `zcash-devtool` main memakai crate pre-release yang mengenal NU7.
- **Endpoint lightwalletd:** `zec.rocks` (5 region) sehat dan tersinkron; `zcash-infra.com` tidak resolve dari mesin ini.
- **Blok mainnet sekitar 74 detik** (1.163 blok/24 jam), konsisten dengan 75 detik.
- **Desain kripto valid**; test vector siap dipakai di HNK-01.
- **NU7 tidak memengaruhi mainnet sebelum deadline** (cek ulang 20 Okt).
- **Frontend toolchain siap** dan bisa bebas resource pihak ketiga.

## Run 3 — keputusan user dan hasil tanpa ZEC

- **Jaringan:** opsi B (D-13). Development di testnet sampai menjelang submit; satu set crate pre-release untuk testnet dan mainnet.
- **Zodl opsional** (D-15); semua peran memakai `zcash-devtool`.
- **Repo lokal** `zkSNARK/hanko/` sampai user membuat repo GitHub (D-14).
- **DEV-02 disetujui:** F1 (HNK-01, HNK-02, HNK-16) mulai sekarang.
- **SPK-02 PASS:** sync wallet kosong mainnet 5,14 dtk, testnet 1,85 dtk.
- **SPK-05 sebagian:** watch-only dari UFVK berhasil dan tidak bisa mengirim; `init-fvk` tidak menerima UIVK (usulan D-11).
- **SPK-19 PASS:** crate pre-release ter-build dan mengenal NU7 testnet; faucet `fauzec.com` (1 TAZ/24 jam).

### Langkah user berikutnya
1. Klaim 1 TAZ di `fauzec.com` ke alamat `TES-wallet-a` (alamat ada di chat dan bisa dilihat dengan `zcash-devtool wallet -w ~/.hanko-tes/testnet/wallet-a list-addresses`).
2. Setelah TAZ masuk: jalankan SPK-03, SPK-05 (baca memo), SPK-07, SPK-08, SPK-16 (explorer testnet), SPK-19 kriteria 4.

## Run 4 — dengan 1 TAZ (testnet)

| Spike | Status | Inti |
|---|---|---|
| SPK-03 | **PASS** | Entri dikirim via ZIP-321, memo di chain di-decode `hanko-core` dengan signature valid (tx `b6e9a61bd50c4b99…`) |
| SPK-05 | **PASS** | Watch-only membaca 3 entri; memo butuh `wallet enhance` |
| SPK-07 | **PASS** | 3 output + change, fee sesuai ZIP-317 (tx `d759bbf2605a9cc9…`) |
| SPK-08 | **PASS** | Latensi 22,8 dan 348,6 dtk; indeks tx tersedia dari `GetBlock` |
| SPK-16 | **FAIL** → fallback | Explorer testnet di chain lama; tampilkan data dari lightwalletd |
| SPK-19 | **PASS** | Transaksi testnet dengan memo berhasil |

### Gerbang F0
**Lulus untuk jaringan development (testnet).** Semua spike kritis (SPK-01, SPK-02, SPK-03, SPK-05, SPK-06) `PASS`. SPK-04 tidak lagi kritis (D-15). F2 boleh dimulai.

### Temuan teknis untuk build
- `zcash-devtool wallet pay` butuh `--disable-confirmation` untuk otomatisasi; pakai `--target-note-count 1` supaya kembalian tidak dipecah.
- Compact block tidak membawa memo: scanner papan (HNK-04) harus mengambil transaksi penuh.
- Waktu konfirmasi testnet sangat bervariasi (sampai sekitar 6 menit): UI dan video harus memperhitungkannya.
- Explorer testnet tidak bisa diandalkan; halaman orang luar memakai data lightwalletd.
- Sisa saldo `TES-wallet-a` setelah 2 transaksi uji: 0,99905 TAZ (1 − 0,00035 − 0,0006).
