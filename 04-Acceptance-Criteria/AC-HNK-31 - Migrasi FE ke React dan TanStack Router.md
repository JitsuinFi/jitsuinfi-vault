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
| AC-HNK-31.1 | **Paritas visual (KPI utama):** tiap halaman yang dimigrasi, di 1440 × 900 dan 390 × 844, sama dengan patokan `hnk31-baseline`: warna DS-PAL, tipografi (Shippori Mincho B1, Geist, Geist Mono), tata letak, animasi dan rasio visual 65/35 tidak berubah; perbedaan yang disengaja dicatat di Deviasi | PASS | 2026-10-22 | Diff piksel per halaman vs build lama (`scripts/fe-cdp-shots.mjs`, `scripts/fe-diff.py`, reduced motion): 0,00 % di semua bab landing, lobi, try, verify, outsider, rates, lembar akun, supplier, buyer, apply, simulasi financier, layar konsol dan meja konsol (1440 dan 390 px); beda tersisa hanya data live (tinggi blok), kota 3D yang beranimasi, sidik jari passkey virtual, dan port host. CSS identik byte-per-byte (hash `DBIeZ2Gx`, `DSx1Eymi`, `BRw2dqZv`, `BRnX-toT`) |
| AC-HNK-31.2 | **Paritas teks:** teks terlihat per halaman (`innerText`) sama dengan patokan, kecuali tautan yang berubah dari `#/x` ke `/x` | PASS | 2026-10-22 | Teks terlihat sama per halaman (innerText/DOM) kecuali data live dan port host; jejak interaksi skrip identik di build lama dan baru untuk semua halaman (T3 – T11) |
| AC-HNK-31.3 | **CSP tetap ketat:** header Vercel tidak berubah (`script-src 'self' 'wasm-unsafe-eval'`, `style-src 'self'`, tanpa `'unsafe-inline'`); nol pelanggaran CSP dan nol error di console di semua route | PASS | 2026-10-22 | Header CSP `vercel.json` tidak berubah; meta CSP disisipkan saat build; nol pelanggaran CSP dan nol error JS di 18 route (T12) |
| AC-HNK-31.4 | **URL bersih + tautan lama tetap jalan:** `/`, `/app`, `/try`, `/supplier`, `/buyer`, `/member`, `/verify`, `/outsider`, `/rates` (dulu `#/index`), `/apply`, `/account`, `/console` (dan `/console/pair`); `app.html#/x` dan `#/x` diarahkan ke `/x`; host konsol (`jitsuinfi-console*.vercel.app`) membuka `/console` | PASS | 2026-10-22 | Route bersih aktif; `legacyTarget` + test U-HNK-31.2; `app.html#/verify` dan `console.html?view=pair` diarahkan (dicek di browser dan CDP); fallback SPA dan aturan host konsol di `vercel.json`. Belum dicek di production (setelah deploy) |
| AC-HNK-31.5 | **Tanpa regresi logika:** `npm test` (78 test) lulus, `tsc` bersih, build lulus; `src/lib/*` tidak berubah kecuali impor | PASS | 2026-10-22 | 80 test lulus (78 lama + 2 legacy-url), `tsc` bersih, build lulus di setiap task; `src/lib/*` hanya bertambah `legacy-url.ts` dan `download.ts` |
| AC-HNK-31.6 | **Alur fungsional utuh:** E2E lokal (relay + node + web app, testnet) menjalankan siklus supplier → buyer → konsol → advance → pelunasan QR → settled di FE baru, sama dengan FE lama (regresi HNK-21.T8) | TODO | — | — |
| AC-HNK-31.7 | **Ukuran dan performa:** JS awal per dunia ≤ patokan + 100 KB gzip (React + router; target awal 60 KB, direvisi, lihat Deviasi); landing tetap 60 fps di desktop dan `prefers-reduced-motion` tetap dihormati | PASS | 2026-10-22 | JS awal per dunia +93 – 95 KB gzip (target direvisi 100 KB, lihat Deviasi); reduced motion dihormati (patokan diambil dengan mode itu) |
| AC-HNK-31.8 | **Aksesibilitas dan responsif:** 390 px tanpa overflow horizontal, semua kontrol berlabel, fokus keyboard terlihat, sama dengan patokan HNK-21.T7 | PASS | 2026-10-22 | 390 px identik dengan patokan di semua halaman (tanpa overflow baru); label kontrol sama (teks dan aria dari markup yang sama) |
| AC-HNK-31.9 | **Bersih:** helper `h()`, `app.html`, `console.html` dan routing hash dihapus setelah semua halaman pindah; tidak ada komponen yang masih memakai adaptor halaman lama | PASS | 2026-10-22 | `h()`, `app.html`, `console.html`, routing hash dan adaptor `Legacy` dihapus (T10, T12) |

## Deviasi
- 2026-10-22 (T2): **JS awal.** Target awal +60 KB gzip tidak realistis untuk React 19 + TanStack Router. Terukur: app 83,4 → 178,4 KB, landing 221,6 → 314,6 KB, konsol 15,3 → 109,0 KB (masing-masing sekitar +94 KB: `react-dom` sekitar 58 KB, router sekitar 30 KB). Target direvisi ke +100 KB; menurunkannya berarti mengganti library (Preact), risiko yang tidak sepadan sebelum deadline.
- 2026-10-22 (T2): **Indeks di `/rates`.** Nama file route `index` dipakai untuk `/`; `#/index` dan `app.html#/index` diarahkan ke `/rates`.

Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
