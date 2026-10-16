---
tags: [test, "HNK-04"]
type: test
id: HNK-04
phase: F2
lead: Hans
owners: [Hans, Dex]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-16
---

# TEST-HNK-04 - Pemindai papan registry

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-04 - Pemindai papan registry|AC]] · **Test** · [[ES-HNK-04 - Pemindai papan registry|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-04.1 | Aturan urutan dan tie-break | TODO | — | — |
| U-HNK-04.2 | Deteksi N ganda dari daftar entri | TODO | — | — |
| U-HNK-04.3 | Filter entri invalid | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-04.1 | Posting 3 entri `TES-` (1 invalid) ke papan uji, lalu scan → 2 valid dan 1 ditolak | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] `jitsuin board scan` menampilkan tabel entri dan statusnya.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
