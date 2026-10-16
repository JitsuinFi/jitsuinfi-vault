---
tags: [test, "HNK-08"]
type: test
id: HNK-08
phase: F4
lead: Dex
owners: [Dex, Dave]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-08 - Indeks suku bunga publik

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-08 - Indeks suku bunga publik|AC]] · **Test** · [[ES-HNK-08 - Indeks suku bunga publik|Exec Summary]]

**Lead:** Dex #dex · **Tim:** Dex #dex, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-08.1 | Agregasi bucket | TODO | — | — |
| U-HNK-08.2 | Ambang k | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-08.1 | Indeks dari entri `TES-` di papan uji | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buka halaman indeks dan cocokkan dengan hasil `jitsuin index`.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
