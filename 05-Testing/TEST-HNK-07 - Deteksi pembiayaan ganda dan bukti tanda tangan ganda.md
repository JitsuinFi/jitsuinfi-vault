---
tags: [test, "HNK-07"]
type: test
id: HNK-07
phase: F3
lead: Hans
owners: [Hans, Dave, Dex]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|AC]] · **Test** · [[ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dave #dave, Dex #dex

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-07.1 | Verifikasi bundel valid dan invalid | TODO | — | — |
| U-HNK-07.2 | Entri ulang dengan commitment yang sama tidak dianggap penipuan | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-07.1 | Supplier `TES-` mencoba ke financier `TES-b`; terdeteksi; bundel tersimpan | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Jalankan skenario demo "supplier mencoba menjual dua kali".

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
