---
tags: [fe-tool, "FE-48", monad-blitz]
type: fe-tool
id: FE-48
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-23
---

# FE-48 - iso-figure

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Figur isometrik garis satu file HTML/SVG tanpa library; kernel proyeksi ~15 baris, tiap bagian bisa ditekan dan menghasilkan output nyata.

## Akar
| | |
|---|---|
| Jenis | Skill |
| Sumber | https://github.com/MrBongoC/ai-iso-skill |
| Pasang | `/plugin marketplace add MrBongoC/ai-iso-skill`, atau salin `skills/iso-figure` ke `~/.claude/skills` |
| Bobot | 1 SKILL.md, output SVG murni, tanpa key |
| Lisensi | MIT |
| Lokasi | `~/.claude/skills/iso-figure` (scope user, ikut tersedia di sesi JitsuinFi) |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-28 (2026-10-23) |
| Vonis di Monad Blitz | **DIPAKAI**; dipakai di: BLZ-16.T3, gaya dasar semua mesin |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: Output SVG murni tanpa library. Contoh di repo memuat Google Fonts: jangan dibawa (FE-01 tanpa CDN; pakai Fontsource FE-12).

## Catatan
Induk iso-glow dan colorfigures, karya Tolga Cohce. 281★, push terakhir 2026-10-04 (GitHub API dicek 2026-10-22). Paling ringan dan konsisten untuk banyak properti.

## Review keamanan (2026-10-22)
Commit `44b4da7`, di-clone `--depth 1` ke folder sementara; tidak dipasang, tidak ada yang dijalankan.

| Cek | Hasil |
|---|---|
| Isi skill | Satu file `skills/iso-figure/SKILL.md` (9.041 byte), hanya instruksi + kernel JS ~15 baris |
| Script / installer | Tidak ada. `.claude-plugin/plugin.json` dan `marketplace.json` hanya metadata |
| Jaringan | Tidak ada di skill. Contoh HTML memuat Google Fonts (`DM Mono`) |
| Aturan output | SKILL.md melarang script eksternal ("the file must run opened from disk") dan logo merek dagang |
| Lisensi | MIT (Tolga Cohce) |

**Vonis: AMAN.** Risiko tersisa hanya font dari Google Fonts di contoh; untuk demo offline, bundle font lokal.

## Cara pakai untuk project
1. Pasang (setelah disetujui): `/plugin marketplace add MrBongoC/ai-iso-skill`, atau salin `skills/iso-figure/` ke `~/.claude/skills/iso-figure/`.
2. Minta figur per mesin, mis. "iso-figure: mesin fotokopi, tombol COPY mengeluarkan kertas, readout jumlah lembar".
3. Ambil `<svg>` dan fungsi `render()` dari HTML hasil, jadikan komponen React di `/toko` dan `/layar`.
4. Pakai warna dari token CSS project (bukan hex bawaan); gaya dua abu-abu + satu warna `--live` cocok dengan aksen ungu Monad.
5. Aturan wajib dari skill: `vector-effect: non-scaling-stroke`, face berwarna opaque, urutan gambar belakang ke depan.

## Terpasang (2026-10-22)
- Lokasi: `~/.claude/skills/iso-figure/` (SKILL.md + LICENSE)
- Commit: `44b4da7714148eef547cc1b102e433472dfe3531` (sama persis dengan yang direview; `diff -rq` kosong)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` / pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
