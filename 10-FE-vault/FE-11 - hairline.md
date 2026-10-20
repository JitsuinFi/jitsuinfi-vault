---
tags: [fe-tool, "FE-11"]
type: fe-tool
id: FE-11
layer: library-ilustrasi
status: TERPASANG-TIDAK-DIPAKAI
updated: 2026-10-20
---

# FE-11 - hairline

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

33 figur garis isometrik yang bereaksi ke pointer.

## Akar
| | |
|---|---|
| Paket | `@lucasmarkes/hairline` 0.5.1 (MIT, https://hairline.lucasmarkes.com, repo https://github.com/lucasmarkes/hairline) |
| Asal permintaan | Daftar tool di [[Landing Page - Brief]] |
| Dipasang | Commit frontend `7fd1e49` (landing: design system MASTER.md, bab 1) |
| Rencana | `MASTER.md` §1 "Allowed patterns": figur garis hairline untuk dokumen |

## Temuan audit 2026-10-20
- **Tidak di-import di file mana pun** di `src/`, `index.html`, atau `app.html`. Paket ada di `dependencies` dan `node_modules`, tetapi tidak masuk bundle.
- Figur dokumen di landing sekarang digambar sendiri (SVG dan canvas).

## Pilihan tindak lanjut
1. Pakai: cocok untuk ilustrasi dokumen di layar app (HNK-21, Dex) atau bab landing.
2. Hapus dari `package.json` bila tidak dipakai sampai submit (perlu izin user).

## Status
TERPASANG, BELUM DIPAKAI.
