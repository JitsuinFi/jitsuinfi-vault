---
tags: [spike, "SPK-04"]
type: spike
id: SPK-04
area: Wallet
owner: Hans
status: TODO
updated: 2026-10-16
---

# SPK-04 - Pembayaran Zodl lewat URI ZIP-321 dengan memo

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Wallet · **Dipakai oleh:** HNK-05, HNK-06, HNK-10

## Tujuan
Pastikan Zodl memindai QR ZIP-321 berparameter memo dan mengirimkannya tanpa mengubah memo.

## Hipotesis
Zodl mendukung parameter `memo` (base64url) pada URI ZIP-321 untuk alamat shielded.

## Langkah
1. Buat URI dengan `address`, `amount`, dan `memo`.
2. Tampilkan sebagai QR; bayar dari Zodl (catat versi app dan OS).
3. Cek memo di penerima: biner vs teks.
4. Uji URI tanpa nominal (user mengisi sendiri).

## Kriteria lulus
- [ ] Memo diterima utuh.
- [ ] Nominal tepat.
- [ ] Versi Zodl tercatat.

## Fallback kalau gagal
- Memo teks (payload biner di-encode base64) kalau memo biner tidak didukung.
- Pembayaran demo dikirim dari wallet backend; Zodl hanya untuk penerimaan.

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| TODO | 2026-10-16 | Keputusan user 16 Okt: **Zodl opsional.** Development memakai wallet CLI `zcash-devtool` untuk semua peran. Wallet web (WebZjs) tidak bisa dipakai (rusak, tanpa Ironwood). | Dijalankan hanya kalau demo akhir ingin memakai Zodl; di testnet NU7 Zodl kemungkinan belum didukung. |
| TODO | 2026-10-16 | Tidak bisa dijalankan dari Mac ini. | Butuh HP dengan Zodl dan ZEC; dijalankan Hans. |

## Catatan
Hasil spike ini menentukan UX pembayaran buyer di HNK-06.
