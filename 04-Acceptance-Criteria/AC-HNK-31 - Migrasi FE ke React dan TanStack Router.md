---
tags: [ac, "HNK-31"]
type: ac
id: HNK-31
phase: F6
status: TODO
updated: 2026-10-22
---

# AC-HNK-31 - Migrasi FE ke React dan TanStack Router

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-31 - Migrasi FE ke React dan TanStack Router|Test]] · [[ES-HNK-31 - Migrasi FE ke React dan TanStack Router|Exec Summary]]

**Item:** HNK-31 · **Fase:** F6 · **Dependency:** HNK-21, HNK-30 · **Keputusan:** D-52 · **Patokan visual:** `05-Testing/assets/hnk31-baseline/` (tangkapan layar main `155eaf7`)

## Deskripsi
Web app (landing, app, konsol financier) dipindah dari TypeScript tanpa framework (helper `h()`, tiga entri HTML, routing hash) ke **React + TanStack Router** (SPA statis di atas Vite, route berbasis file, URL bersih). Alasan Next.js ditolak: script inline App Router melanggar CSP `script-src 'self'` (D-52). Logika `src/lib/*` dan test-nya tidak diubah. Migrasi satu halaman per task, berurutan, tidak paralel; tiap task ditutup dengan paritas visual terhadap patokan sebelum task berikutnya mulai.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-31.1 | **Paritas visual (KPI utama):** tiap halaman yang dimigrasi, di 1440 × 900 dan 390 × 844, sama dengan patokan `hnk31-baseline`: warna DS-PAL, tipografi (Shippori Mincho B1, Geist, Geist Mono), tata letak, animasi dan rasio visual 65/35 tidak berubah; perbedaan yang disengaja dicatat di Deviasi | TODO | — | — |
| AC-HNK-31.2 | **Paritas teks:** teks terlihat per halaman (`innerText`) sama dengan patokan, kecuali tautan yang berubah dari `#/x` ke `/x` | TODO | — | — |
| AC-HNK-31.3 | **CSP tetap ketat:** header Vercel tidak berubah (`script-src 'self' 'wasm-unsafe-eval'`, `style-src 'self'`, tanpa `'unsafe-inline'`); nol pelanggaran CSP dan nol error di console di semua route | TODO | — | — |
| AC-HNK-31.4 | **URL bersih + tautan lama tetap jalan:** `/`, `/app`, `/try`, `/supplier`, `/buyer`, `/member`, `/verify`, `/outsider`, `/index`, `/apply`, `/account`, `/console` (dan `/console/pair`); `app.html#/x` dan `#/x` diarahkan ke `/x`; host konsol (`jitsuinfi-console*.vercel.app`) membuka `/console` | TODO | — | — |
| AC-HNK-31.5 | **Tanpa regresi logika:** `npm test` (78 test) lulus, `tsc` bersih, build lulus; `src/lib/*` tidak berubah kecuali impor | TODO | — | — |
| AC-HNK-31.6 | **Alur fungsional utuh:** E2E lokal (relay + node + web app, testnet) menjalankan siklus supplier → buyer → konsol → advance → pelunasan QR → settled di FE baru, sama dengan FE lama (regresi HNK-21.T8) | TODO | — | — |
| AC-HNK-31.7 | **Ukuran dan performa:** JS awal per route ≤ patokan + 60 KB gzip (React + router); landing tetap 60 fps di desktop dan `prefers-reduced-motion` tetap dihormati | TODO | — | — |
| AC-HNK-31.8 | **Aksesibilitas dan responsif:** 390 px tanpa overflow horizontal, semua kontrol berlabel, fokus keyboard terlihat, sama dengan patokan HNK-21.T7 | TODO | — | — |
| AC-HNK-31.9 | **Bersih:** helper `h()`, `app.html`, `console.html` dan routing hash dihapus setelah semua halaman pindah; tidak ada komponen yang masih memakai adaptor halaman lama | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
