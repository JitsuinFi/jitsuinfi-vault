---
tags: [spike, "SPK-16"]
type: spike
id: SPK-16
area: Resource
owner: Hans
status: FAIL
updated: 2026-10-16
---

# SPK-16 - Block explorer untuk demo

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Resource · **Dipakai oleh:** HNK-11, HNK-14

## Tujuan
Temukan explorer mainnet yang bisa menampilkan transaksi shielded Ironwood (terlihat ada, isinya tidak) untuk demo dan halaman orang luar.

## Hipotesis
Minimal satu explorer publik mendukung transaksi Ironwood.

## Langkah
1. Uji akses beberapa explorer.
2. Setelah SPK-03, buka txid uji di tiap explorer dari browser.
3. Catat explorer yang menampilkan transaksi Ironwood dengan benar.

## Kriteria lulus
- [x] Minimal 1 explorer bisa diakses.
- [ ] Txid Ironwood uji tampil dengan benar di explorer itu.

## Fallback kalau gagal
- Tampilkan data langsung dari lightwalletd (`GetTransaction`) di halaman orang luar.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| FAIL | 2026-10-16 | Testnet: `testnet.zcashexplorer.app` (dibuka lewat browser) berada di tinggi 4.481.008 sementara testnet NU7 di sekitar 4.508.900 → mengikuti chain yang tertinggal/fork lama; tx Ironwood kita **tidak ditemukan**. Mainnet: `zecblock.com` bisa diakses (belum diuji dengan tx Ironwood). | **Fallback dipakai:** halaman "orang luar" (HNK-11) menampilkan data langsung dari lightwalletd (`GetBlock`/`GetTransaction`), yang sudah terbukti jalan. Explorer mainnet diuji ulang saat demo mainnet. |
| BLOCKED | 2026-10-16 | Akses dari curl: `zecblock.com` HTTP 200; API Blockchair `/zcash/stats` OK (tinggi cocok), web Blockchair 401 dan `mainnet.zcashexplorer.app` 403 (kemungkinan proteksi bot, perlu cek di browser); `3xpl.com` 429 (rate limit); `zcashblockexplorer.com` dan `explorer.zec.rocks` tidak bisa diakses. | Kriteria kedua (txid Ironwood tampil benar) butuh transaksi uji dari SPK-03. |

## Catatan
_TODO_
