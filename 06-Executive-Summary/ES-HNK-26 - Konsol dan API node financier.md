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
- **T14 (Hans), library, di-merge (PR #11, `01ecdc3`):** `Flow::double_sign_proof(buyer_signature)` di `jitsuin-flow`: deal yang berhenti `DoubleFinanced` menghasilkan bukti tanda tangan ganda dengan posisi papan kedua entri, sehingga lolos `jitsuin verify` dan layar Verify. Penyimpanan di deal dan kartu konsol menunggu node.
- **T10 (Hans), library, PR #12:** snapshot deal `Flow::to_bytes` / `Flow::from_bytes` (format `JTSF` v1, ditulis manual seperti format lain di repo, tanpa dependency baru). Pemuatan mengecek ulang deal, entri kita, dan segel surat. Penyimpanan di node menunggu T1.
- **T8 (Hans):** `check_buyer` sudah ada di `jitsuin-flow` (HNK-20.T3); endpoint dan penyimpanan tag menunggu node.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Deal tanpa operator di terminal | 100% | — |

## Status
**PARSIAL.** Bagian library T14 di-merge, T10 di PR #12; node (T1, Dex) belum ada, jadi API, penyimpanan, dan konsol belum.

## Risiko tersisa
_TODO_

## Bukti
- Commit: _TODO_
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
