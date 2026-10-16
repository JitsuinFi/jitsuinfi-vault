---
tags: [spike, "SPK-03"]
type: spike
id: SPK-03
area: Zcash
owner: Hans
status: PASS
updated: 2026-10-16
---

# SPK-03 - Kirim dan terima shielded dengan memo di mainnet

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Zcash · **Dipakai oleh:** HNK-03, HNK-05 – HNK-07

## Tujuan
Bukti end-to-end: backend mengirim transaksi shielded Ironwood berisi memo biner, penerima mendekode memo itu.

## Hipotesis
Crate stabil (atau zcash-devtool) bisa mengirim output Ironwood dengan memo arbitrer 512 byte.

## Langkah
1. Buat wallet `TES-wallet-a` dan `TES-wallet-b`; simpan seed secara aman di luar repo.
2. Danai `TES-wallet-a` dengan nominal kecil (lihat SPK-10).
3. Kirim 1 output ke `TES-wallet-b` dengan memo biner berprefix `0xFF` (sekitar 136 byte).
4. Tunggu konfirmasi; dekode memo di `TES-wallet-b`.
5. Catat txid, fee, pool, dan waktu konfirmasi.

## Kriteria lulus
- [x] Txid tercatat.
- [x] Memo terdekode identik byte per byte.
- [x] Fee sesuai ZIP-317.
- [x] Pool penerima = Ironwood.

## Fallback kalau gagal
- Panggil `zcash-devtool` atau Zally lewat subprocess dari backend.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Testnet (DEV-03). 1 TAZ dari `fauzec.com` masuk ke `TES-wallet-a` di pool Ironwood (txid `64795b2ba61d7998940277b246180a4bf03206d78b81086bcec7c0e28be54932`, blok 4.508.848). Entri papan dibuat dengan `hanko-core`, dikirim via URI ZIP-321 (`zcash-devtool wallet pay`) ke `TES-board`: txid `b6e9a61bd50c4b998d31adbf1d13a92a83e29846f6bc01e2731813e3bbea1fc4`, blok 4.508.905, pool Ironwood. Memo di chain (`0xFF` + 511 byte) di-decode `hanko-core`: N sama, signature supplier valid. Fee 0,00025 TAZ = 5 action × 5.000 zat (ZIP-317; 1 payment + 4 change). | Temuan: `pay` meminta konfirmasi interaktif → pakai `--disable-confirmation`; default `--target-note-count 4` memecah kembalian jadi 4 note (lebih banyak output dan fee) → pakai `--target-note-count 1`. |
| BLOCKED | 2026-10-16 | Belum bisa dijalankan. | Butuh Rust (SPK-01) dan ZEC untuk wallet `TES-` (SPK-10). |

## Catatan
Hanya akun `TES-`. Artefak on-chain tidak bisa dihapus (DEV-01 di [[Backlog]]).
