---
tags: [ac, "HNK-21"]
type: ac
id: HNK-21
phase: F5
lead: Dex
owners: [Dex, Dave]
status: TODO
updated: 2026-10-19
---

# AC-HNK-21 - Polish halaman internal web app

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-21 - Polish halaman internal web app|Test]] · [[ES-HNK-21 - Polish halaman internal web app|Exec Summary]]

**Lead:** Dex #dex · **Tim:** Dex #dex, Dave #dave (T9) · Dipindah dari Hans 2026-10-20 (D-29, DEV-12)

**Item:** HNK-21 · **Fase:** F5 · **Dependency:** HNK-10, HNK-18.T4

## Deskripsi
Halaman internal web app (`app.html`: shell dan beranda, supplier, buyer, financier, verify, orang luar) dipoles 100% ke tingkat landing: bahasa visual yang sama (kertas siang, segel 実印, ink line, motion token MASTER), tanpa UI kartu kotak sebagai wadah informasi, toggle EN/中文, dan layak dipakai di HP. Fungsi dan panggilan jitsuin-wasm tidak berubah; ini lapisan tampilan dan pengalaman.

Dicatat 2026-10-19 atas permintaan user ("page internal itu jelas perlu kita polish 100%+++ ... catat planning ini ke vault sebagai backlog saya dulu, nanti kita kerjakan"). Dikerjakan setelah backlog terbuka yang sudah ada.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-21.1 | Keenam halaman memakai token dan komponen landing (`tokens.css`, segel, tombol `seal-btn`, `ink-link`); tidak ada kartu kotak sebagai wadah informasi. | TODO | — | — |
| AC-HNK-21.2 | Semua teks halaman internal lewat `i18n.ts`; toggle EN/中文 di shell, pilihan sama dengan landing (localStorage `jitsuinfi.lang`). | TODO | — | — |
| AC-HNK-21.3 | Tiap halaman lolos 390×844 tanpa scroll horizontal dan 1440×900; reduced motion menampilkan keadaan akhir. | TODO | — | — |
| AC-HNK-21.4 | Alur fungsional tidak berubah: siklus supplier → buyer → financier → verify dengan kunci uji TES- tetap lulus seperti sebelum polish (perbandingan output wasm). | TODO | — | — |
| AC-HNK-21.5 | Fokus keyboard terlihat, label aria lengkap, kontras teks ≥ 4,5:1. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
