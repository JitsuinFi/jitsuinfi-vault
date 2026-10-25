---
tags: [fe-tool, "FE-59", monad-blitz]
type: fe-tool
id: FE-59
layer: tool
status: REFERENSI
updated: 2026-10-23
---

# FE-59 - SVGO

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Optimasi SVG: buang metadata, rapikan path, kecilkan angka.

## Akar
| | |
|---|---|
| Jenis | Tool |
| Sumber | https://github.com/svg/svgo · https://svgo.dev · GUI: https://jakearchibald.github.io/svgomg/ |
| Pasang | `npm i -D svgo` lalu `npx svgo in.svg -o out.svg` |
| Bobot | Dev dependency saja (4.1.0, 1,49 MB unpacked); tidak ikut ke bundle |
| Lisensi | MIT |
| Lokasi | Belum dipasang di proyek ini |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-39 (2026-10-23) |
| Vonis di Monad Blitz | **KANDIDAT**; dipakai di: Pasca-proses SVG dari iso-figure/Anatomy sebelum masuk `/pesan` |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: Library/aset baru perlu izin dependensi dan di-bundle lokal (FE-01: tanpa CDN).

## Catatan
22.766★, push terakhir 2026-08-27 (GitHub API). **Hati-hati:** matikan plugin yang mengganti/menghapus `id` dan `class` (`cleanupIds`, `removeUnknownsAndDefaults`) karena `render()` figur memakai class toggle; jangan pakai pada SVG dengan filter/ID yang dirujuk script. Cek visual sebelum dan sesudah.

Ditemukan lewat RS-01 - Lightweight Detailed 3D Assets (vault Monad Blitz) (author Gpt 6.1 sol - agentrouter); dicek ulang 2026-10-22.

## Status
REFERENSI (untuk JitsuinFi).
