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
- **T2 (Hans), di-merge:** `jitsuin-board` `ProofOnBoard` (satu field per klaim) dipakai CLI dan wasm `verifyProofOnBoard`; layar Verify memeriksa posisi bukti terhadap data papan, tanpa data papan posisi ditulis sebagai klaim. Bukti tanpa posisi pertama FAIL di web dan CLI.
- **T6 (Hans), di-merge (PR #10, `c73009b`):** UFVK papan testnet dipublikasikan di `jitsuinfi-zcash/examples/testnet/board-ufvk.txt` (D-11, disetujui user 2026-10-20), birthday 4508703, snapshot papan live, dan bukti pembiayaan ganda `TES-INV-0003` yang dibangun ulang dari papan. README punya bagian "For judges" (scan live, indeks, offline, layar Verify).
- **T3 (Hans), di-merge:** `rate_index_json` bersama; wasm `rateIndex` sama dengan `jitsuin index --json`. Halaman `#/index` (HNK-08.T3, Hans, dari Dave, D-35) belum ada.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Verdict web vs CLI berbeda | 0 | 0 (I-HNK-28.2; I-HNK-28.4 di data testnet asli) |
| Pertanyaan juri ke tim untuk verifikasi | 0 | 0: uji wallet baru hanya dengan data README (I-HNK-28.3) |

## Status
**PARSIAL.** T2, T3 DONE (di-merge); T6 DONE (di-merge); halaman indeks, snapshot otomatis, dan sisa item belum.

## Risiko tersisa
- UFVK baru publik saat repo `jitsuinfi-zcash` dibuka (DEV-19, menjelang submit).
- Snapshot berhenti di blok 4511024; scan live setelahnya bisa menampilkan entri baru (README menyebutnya).
- Build image pertama sekitar 4 menit di Docker arm64 native (OrbStack); di daemon x86_64 teremulasi (colima di mesin ini) jauh lebih lama.

## Bukti
- Commit: _TODO_
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: 2026-10-20 ("Gas push semua dan buka PR", "cek lagi, kalau hijau merge #10"); T6 di-merge `c73009b`
