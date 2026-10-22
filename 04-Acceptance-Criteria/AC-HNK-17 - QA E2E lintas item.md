---
tags: [ac, "HNK-17"]
type: ac
id: HNK-17
phase: F6
lead: Hans
owners: [Hans]
status: TODO
updated: 2026-10-16
---

# AC-HNK-17 - QA E2E lintas item

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-17 - QA E2E lintas item|Test]] · [[ES-HNK-17 - QA E2E lintas item|Exec Summary]]

**Item:** HNK-17 · **Fase:** F6 · **Dependency:** HNK-05 – HNK-11

**Lead:** Hans #hans · **Tim:** Hans #hans 

## Deskripsi
Tester independen menjalankan semua panduan E2E di file TEST tiap item, mencatat hasilnya di tabel E2E masing-masing, dan melaporkan bug ke [[Backlog]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-17.1 | Setiap item HNK-01 – HNK-11 punya hasil E2E tercatat (PASS/FAIL + tanggal) oleh tester yang bukan pembuat item. | PASS | 2026-10-22 | Putaran 1 HNK-01 – HNK-07 (HNK-17.T1, `TES-INV-E2E1-77210`) dan putaran 2 HNK-08 – HNK-11 (HNK-17.T2) di [[TEST-HNK-17 - QA E2E lintas item]]; tester agent (DEV-35) |
| AC-HNK-17.2 | Setiap bug dicatat (item baru atau DEV) dengan langkah reproduksi. | TODO | — | — |
| AC-HNK-17.3 | Bug yang diperbaiki di-retest dan hasilnya dicatat. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
