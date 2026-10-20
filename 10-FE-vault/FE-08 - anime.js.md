---
tags: [fe-tool, "FE-08"]
type: fe-tool
id: FE-08
layer: library-motion
status: AKTIF
updated: 2026-10-20
---

# FE-08 - anime.js

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Mesin animasi utama landing: entri teks, segel, garis SVG, timer episode hero.

## Akar
| | |
|---|---|
| Paket | `animejs` 4.5.0 (MIT, https://animejs.com, dokumentasi https://animejs.com/documentation) |
| Asal permintaan | Daftar tool di [[Landing Page - Brief]] |
| Token gerak | `src/landing/motion.ts`: `ease` (softLand, snapSettle, glide, softInOut, accelExit, popOver, linear) dan `dur` (67 – 2400 ms), sama dengan `MASTER.md` §5 |

## Dipakai di
| File | API |
|---|---|
| `src/landing/hero.ts` | `animate`, `stagger`, `createTimer` (rail episode), tipe `JSAnimation`, `Timer` |
| `src/landing/fingerprint.ts` | `animate`, `stagger`, `svg.createDrawable` (garis sidik jari) |
| `src/landing/print.ts`, `history.ts` | `animate`, `stagger`, `svg` |
| `src/landing/sealchain.ts` | `animate`, `svg` |
| `src/landing/twice.ts` | `animate` |
| `src/landing/finale.ts` | `animate`, `stagger` (amplop, huruf, segel) |

Ease dikirim sebagai fungsi (`fn(ease.softLand)`) agar kurva persis sama dengan motionmaxxing ([[FE-26 - motionmaxxing]]).

## Basis pengetahuan
- `PortoWeb/_resources/notes/animejs-v4.md`: digest API anime.js 4.5.0 yang dicek ke source (core, easing, `onScroll`/ScrollObserver, `splitText`/`scrambleText`, SVG, Draggable dan Layout, Scope, modul WAAPI, gotcha dan performa).
- Klon source: `PortoWeb/_resources/repos/anime` (commit `01b81be`).
- Fitur yang belum dipakai landing JitsuinFi: `onScroll` (scroll-driven), `splitText`/`scrambleText` (teks), `Draggable`, modul WAAPI.

## Batasan
- Reduced motion: `reducedMotion()` di `motion.ts`; setiap bab menampilkan keadaan akhir.
- Larangan dari `MASTER.md`: fade tunggal, stagger fade-up seragam, bounce atau elastic (kecuali satu `popOver`).

## Status
AKTIF (landing). App belum memakai animasi.
