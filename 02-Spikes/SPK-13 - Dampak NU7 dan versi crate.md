---
tags: [spike, "SPK-13"]
type: spike
id: SPK-13
area: Zcash
owner: Dex
status: PASS
updated: 2026-10-16
---

# SPK-13 - Dampak NU7 dan versi crate

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dex #dex · **Area:** Zcash · **Dipakai oleh:** Semua item

## Tujuan
Pastikan keputusan NU7 (go/no-go 20 Okt, target mainnet 5 Nov) tidak mengganggu build sebelum deadline.

## Hipotesis
Tidak ada upgrade mainnet sebelum 28 Okt.

## Langkah
1. Pantau pengumuman 20 Okt.
2. Cek apakah crate yang di-pin tetap valid di mainnet sampai 28 Okt.
3. Cek perubahan fee atau aturan transaksi sebelum deadline.

## Kriteria lulus
- [x] Konfirmasi tidak ada upgrade mainnet sebelum 28 Okt, atau rencana migrasi tercatat.

## Fallback kalau gagal
- Pin versi; tidak upgrade crate di minggu terakhir.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Per 16 Okt: NU7 aktif di testnet sejak blok 4.465.026 (4 Okt); mainnet ditargetkan 5 Nov, keputusan final 20 Okt; belum ada tinggi aktivasi mainnet. Jadi aturan mainnet saat ini (blok 75 dtk) berlaku sampai setelah deadline 28 Okt. | Cek ulang setelah keputusan 20 Okt. Kalau berubah, status kembali ke TODO. |

## Catatan
_Kosong._
