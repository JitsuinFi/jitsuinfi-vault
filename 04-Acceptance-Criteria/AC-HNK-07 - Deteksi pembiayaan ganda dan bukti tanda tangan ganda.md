---
tags: [ac, "HNK-07"]
type: ac
id: HNK-07
phase: F3
lead: Hans
owners: [Hans, Dave, Dex]
status: TODO
updated: 2026-10-16
---

# AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|Test]] · [[ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|Exec Summary]]

**Item:** HNK-07 · **Fase:** F3 · **Dependency:** HNK-05

**Lead:** Hans #hans · **Tim:** Hans #hans, Dave #dave, Dex #dex

## Deskripsi
Financier kedua yang menerima invoice yang sama menemukan N di papan dan mendapat bundel bukti bahwa supplier menandatangani dua kali.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-07.1 | Financier B menolak invoice yang N-nya sudah terdaftar. | TODO | — | — |
| AC-HNK-07.2 | Bundel bukti (dua tanda tangan key sementara supplier atas N yang sama dengan commitment financier berbeda) bisa diverifikasi offline. | TODO | — | — |
| AC-HNK-07.3 | Orang luar tanpa invoice tidak bisa memahami isi entri atau bundel. | TODO | — | — |
| AC-HNK-07.4 | Didemokan di mainnet dengan `TES-INV-0003`. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
