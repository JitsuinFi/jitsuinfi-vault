---
tags: [ac, "HNK-33"]
type: ac
id: HNK-33
phase: F6
status: TODO
updated: 2026-10-25
---

# AC-HNK-33 - Rombak landing dengan figur Anatomy

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-33 - Rombak landing dengan figur Anatomy|Test]] · [[ES-HNK-33 - Rombak landing dengan figur Anatomy|Exec Summary]]

**Item:** HNK-33 · **Fase:** F6 · **Dependency:** HNK-18, HNK-31 · **Rujukan:** [[FE-49 - Anatomy|FE-49]], [[DS-PAL - Palet Utama JitsuinFi|DS-PAL]], [[FE-01 - Batasan Platform FE|FE-01]]

## Deskripsi
Bab 2 – 6 landing mendapat figur isometrik interaktif gaya Anatomy: benda fisik yang menceritakan bab itu, bagian yang ditekan menghasilkan keluaran nyata. Hero (kota 3D) tetap, hanya dirapikan. Copy dan terjemahan EN/中文 setiap bab tetap.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti.

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-33.1 | **Figur per bab:** bab 2 – 6 masing-masing punya satu figur Anatomy interaktif dengan keluaran nyata (N dari wasm, urutan segel, Exhibit A, riwayat) | TODO | — | — |
| AC-HNK-33.2 | **Palet dan tipe:** hanya warna DS-PAL, tanpa `#000`/`#FFF`; Shippori Mincho B1 dan Geist dari Fontsource; visual 65 % / caption 35 %; tanpa UI kartu kotak | TODO | — | — |
| AC-HNK-33.3 | **CSP ketat:** nol pelanggaran CSP dan nol error console; tanpa CDN, tanpa script atau atribut `style` inline | TODO | — | — |
| AC-HNK-33.4 | **Responsif dan aksesibel:** rapi di 390 px dan 1440 px; `prefers-reduced-motion` dihormati; bisa dipakai dengan keyboard; label EN/中文 | TODO | — | — |
| AC-HNK-33.5 | **Hero:** kota 3D dan copy sama, jarak dan perataan lebih rapi, disetujui user | TODO | — | — |
| AC-HNK-33.6 | **Persetujuan per bab:** tiap bab ditunjukkan ke user dan disetujui sebelum bab berikutnya; deploy setelah persetujuan | TODO | — | — |
