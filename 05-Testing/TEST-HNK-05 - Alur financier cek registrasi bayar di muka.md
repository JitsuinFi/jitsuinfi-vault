---
tags: [test, "HNK-05"]
type: test
id: HNK-05
phase: F3
lead: Hans
owners: [Hans, Dex, Dave]
unit: PASS
integrasi: PASS
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-05 - Alur financier cek registrasi bayar di muka

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-05 - Alur financier cek registrasi bayar di muka|AC]] · **Test** · [[ES-HNK-05 - Alur financier cek registrasi bayar di muka|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-05.1 | State machine alur: cek → daftar → tunggu → bayar | PASS | 2026-10-17 | 8 test `financier::tests` (`cargo test -p jitsuin-flow`): happy path dengan 2 konfirmasi, berhenti bila sudah dibiayai, berhenti bila double financing setelah posting, resume, entri supplier yang tidak cocok ditolak, deal invalid, hitung konfirmasi, advance yang sudah terkirim dipakai ulang |
| U-HNK-05.2 | Format kuitansi | PASS | 2026-10-17 | 6 test `receipt::tests` (`cargo test -p jitsuin-core`): roundtrip, layout tetap, signer salah/tamper, decoder ketat, nominal 0, test vector commitment; 2 test `supplier::tests` |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-05.1 | Siklus `TES-INV-0002` di mainnet | PASS (testnet, DEV-03) | 2026-10-17 | Scratchpad `flow-it`: entri `fe33137b7b76ce86e5c32d2e4bd6f271806b685837c6a99160857810ce7a98bc` (fee 10000 zat), advance `b52998041cf5e5ac9364272a5069200910ae613f4d9379f5a845561bcb53d30a` (fee 10000 zat), supplier verdict `Valid`, retry memakai advance yang sama (tidak bayar dua kali), financier lain dan N=`42…` berhenti. Total 273 dtk |
| I-HNK-05.2 | DB uji dibersihkan setelah tes (sisa 0) | PASS | 2026-10-17 | Tidak ada DB; program uji tidak menulis file. Artefak on-chain (2 tx di atas) dicatat, tidak bisa dihapus (DEV-01) |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = **0** (tidak ada DB atau file uji). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Ikuti panduan financier di web atau CLI dari awal sampai pembayaran di muka.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
