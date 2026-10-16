---
tags: [spike, "SPK-17"]
type: spike
id: SPK-17
area: Tooling
owner: Dave
status: PASS
updated: 2026-10-16
---

# SPK-17 - Toolchain frontend dan aset offline

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Dave #dave · **Area:** Tooling · **Dipakai oleh:** HNK-10, HNK-11, HNK-08

## Tujuan
Pastikan stack frontend bisa di-build lokal tanpa resource pihak ketiga saat runtime.

## Hipotesis
Vite + React + TypeScript dengan Node yang terpasang cukup; semua aset bisa di-bundle.

## Langkah
1. Scaffold Vite React-TS di scratchpad.
2. `npx tsc -b --noEmit` dan `npm run build`.
3. Cari resource eksternal (src/href/@import/url) di hasil build.

## Kriteria lulus
- [x] Typecheck dan build hijau.
- [x] 0 resource eksternal yang dimuat saat runtime.

## Fallback kalau gagal
- Stack lain yang lebih ringan (misalnya HTML + TypeScript tanpa framework).

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Node 26.11.1, npm 11.20.0. Scaffold Vite 8.3.4 + React 19.3.1 + TypeScript 6.0.3; `tsc` hijau; `npm run build` exit 0 dalam 1,08 dtk; `dist/index.html` memuat 0 resource eksternal (link `<a>` bawaan template dihapus saat build nyata). pnpm tidak terpasang (tidak dibutuhkan). | Usulan stack frontend: Vite + React + TypeScript (perlu persetujuan user, catat di Decision Log). |

## Catatan
_TODO_
