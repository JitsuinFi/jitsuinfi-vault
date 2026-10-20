---
tags: [fe-tool, "FE-25"]
type: fe-tool
id: FE-25
layer: komponen
status: BELUM-TERPASANG
updated: 2026-10-20
---

# FE-25 - React Bits shadcn MCP

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Pustaka komponen animasi React dan Next.js, diakses lewat MCP registry shadcn.

## Akar
| | |
|---|---|
| Repo | https://github.com/DavidHDev/react-bits; dokumentasi https://reactbits.dev/get-started/introduction |
| Lisensi | **MIT + Commons Clause v1.0** (`LICENSE.md`): boleh dipakai dan dimodifikasi sebagai bagian aplikasi atau situs; menjual komponennya sendiri tidak boleh |
| Isi | Komponen animasi React; tiap komponen dalam 4 varian: `JS-CSS`, `JS-TW`, `TS-CSS`, `TS-TW`. Katalog 218 komponen dengan dependensi dan bobot: `PortoWeb/_resources/notes/reactbits-catalog.md` |
| Pasang komponen | `npx shadcn@latest add @react-bits/<Nama>-<JS\|TS>-<CSS\|TW>`, contoh `npx shadcn@latest add @react-bits/SplitText-TS-TW` |
| Perintah MCP dari user | `npx shadcn@latest mcp init --client claude` ([[Landing Page - Brief]], [[FE-M0 - Mandat FE]]); dokumentasi shadcn menulisnya `pnpm dlx shadcn@latest mcp init --client claude`, lalu restart Claude Code. Konfigurasi manual yang didokumentasikan: `.mcp.json` di root proyek dengan server `shadcn` = `npx shadcn@latest mcp` |
| Status | **Belum dijalankan untuk JitsuinFi**; tidak ada server shadcn di `claude mcp list` sesi ini. Sudah terkonfigurasi di PortoWeb (`PortoWeb/.mcp.json`, registry `@react-bits` di `Hans_Porto_Web/components.json`) |

## Kecocokan dengan JitsuinFi
- Komponen React; frontend JitsuinFi vanilla TypeScript tanpa React ([[FE-03 - TypeScript]]). Memakai komponen apa adanya berarti menambah React (dependensi baru, butuh izin).
- Jalan tengah: pakai sebagai referensi efek, lalu tulis ulang dengan anime.js atau Motion.
- `shadcn mcp init` menulis konfigurasi MCP proyek; jalankan hanya dengan izin user. Registry shadcn butuh `components.json` (proyek React + Tailwind); frontend JitsuinFi tidak punya keduanya.
- Temuan katalog PortoWeb (`reactbits-catalog.md`, 2026-10-18):
  - 28 komponen mengimpor `motion/react` (paket `motion` v12), bukan `framer-motion`.
  - 5 komponen mencantumkan `react-dom@^19` di registry (`TargetCursor`, `Dock`, `Masonry`, `WarmTooltip`, `Shredder`); `ModelViewer` butuh React 19.
  - 102 komponen WebGL, hanya 16 yang menarik `ogl` atau `three`; sisanya **WebGL2 mentah tanpa dependensi** dengan loop yang sudah benar (DPR ≤ 2, berhenti di luar layar dan tab tersembunyi, satu frame statis saat reduced motion).
  - 130 dari 218 komponen tanpa dependensi npm.
- **Akibat untuk JitsuinFi (vanilla TS):** shader dan loop WebGL2 React Bits bisa di-port ke vanilla tanpa React; ini jalan memakai React Bits tanpa menambah React. Cek lisensi (Commons Clause) dan CSP (shader inline di JS boleh, `style-src 'self'` tetap berlaku).

## Status
BELUM TERPASANG.
