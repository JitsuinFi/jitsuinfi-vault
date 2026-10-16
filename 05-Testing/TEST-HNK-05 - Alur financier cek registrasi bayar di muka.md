---
tags: [test, "HNK-05"]
type: test
id: HNK-05
phase: F3
lead: Hans
owners: [Hans, Dex, Dave]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-05 - Alur financier cek registrasi bayar di muka

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-05 - Alur financier cek registrasi bayar di muka|AC]] · **Test** · [[ES-HNK-05 - Alur financier cek registrasi bayar di muka|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-05.1 | State machine alur: cek → daftar → tunggu → bayar | TODO | — | — |
| U-HNK-05.2 | Format kuitansi | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-05.1 | Siklus `TES-INV-0002` di mainnet | TODO | — | — |
| I-HNK-05.2 | DB uji dibersihkan setelah tes (sisa 0) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Ikuti panduan financier di web atau CLI dari awal sampai pembayaran di muka.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
