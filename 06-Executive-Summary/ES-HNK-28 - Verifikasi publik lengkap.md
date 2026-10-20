---
tags: [es, "HNK-28"]
type: es
id: HNK-28
phase: F4
status: PARSIAL
updated: 2026-10-20
---

# ES-HNK-28 - Verifikasi publik lengkap

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-28 - Verifikasi publik lengkap|AC]] · [[TEST-HNK-28 - Verifikasi publik lengkap|Test]] · **Exec Summary**

## Apa diubah
- **T2 (Hans), lokal:** `jitsuin-board` `ProofOnBoard` (satu field per klaim) dipakai CLI dan wasm `verifyProofOnBoard`; layar Verify memeriksa posisi bukti terhadap data papan, tanpa data papan posisi ditulis sebagai klaim. Bukti tanpa posisi pertama FAIL di web dan CLI.
- **T3 (Hans), lokal:** `rate_index_json` bersama; wasm `rateIndex` sama dengan `jitsuin index --json`. Halaman `#/index` (HNK-08.T3, Dave) belum ada.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Verdict web vs CLI berbeda | 0 | — |

## Status
**PARSIAL.** T2, T3 DONE (lokal); halaman indeks, snapshot otomatis, dan sisa item belum.

## Risiko tersisa
_TODO_

## Bukti
- Commit: _TODO_
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
