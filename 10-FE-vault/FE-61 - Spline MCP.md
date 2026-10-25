---
tags: [fe-tool, "FE-61", monad-blitz]
type: fe-tool
id: FE-61
layer: mcp
status: REFERENSI
updated: 2026-10-23
---

# FE-61 - Spline MCP

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Agent membuat dan mengedit scene 3D Spline dan desain Hana; ekspor ke React, Next.js, Vanilla JS, three.js, R3F; publish ke URL publik.

## Akar
| | |
|---|---|
| Jenis | MCP |
| Sumber | https://docs.spline.design/generate/spline-mcp-server.md · skills: https://github.com/splinetool/spline-skills |
| Pasang | Claude Code: `claude mcp add --transport http --scope user spline https://mcp.spline.design/mcp`; atau server bawaan aplikasi desktop Spline (`127.0.0.1`) |
| Bobot | Butuh akun Spline (OAuth); kuota harian per paket + batas per menit; runtime Spline/three.js di halaman |
| Lisensi | Docs Spline; repo skills MIT |
| Lokasi | Belum dipasang di proyek ini |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-41 (2026-10-23) |
| Vonis di Monad Blitz | **DITOLAK**; dipakai di: — |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: Runtime Spline/three.js dan scene di cloud Spline: bertentangan dengan FE-01 (CDN, layanan luar).

## Catatan
Output berupa file Spline di cloud, bukan SVG milik kita; runtime 3D berat untuk HP; menambah MCP mengubah config Claude (butuh persetujuan). Repo `splinetool/spline-skills` baru dibuat 2026-10-22, 0★. Fitur restore versi khusus paket berbayar.

Ditemukan lewat RS-01 - Lightweight Detailed 3D Assets (vault Monad Blitz) (author Gpt 6.1 sol - agentrouter); dicek ulang 2026-10-22.

## Status
REFERENSI (untuk JitsuinFi).
