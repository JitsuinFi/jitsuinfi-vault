---
tags: [test, "HNK-31"]
type: test
id: HNK-31
phase: F6
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-22
---

# TEST-HNK-31 - Migrasi FE ke React dan TanStack Router

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-31 - Migrasi FE ke React dan TanStack Router|AC]] · **Test** · [[ES-HNK-31 - Migrasi FE ke React dan TanStack Router|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-31.1 | `npm test` 78 test `src/lib/*` lulus setelah tiap task | TODO | — | — |
| U-HNK-31.2 | Pengalihan tautan lama: `#/supplier`, `app.html#/verify`, `/console.html` ke route baru (test unit fungsi redirect) | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-31.1 | Paritas visual per halaman: tangkapan layar 1440 × 900 dan 390 × 844 dibandingkan berdampingan dengan `assets/hnk31-baseline/`, dicatat per task T3 – T10 | TODO | — | — |
| I-HNK-31.2 | Nol pelanggaran CSP dan nol error console di semua route (`vite preview` dengan header produksi) | TODO | — | — |
| I-HNK-31.3 | E2E lokal testnet di FE baru: siklus penuh sampai settled | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Buka tiap URL bersih di production setelah deploy, bandingkan dengan patokan
- [ ] Jalankan E2E lokal (relay, node, web app) dengan passkey di Chrome

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
