---
tags: [fe-tool, "FE-62", monad-blitz]
type: fe-tool
id: FE-62
layer: layanan
status: REFERENSI
updated: 2026-10-23
---

# FE-62 - Meshy dan Tripo

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Generasi model 3D dari teks/gambar dengan kontrol jumlah face; Meshy MCP dan skills, Tripo CLI dengan mode MCP (`tripo mcp`).

## Akar
| | |
|---|---|
| Jenis | Layanan AI 3D |
| Sumber | Meshy: https://docs.meshy.ai/en/api/text-to-3d · https://github.com/meshy-dev/meshy-mcp-server · https://github.com/meshy-dev/meshy-3d-agent — Tripo: https://developers.tripo3d.ai/en/docs/cli |
| Pasang | Meshy: API key (Bearer). Tripo: `npm install -g tripo-cli` (Node ≥ 20) lalu `tripo login` |
| Bobot | Meshy: **wajib paket berbayar** (error 402), kredit per task. Tripo: kredit per generasi. Output mesh (GLB/OBJ/FBX/STL/USDZ di Meshy) |
| Lisensi | Repo MCP/skills Meshy MIT; layanan komersial |
| Lokasi | Belum dipasang di proyek ini |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-42 (2026-10-23) |
| Vonis di Monad Blitz | **DITOLAK**; dipakai di: — |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: Layanan berbayar; output mesh GLB, bukan bagian bundle. Prompt dikirim ke pihak ketiga.

## Catatan
Meshy MCP 84★ dan skills 103★, keduanya MIT (GitHub API). Meshy Smart Topology `meshy-t2.5`: 100–30.000 face; mode `lowpoly` dihentikan 30 Okt 2026. Tripo: preset `game-mobile`, `--face-limit`. Ditolak karena berbayar, output mesh (bukan SVG), gaya tidak konsisten dengan iso-figure, dan prompt dikirim ke layanan pihak ketiga.

Ditemukan lewat RS-01 - Lightweight Detailed 3D Assets (vault Monad Blitz) (author Gpt 6.1 sol - agentrouter); dicek ulang 2026-10-22.

## Status
REFERENSI (untuk JitsuinFi).
