---
tags: [spike, "SPK-02"]
type: spike
id: SPK-02
area: Infra
owner: Dex
status: PASS
updated: 2026-10-16
---

# SPK-02 - Endpoint lightwalletd mainnet

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dex #dex · **Area:** Infra · **Dipakai oleh:** HNK-03, HNK-04, HNK-09

## Tujuan
Temukan minimal dua endpoint lightwalletd/Zaino publik mainnet yang stabil dan mendukung Ironwood.

## Hipotesis
Ada endpoint komunitas yang bisa dipakai tanpa menjalankan node sendiri.

## Langkah
1. Kumpulkan kandidat endpoint dari dokumentasi Zcash, ZecHub, dan default `zcash-devtool`/Zodl.
2. Uji koneksi gRPC dan versi server.
3. Ukur latency dan waktu sync dari birthday height baru.
4. Bandingkan tinggi blok dengan explorer.
5. Catat endpoint utama dan cadangan.

## Kriteria lulus
- [x] Minimal 2 endpoint bisa dipakai.
- [x] Waktu sync dari birthday baru tercatat (angka).
- [x] Tinggi blok cocok dengan explorer.

## Fallback kalau gagal
- Endpoint komunitas lain.
- Menjalankan Zebra/Zakura + Zaino sendiri (berat; snapshot Zakura sekitar 11 GB) — hanya kalau terpaksa.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Run 3: wallet kosong `TES-wallet-a` (birthday = tip) via `zcash-devtool`: sync **mainnet 5,14 dtk** (`zec.rocks`, tinggi 3.519.969), **testnet 1,85 dtk** (`testnet.zec.rocks`, tinggi 4.508.802). | Semua kriteria terpenuhi. |
| BLOCKED | 2026-10-16 | `GetLightdInfo` via curl HTTP/2 (tanpa grpcurl): zec.rocks, na/eu/ap/sa.zec.rocks:443 semua HTTP 200 dalam 0,27–0,66 dtk; lightwalletd v0.5.3, chain `main`, branch `37a5165b`, tinggi 3.519.952 = Blockchair (3.519.952). `lwd1`–`lwd5.zcash-infra.com:9067`: DNS tidak resolve dari mesin ini. | Endpoint utama: `zec.rocks:443`; cadangan: `na.zec.rocks`, `eu.zec.rocks`, `ap.zec.rocks`, `sa.zec.rocks`. Sisa kriteria (waktu sync dari birthday) butuh wallet/Rust (SPK-01). |

## Catatan
IP kita terlihat oleh server endpoint. Masukkan ke [[Threat Model]].
