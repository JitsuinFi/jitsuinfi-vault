---
tags: [test, "HNK-28"]
type: test
id: HNK-28
phase: F4
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-28 - Verifikasi publik lengkap

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-28 - Verifikasi publik lengkap|AC]] · **Test** · [[ES-HNK-28 - Verifikasi publik lengkap|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-28.1 | `verifyProofOnBoard` menolak posisi palsu | TODO | — | — |
| U-HNK-28.2 | `rateIndex` sama dengan `rate_index` | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-28.1 | Snapshot relay dibandingkan dengan `jitsuin verify --save-board` | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buka Verify, tempel bundel contoh
- [ ] Buka halaman indeks
- [ ] Buka halaman orang luar

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
