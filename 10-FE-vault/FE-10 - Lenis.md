---
tags: [fe-tool, "FE-10"]
type: fe-tool
id: FE-10
layer: library-motion
status: AKTIF
updated: 2026-10-20
---

# FE-10 - Lenis

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Smooth scroll yang menjadi "jam cerita" landing (adegan dipin 160 – 220vh).

## Akar
| | |
|---|---|
| Paket | `lenis` 1.3.27 (MIT, https://github.com/darkroomengineering/lenis) |
| Asal | `MASTER.md` §1 Interaction thesis dan §5 (Lenis duration 1.2) |

## Dipakai di
- `src/landing/main.ts`: `new Lenis({ duration: 1.2 })`, loop `requestAnimationFrame` memanggil `lenis.raf(t)`.
- Mati bila `prefers-reduced-motion: reduce`.

## Status
AKTIF (landing). App tidak memakai Lenis.
