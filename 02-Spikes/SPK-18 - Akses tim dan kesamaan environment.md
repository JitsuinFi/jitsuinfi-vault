---
tags: [spike, "SPK-18"]
type: spike
id: SPK-18
area: Infra
owner: Dex
status: TODO
updated: 2026-10-16
---

# SPK-18 - Akses tim dan kesamaan environment

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dex #dex · **Area:** Infra · **Dipakai oleh:** Semua item

## Tujuan
Pastikan Hans, Dex, dan Dave punya akses dan environment yang sama sebelum build paralel.

## Hipotesis
Akses GitHub, Railway, dan vault bisa disiapkan dalam satu hari.

## Langkah
1. Undang Dex dan Dave ke repo GitHub (setelah repo dibuat, SPK-14) dan project Railway.
2. Tentukan cara berbagi vault (di dalam repo atau sinkronisasi lain).
3. Cek versi Rust, Node, dan Docker di mesin Dex dan Dave; samakan dengan `rust-toolchain.toml` dan `.nvmrc`.
4. Sepakati kebijakan rahasia: seed tidak pernah dibagikan; secret lewat env Railway.

## Kriteria lulus
- [ ] Dex dan Dave bisa clone, build, dan menjalankan test.
- [ ] Versi toolchain tercatat dan sama.
- [ ] Kebijakan rahasia disepakati.

## Fallback kalau gagal
- Dex dan Dave memakai container dev yang sama (Docker).

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| TODO | 2026-10-16 | Belum dijalankan. | Butuh info mesin Dex dan Dave, serta undangan repo dan Railway. |

## Catatan
_TODO_
