---
tags: [fe-tool, "FE-12"]
type: fe-tool
id: FE-12
layer: library-font
status: AKTIF
updated: 2026-10-20
---

# FE-12 - Font Fontsource

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Tiga font dibundel lokal lewat paket Fontsource (tanpa Google Fonts).

## Akar
| Paket | Versi | Lisensi | Peran (`MASTER.md` §3) |
|---|---|---|---|
| `@fontsource/shippori-mincho-b1` | 5.3.0 | OFL-1.1 | Display dan segel (berat 700, 800) |
| `@fontsource-variable/geist` | 5.3.0 | OFL-1.1 | Caption, navigasi, tombol |
| `@fontsource-variable/geist-mono` | 5.3.0 | OFL-1.1 | Data nyata saja (N, txid, hex) |

## Dipakai di
- `src/landing/tokens.css` baris 2 – 5: `@import` empat file CSS Fontsource; Vite menyalin `woff2` ke `dist/assets/`.
- Token: `--f-display`, `--f-seal`, `--f-body`, `--f-mono` (dengan fallback sistem; varian 中文 memakai Songti SC dan PingFang SC).
- App (`src/style.css`) **tidak** memakai font ini: `--sans` dan `--mono` adalah font sistem.

## Batasan
- `font-src 'self'`: font dari URL luar akan diblokir.
- Lisensi OFL boleh dipakai komersial; catat juga di [[VID-05 - Aset dan Lisensi]] bila dipakai di video.

## Status
AKTIF (landing).
