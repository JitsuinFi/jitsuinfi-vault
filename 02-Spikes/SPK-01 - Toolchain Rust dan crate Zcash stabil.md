---
tags: [spike, "SPK-01"]
type: spike
id: SPK-01
area: Tooling
owner: Dex
status: PASS
updated: 2026-10-16
---

# SPK-01 - Toolchain Rust dan crate Zcash stabil

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dex #dex · **Area:** Tooling · **Dipakai oleh:** HNK-01 – HNK-04

## Tujuan
Pastikan toolchain Rust dan crate librustzcash versi stabil bisa di-build di Mac ini dan mendukung Ironwood.

## Hipotesis
`zcash_client_backend` 0.24 + `zcash_client_sqlite` 0.22 (+ `pczt` 0.9.3) ter-build tanpa error di Rust stable; `zcash-devtool` bisa di-build sebagai fallback.

## Langkah
1. Catat versi `rustc` dan `cargo`.
2. Buat proyek kosong dengan dependency di-pin ke versi di atas, lalu `cargo build`.
3. Clone dan build `zcash-devtool`; jalankan `--help`.
4. Cek changelog crate: dukungan Ironwood (NU6.3).
5. Catat waktu build dan versi final di [[Decision Log]].

## Kriteria lulus
- [x] `cargo build` hijau dengan versi yang di-pin.
- [x] `zcash-devtool --help` jalan.
- [x] Dukungan Ironwood terkonfirmasi dari changelog/dokumentasi.
- [x] Versi tercatat di [[Decision Log]].

## Fallback kalau gagal
- Pakai library Zally.
- Turunkan ke versi crate yang masih kompatibel Ironwood.
- **Jangan** memakai crate pre-release NU7.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Rust terpasang lewat rustup resmi: rustc 1.99.1, cargo 1.99.1, rustup 1.29.1. Proyek spike dengan versi di-pin (`zcash_client_backend =0.24.0` fitur `lightwalletd-tonic`+`orchard`, `zcash_client_sqlite =0.22.0`, `pczt =0.9.3`, `zcash_protocol =0.10.6`, `blake2b_simd =1.0.5`) ter-build dalam 41,9 dtk. **`ed25519-dalek` 3.0.0 gagal resolve** (butuh `sha2` ^0.11, bentrok dengan `sha2 =0.11.0-pre.4` dari `bip32` via `zcash_transparent`/`pczt`) → dipakai **2.2.0**. `zcash_protocol` 0.10.6: `Nu6_3` mainnet = blok 3.428.143 (Ironwood), `Nu7 => None`. `zcash-devtool` main (clone 2026-10-16) memakai crate **pre-release**: `zcash_primitives =0.31.0-pre.2`, `zcash_protocol =0.11.0-pre.1` (fitur `local-consensus`), `pczt` dari git librustzcash. `cargo build --release` berhasil; `--help` jalan. Artinya fallback via devtool mengenal NU7 dan berpotensi bekerja di testnet maupun mainnet. | Versi final dicatat sebagai D-10 di [[Decision Log]]. |
| BLOCKED | 2026-10-16 | Rust tidak terpasang: `rustc`, `cargo`, `rustup` tidak ditemukan (`command -v`). macOS 26.5.1 arm64, disk kosong 355 GB. | Butuh persetujuan user: install Rust lewat rustup resmi, atau build di container Docker (butuh Colima dijalankan, lihat SPK-11). |

## Catatan
Library sebelum NU6.3 gagal mengirim ke Ironwood. Lihat `../research_notes/Kandidat ide ZECATHON tiga track/technical_feasibility.md`.
