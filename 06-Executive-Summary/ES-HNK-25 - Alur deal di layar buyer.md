---
tags: [es, "HNK-25"]
type: es
id: HNK-25
phase: F5
status: PARSIAL
updated: 2026-10-20
---

# ES-HNK-25 - Alur deal di layar buyer

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-25 - Alur deal di layar buyer|AC]] · [[TEST-HNK-25 - Alur deal di layar buyer|Test]] · **Exec Summary**

## Apa diubah
- **T2 (Hans), di-merge, PARSIAL:** `jitsuin-board` `own_chain` + wasm `historyNext`; layar buyer tanpa kolom `k`: `k` berikutnya dari sertifikat yang disimpan terenkripsi, dicek ke papan bila ada data papan; tanda tangan, segel, dan bayar mencari `k` dari key tujuan invoice; sertifikat terbit menyambung ke sertifikat tersimpan. Sisa: bagikan key dan permintaan riwayat lewat relay, kepala rantai di relay (HNK-23).
- Perbaikan: sign up dari layar peran kini menampilkan onboarding dulu.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| QR dari surat belum Sealed | 0 | — |

## Status
**PARSIAL.** T2 PARSIAL (di-merge); AC-HNK-25.1 PASS.

## Risiko tersisa
_TODO_

## Bukti
- Commit: _TODO_
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
