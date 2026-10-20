---
tags: [fe-tool, "FE-09"]
type: fe-tool
id: FE-09
layer: library-motion
status: AKTIF
updated: 2026-10-20
---

# FE-09 - Motion

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Library Motion (dulu Framer Motion) versi JavaScript murni, dipakai untuk pemicu scroll dan gestur.

## Akar
| | |
|---|---|
| Paket | `motion` 14.3.0 (MIT, https://github.com/motiondivision/motion) |
| Asal permintaan | Daftar tool di [[Landing Page - Brief]] |
| Bukan | motion.so (generator video, lihat [[FE-23 - Motion.so]]) |

## Dipakai di
| File | API |
|---|---|
| `src/landing/hero.ts` | `animate` (diimpor sebagai `motionAnimate`), `hover`, `press` (tombol magnetik, efek tekan) |
| `fingerprint.ts`, `sealchain.ts`, `twice.ts`, `history.ts`, `finale.ts` | `inView` (memulai bab saat masuk layar) |

## Pembagian kerja dengan anime.js
- anime.js: timeline dan animasi nilai (lihat [[FE-08 - anime.js]]).
- Motion: kapan mulai (`inView`) dan interaksi pointer (`hover`, `press`).

## Batasan
- Varian React (`motion/react`) tidak dipakai karena app tanpa React.
- Sub-skill panduan: `framer-motion` di genjutsu ([[FE-13 - genjutsu]]).

## Status
AKTIF (landing).
