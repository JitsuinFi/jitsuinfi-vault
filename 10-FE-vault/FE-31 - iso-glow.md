---
tags: [fe-tool, "FE-31", monad-blitz]
type: fe-tool
id: FE-31
layer: skill
status: REFERENSI
updated: 2026-10-23
---

# FE-31 - iso-glow

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Satu figur `.html` isometrik garis halus; bagian menyala dan bereaksi saat ditekan; opsi 3D three.js dan gaya Lumen.

## Akar
| | |
|---|---|
| Jenis | Skill (April Zhu) |
| Sumber | https://iso-glow.vercel.app |
| Pasang | `curl … | tar -xz -C ~/.claude/skills` |
| Bobot | ~300 KB file skill; figur 3D memuat three.js dari CDN |
| Lisensi | MIT |
| Lokasi | Belum dipasang di proyek ini |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-06 (2026-10-23) |
| Vonis di Monad Blitz | **PERLU REVIEW**; dipakai di: BLZ-16.T3 (1–2 figur utama) |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: Figur 3D iso-glow memuat three.js dari CDN: melanggar FE-01 kecuali three.js di-bundle lewat Vite (JitsuinFi sudah punya three.js 0.186.1, FE-07). Figur 2D (SVG) aman.

## Catatan
Ambil SVG dari HTML ke komponen React. Pin versi three.js atau bundle lokal.

## Status
REFERENSI (untuk JitsuinFi).
