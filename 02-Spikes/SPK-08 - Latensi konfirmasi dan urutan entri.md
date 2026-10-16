---
tags: [spike, "SPK-08"]
type: spike
id: SPK-08
area: Zcash
owner: Hans
status: PASS
updated: 2026-10-16
---

# SPK-08 - Latensi konfirmasi dan urutan entri

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Zcash · **Dipakai oleh:** HNK-04, HNK-05, HNK-07

## Tujuan
Ukur waktu konfirmasi mainnet dan pastikan scanner bisa mengurutkan entri secara deterministik untuk aturan "entri pertama menang".

## Hipotesis
Compact block memberi tinggi blok dan indeks transaksi yang cukup untuk urutan total.

## Langkah
1. Kirim 2 entri berurutan; catat waktu broadcast sampai 1 konfirmasi.
2. Cek data urutan (tinggi blok, indeks transaksi) dari lightwalletd.
3. Coba 2 entri di blok yang sama bila memungkinkan.

## Kriteria lulus
- [x] Median waktu konfirmasi tercatat.
- [x] Urutan deterministik bisa dihitung dari data yang tersedia.

## Fallback kalau gagal
- Tie-break tambahan: txid leksikografis. Catat di [[Format Data]].

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Latensi broadcast → masuk blok (dari stempel waktu blok): sampel 1 = 22,8 dtk, sampel 2 = 348,6 dtk (testnet NU7, variasi besar). `GetBlock` (compact block) memuat indeks tiap transaksi: tx1 indeks 4 dari 5 di blok 4.508.905; tx2 indeks 1 dari 6 di blok 4.508.918 → urutan total (tinggi blok, indeks tx, indeks output) bisa dihitung. | Waktu konfirmasi testnet bisa sampai sekitar 6 menit: demo harus direkam dengan buffer dan dipercepat; UI wajib menampilkan status "menunggu konfirmasi". |
| BLOCKED | 2026-10-16 | Sebagian: Blockchair `blocks_24h` = 1.163 → rata-rata sekitar 74,3 dtk per blok (blok mainnet 75 dtk terkonfirmasi). | Median waktu konfirmasi dan data urutan (indeks transaksi) butuh transaksi uji dan klien gRPC (SPK-01, SPK-03). |

## Catatan
_Kosong._
