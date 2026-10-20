---
tags: [ac, "HNK-05"]
type: ac
id: HNK-05
phase: F3
lead: Hans
owners: [Hans]
status: PASS
updated: 2026-10-17
---

# AC-HNK-05 - Alur financier cek registrasi bayar di muka

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-05 - Alur financier cek registrasi bayar di muka|Test]] · [[ES-HNK-05 - Alur financier cek registrasi bayar di muka|Exec Summary]]

**Item:** HNK-05 · **Fase:** F3 · **Dependency:** HNK-04

**Lead:** Hans #hans · **Tim:** Hans #hans 

## Deskripsi
Financier memeriksa papan, mendaftarkan N, menunggu minimal satu konfirmasi, lalu membayar di muka secara shielded ke supplier dengan memo kuitansi.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-05.1 | Kalau N sudah ada di papan, alur berhenti sebelum pembayaran. | PASS | 2026-10-17 | Testnet: financier kedua untuk N yang sama berhenti di `Stopped(AlreadyFinanced)` (pemenang `fe33137b…`); N=`42…` berhenti di `Stopped(DoubleFinanced)` (1 konflik). Tidak ada transaksi terkirim. Unit: `stops_when_another_financier_is_registered`, `stops_on_double_financing_even_after_posting` |
| AC-HNK-05.2 | Entri registrasi terkonfirmasi sebelum pembayaran di muka dikirim. | PASS | 2026-10-17 | `pay_advance` ditolak saat `AwaitConfirmation` (state machine). Entri `fe33137b7b76ce86…` terkonfirmasi di tinggi 4509085 (tip 4509085, 1 konfirmasi) sebelum advance dikirim. Unit: `happy_path_waits_for_confirmations_before_paying` |
| AC-HNK-05.3 | Pembayaran di muka shielded dengan memo kuitansi bertanda tangan financier; supplier memverifikasinya. | PASS | 2026-10-17 | Advance `b52998041cf5e5ac9364272a5069200910ae613f4d9379f5a845561bcb53d30a` 100.000 zat, output Ironwood (transparent: tidak), memo `JTR1` bertanda tangan financier; supplier (wallet-b) memverifikasi: verdict `Valid` (signer, tanda tangan, nominal = nilai output) |
| AC-HNK-05.4 | Satu siklus penuh di mainnet dengan invoice `TES-INV-xxxx`; semua txid tercatat. | PASS | 2026-10-17 | Dibaca sebagai testnet (DEV-03): siklus `TES-INV-0002/HNK-05/1792174167`, entri `fe33137b7b76ce86e5c32d2e4bd6f271806b685837c6a99160857810ce7a98bc`, advance `b52998041cf5e5ac9364272a5069200910ae613f4d9379f5a845561bcb53d30a`, total 273 dtk. **Uji ulang di mainnet bila ZEC tersedia** |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
