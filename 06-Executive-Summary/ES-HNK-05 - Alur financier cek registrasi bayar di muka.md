---
tags: [es, "HNK-05"]
type: es
id: HNK-05
phase: F3
lead: Hans
owners: [Hans, Dex, Dave]
status: PARSIAL
updated: 2026-10-17
---

# ES-HNK-05 - Alur financier cek registrasi bayar di muka

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-05 - Alur financier cek registrasi bayar di muka|AC]] · [[TEST-HNK-05 - Alur financier cek registrasi bayar di muka|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## Apa diubah
- Crate baru `jitsuin-flow`: state machine financier murni (`Check` → `AwaitSupplierSignature` → `Register` → `AwaitConfirmation` → `Pay` → `Done`, atau `Stopped`) dan driver `Financier` (scan papan, post entri, tunggu konfirmasi, bayar advance).
- Pengaman: advance hanya bisa dibayar bila entri kita yang pertama valid dan cukup konfirmasi. Retry setelah crash memakai advance yang sudah terkirim (tidak bayar dua kali).
- `jitsuin-core`: memo kuitansi `JTR1` (146 byte) dengan decoder ketat, dan `financier_commitment`.
- Sisi supplier: `sign_register_entry` dan `received_advances` (cek signer, tanda tangan, nominal).
- `lwd::latest_height` (`GetLatestBlock`) untuk menghitung konfirmasi.
- 27 unit test workspace lulus; `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Waktu siklus registrasi + bayar | dicatat (sekitar 2 konfirmasi) | 273 dtk total; entri terkonfirmasi 228 dtk setelah mulai; advance terlihat di supplier 19 dtk setelah dikirim (min. 1 konfirmasi) |
| Pembayaran sebelum entri terkonfirmasi | 0 | 0 (percobaan sengaja ditolak) |

## Status
**PARSIAL**. Bagian Hans (T1, T2) selesai; T3 (Dex), T4 (Hans, menunggu scaffold FE Dave), T5 dan T6 (Dave) belum.

## Risiko tersisa
- Endpoint API (T3), integrasi layar (T4), layout (T5), dan panduan E2E (T6) belum.
- N masih placeholder di uji integrasi; derivasi final menunggu DEV-04.
- Uji mainnet menunggu ZEC (DEV-03).
- State `Flow` belum dipersist; backend (T3) harus menyimpannya. Pengaman bayar-dua-kali bergantung pada riwayat wallet financier.

## Bukti
- Commit: `6b5c343` (lokal)
- ID tes: U-HNK-05.1–2, I-HNK-05.1–2; entri `fe33137b7b76ce86e5c32d2e4bd6f271806b685837c6a99160857810ce7a98bc`, advance `b52998041cf5e5ac9364272a5069200910ae613f4d9379f5a845561bcb53d30a`
- Persetujuan user untuk push/deploy: _belum_
