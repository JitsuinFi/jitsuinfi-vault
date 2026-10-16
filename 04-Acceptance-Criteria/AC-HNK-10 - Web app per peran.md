---
tags: [ac, "HNK-10"]
type: ac
id: HNK-10
phase: F5
lead: Dave
owners: [Dave, Hans, Dex]
status: TODO
updated: 2026-10-16
---

# AC-HNK-10 - Web app per peran

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-10 - Web app per peran|Test]] · [[ES-HNK-10 - Web app per peran|Exec Summary]]

**Item:** HNK-10 · **Fase:** F5 · **Dependency:** HNK-05, HNK-06, SPK-09

**Lead:** Dave #dave · **Tim:** Dave #dave, Hans #hans, Dex #dex

## Deskripsi
Antarmuka web untuk supplier, buyer, dan financier; tanpa CDN pihak ketiga, analytics, atau cookie pelacak; header CSP ketat.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-10.1 | Alur supplier, buyer, dan financier bisa dijalankan dari browser. | TODO | — | — |
| AC-HNK-10.2 | 0 request ke domain pihak ketiga (bukti DevTools). | TODO | — | — |
| AC-HNK-10.3 | Header CSP aktif; tanpa cookie pelacak. | TODO | — | — |
| AC-HNK-10.4 | Diuji dalam keadaan logout dari jaringan lain. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
