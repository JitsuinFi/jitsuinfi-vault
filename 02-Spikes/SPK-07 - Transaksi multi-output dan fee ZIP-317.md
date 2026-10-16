---
tags: [spike, "SPK-07"]
type: spike
id: SPK-07
area: Zcash
owner: Hans
status: PASS
updated: 2026-10-16
---

# SPK-07 - Transaksi multi-output dan fee ZIP-317

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Zcash · **Dipakai oleh:** HNK-05, HNK-06, HNK-15

## Tujuan
Pastikan backend bisa membuat satu transaksi dengan beberapa output shielded dan fee terhitung benar.

## Hipotesis
Builder transaksi mendukung banyak output dengan memo berbeda per output.

## Langkah
1. Kirim 1 transaksi dengan 3 output dan memo berbeda.
2. Bandingkan fee aktual dengan hitungan ZIP-317 (logical actions).
3. Catat padding action.

## Kriteria lulus
- [x] Transaksi terkonfirmasi.
- [x] Fee sesuai hitungan.
- [x] Setiap penerima mendekode memonya.

## Fallback kalau gagal
- Satu transaksi per penerima.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Satu transaksi `d759bbf2605a9cc9a220dbc0383645133c01bb722a38fc22a0f13b36355d2ac0` dengan 3 payment (2 entri ke papan, 1 memo teks ke `TES-wallet-b`) + 1 change, `--target-note-count 1`: fee 0,0002 TAZ = 4 action × 5.000 zat (sesuai ZIP-317). Papan men-decode 2 entri (signature valid); `wallet-b` membaca `Memo::Text("TES-SPK07 memo teks untuk wallet-b")`. | Multi-output dipakai untuk payout HNK-05/HNK-06. |
| BLOCKED | 2026-10-16 | Belum bisa dijalankan. | Butuh Rust (SPK-01) dan ZEC (SPK-10). |

## Catatan
_Kosong._
