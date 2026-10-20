---
tags: [es, "HNK-26"]
type: es
id: HNK-26
phase: F5
status: PARSIAL
updated: 2026-10-20
---

# ES-HNK-26 - Konsol dan API node financier

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-26 - Konsol dan API node financier|AC]] · [[TEST-HNK-26 - Konsol dan API node financier|Test]] · **Exec Summary**

## Apa diubah
- **T14 (Hans), library, lokal:** `Flow::double_sign_proof(buyer_signature)` di `jitsuin-flow`: deal yang berhenti `DoubleFinanced` menghasilkan bukti tanda tangan ganda dengan posisi papan kedua entri, sehingga lolos `jitsuin verify` dan layar Verify. Penyimpanan di deal dan kartu konsol menunggu node.
- **T8 (Hans):** `check_buyer` sudah ada di `jitsuin-flow` (HNK-20.T3); endpoint dan penyimpanan tag menunggu node.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Deal tanpa operator di terminal | 100% | — |

## Status
**PARSIAL.** Bagian library T14 selesai lokal; node (T1, Dex) belum ada, jadi API, penyimpanan, dan konsol belum.

## Risiko tersisa
_TODO_

## Bukti
- Commit: _TODO_
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
