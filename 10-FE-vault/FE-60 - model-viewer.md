---
tags: [fe-tool, "FE-60", monad-blitz]
type: fe-tool
id: FE-60
layer: library-3d
status: REFERENSI
updated: 2026-10-23
---

# FE-60 - model-viewer

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Web component `<model-viewer>` untuk menampilkan satu model GLB/glTF: orbit, poster, loading, anotasi, AR.

## Akar
| | |
|---|---|
| Jenis | Komponen web |
| Sumber | https://github.com/google/model-viewer · https://modelviewer.dev |
| Pasang | `npm i @google/model-viewer` |
| Bobot | `model-viewer.min.js` 1.069.272 byte (~1,07 MB, jsDelivr) + model GLB |
| Lisensi | Apache-2.0 |
| Lokasi | Belum dipasang di proyek ini |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-40 (2026-10-23) |
| Vonis di Monad Blitz | **DITOLAK**; dipakai di: — |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: ~1 MB JS + model GLB; perlu izin dependensi dan bundle lokal.

## Catatan
8.287★, push terakhir 2026-10-09 (GitHub API). MVP tidak memakai GLB (D-11: figur SVG); 1 MB terlalu berat untuk `/pesan` di HP. Pertimbangkan hanya bila nanti ada model 3D di `/layar`.

Ditemukan lewat RS-01 - Lightweight Detailed 3D Assets (vault Monad Blitz) (author Gpt 6.1 sol - agentrouter); dicek ulang 2026-10-22.

## Status
REFERENSI (untuk JitsuinFi).
