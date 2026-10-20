---
tags: [test, "HNK-30"]
type: test
id: HNK-30
phase: F6
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-21
---

# TEST-HNK-30 - Demo juri dan narasi dari judging

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-30 - Demo juri dan narasi dari judging|AC]] · **Test** · [[ES-HNK-30 - Demo juri dan narasi dari judging|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-30.1 | Fuzz kanonikalisasi: mutasi invoice hanya berakhir di 偽 atau 重 (AC-HNK-30.1) | TODO | — | — |
| U-HNK-30.2 | Exhibit A tidak memuat field selain dua tanda tangan, N, dan rujukan papan (AC-HNK-30.4) | TODO | — | — |
| U-HNK-30.3 | Entri dengan kelas terenkripsi: pemegang UFVK tidak bisa membaca kelas; financier bisa (AC-HNK-30.6) | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-30.1 | Dua pintu keluar memukul papan testnet hidup (AC-HNK-30.3) | TODO | — | — |
| I-HNK-30.2 | Alur emas dari snapshot statis saat relay dimatikan (AC-HNK-30.8) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buka tautan kit invoice, coba double-finance di meja financier kedua, unduh Exhibit A, verifikasi di `/verify`

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
