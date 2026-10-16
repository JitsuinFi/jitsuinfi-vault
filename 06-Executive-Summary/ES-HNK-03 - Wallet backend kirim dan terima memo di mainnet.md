---
tags: [es, "HNK-03"]
type: es
id: HNK-03
phase: F2
lead: Hans
owners: [Hans, Dex]
status: PARSIAL
updated: 2026-10-17
---

# ES-HNK-03 - Wallet backend kirim dan terima memo di mainnet

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-03 - Wallet backend kirim dan terima memo di mainnet|AC]] · [[TEST-HNK-03 - Wallet backend kirim dan terima memo di mainnet|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## Apa diubah
- Crate `jitsuin-wallet`: `Devtool` membungkus `zcash-devtool` (sync, enhance, alamat default, `pay` dengan URI ZIP-321 multi-output dan memo biner/teks, `--disable-confirmation`, `--target-note-count 1`), parser `list-tx` (tinggi blok, fee, output, memo, flag transparan).
- 4 unit test lulus. `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Waktu konfirmasi rata-rata | sekitar 75 detik (dicatat) | 29 dtk (1 sampel testnet; spike: 22,8 dan 348,6 dtk) |
| Fee per transaksi | sekitar 0,0001 ZEC (dicatat) | 15.000 zat untuk 2 payment + change (testnet) |

## Status
**PARSIAL** (lihat Risiko tersisa).

## Risiko tersisa
- Script uji integrasi resmi + bukti pembersihan (HNK-03.T5, Dex) belum.
- Bergantung pada format output teks `zcash-devtool` (commit `b532d4c`); parser bisa rusak kalau devtool di-upgrade. Pin binary.
- Diuji di testnet saja (DEV-03); mainnet belum.

## Bukti
- Commit: `7fd8202` (lokal)
- ID tes: U-HNK-03.1–3, I-HNK-03.1–2; tx `8d8835f72129468ee06486458318355ebe98388594ae8f962ab814f99be887bc`
- Persetujuan user untuk push/deploy: _belum_ (org GitHub `JitsuinFi` ada, repo belum)
