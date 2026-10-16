---
tags: [test, "HNK-10"]
type: test
id: HNK-10
phase: F5
lead: Dave
owners: [Dave, Hans, Dex]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-10 - Web app per peran

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-10 - Web app per peran|AC]] · **Test** · [[ES-HNK-10 - Web app per peran|Exec Summary]]

**Lead:** Dave #dave · **Tim:** Dave #dave, Hans #hans, Dex #dex

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-10.1 | Validasi input dan komponen (TypeScript) | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-10.1 | Frontend ↔ backend uji di Railway staging (setelah persetujuan deploy) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Checklist per peran: supplier, buyer, financier.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
