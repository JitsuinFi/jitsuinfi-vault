---
tags: [fe-tool, "FE-65", mobile]
type: fe-tool
id: FE-65
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-65 - responsive-design (Mindrally)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

Panduan umum responsive web: mobile-first dengan `min-width`, Flexbox/Grid, container query, `clamp()`, `srcset`, breakpoint umum (320 – 1536 px), target sentuh 44 px, jangan matikan zoom.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/Mindrally/skills (`responsive-design`) |
| Commit | `7682ca77710e0971eab4e0ae5dddfa281aea0ba5` |
| Lisensi | Apache-2.0 |
| Isi | 1 file (`SKILL.md`, 5,2 KB) + `LICENSE` |
| Lokasi | `~/.claude/skills/responsive-design-mindrally` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Dasar saja; tidak ada aturan struktur layar (pane, navigasi, progressive disclosure). Breakpoint-nya berbasis perangkat, berbeda dengan 600/840 di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]; pakai DS-MOB.

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

Hanya teks. Tidak ada script.

## Tumpang tindih
Hampir duplikat FE-67 (flitzrrr). Nama `name:` di frontmatter diubah dari `responsive-design` ke `responsive-design-mindrally` agar tidak bentrok dengan FE-67 (satu-satunya perubahan lokal, tercatat di `.reviewed-commit`).

## Terpasang
- Lokasi: `~/.claude/skills/responsive-design-mindrally/` (tanpa `.git`)
- Commit: `7682ca77710e0971eab4e0ae5dddfa281aea0ba5` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
