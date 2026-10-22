---
tags: [es, "HNK-31"]
type: es
id: HNK-31
phase: F6
status: BELUM
updated: 2026-10-22
---

# ES-HNK-31 - Migrasi FE ke React dan TanStack Router

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-31 - Migrasi FE ke React dan TanStack Router|AC]] · [[TEST-HNK-31 - Migrasi FE ke React dan TanStack Router|Test]] · **Exec Summary**

## Apa diubah
Web app JitsuinFi (landing, app, konsol financier) pindah dari TypeScript tanpa framework (helper `h()`, tiga entri HTML, routing hash) ke React 19 + TanStack Router: satu SPA statis di atas Vite, route berbasis file (`src/routes/`), URL bersih (`/supplier`, `/verify`, `/console`, ...), alamat lama dialihkan. Next.js ditolak karena script inline-nya melanggar CSP (D-52). Animasi (anime.js, three.js, hairline) tetap imperatif lewat ref; logika `src/lib/*` tidak berubah. Dikerjakan satu halaman per task, berurutan, dengan patokan visual dari build lama.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Paritas visual per halaman | 100 % halaman sama dengan patokan (1440 dan 390 px) | 100 %: 0,00 % di semua halaman; beda hanya data live, kota 3D beranimasi, sidik jari passkey virtual, port host |
| Pelanggaran CSP | 0 | 0 di 18 route, 0 error JS |
| Test `src/lib/*` | 78/78 lulus | 80/80 (78 + 2 baru) |
| JS awal tambahan | ≤ 60 KB gzip (direvisi ≤ 100 KB) | +93 – 95 KB per dunia (deviasi tercatat) |
| Siklus E2E di FE baru | sampai settled | settled, bundle genuine di `/verify` (`TES-INV-FE-36210`) |

## Status
`BELUM` → isi `SELESAI` / `PARSIAL` / `BLOCKED` (juga di frontmatter).

## Risiko tersisa
JS awal lebih berat sekitar 94 KB gzip (React + router). Belum di-deploy: perlu persetujuan user (push, PR, merge, Vercel). Konsol di host terpisah (D-45) memakai build yang sama; dicek di production setelah deploy.

## Bukti
- Commit: jitsuinfi-frontend branch `hans/fe-react` (`f9da69b` … `19450a2`)
- ID tes: U-HNK-31.1, U-HNK-31.2, I-HNK-31.1, I-HNK-31.2, I-HNK-31.3 (PASS)
- Persetujuan user untuk push/deploy: _belum_
