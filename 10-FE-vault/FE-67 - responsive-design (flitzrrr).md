---
tags: [fe-tool, "FE-67", mobile]
type: fe-tool
id: FE-67
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-67 - responsive-design (flitzrrr)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

Mobile-first, breakpoint ditentukan konten (maks. 4 – 5), *content choreography* (urutan konten per viewport), jangan sembunyikan konten dengan `display:none` saja, jangan scroll horizontal, uji di 320 px, panjang baris 45 – 75 karakter, checklist.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/flitzrrr/frontend-design-skills (`skills-src/responsive-design`) |
| Commit | `d607ba305bf606605de9382609864a69ad92699b` |
| Lisensi | MIT |
| Isi | 1 file (`SKILL.md`, 7,0 KB) + `LICENSE` |
| Lokasi | `~/.claude/skills/responsive-design-flitzrrr` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Berguna untuk aturan "jangan memeras desktop" dan uji 320 px. Pola *card layout* dan hamburger di dalamnya **tidak** dipakai untuk app (lihat [[FE-M0 - Mandat FE|FE-M0]] M5 dan tab bar di DS-MOB).

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

Hanya teks. Tidak ada script. SKILL.md merujuk `references/fluid-grid.md` yang tidak ada di repo.

## Tumpang tindih
Hampir duplikat FE-65; frontmatter `name:` diubah ke `responsive-design-flitzrrr` agar tidak bentrok.

## Terpasang
- Lokasi: `~/.claude/skills/responsive-design-flitzrrr/` (tanpa `.git`)
- Commit: `d607ba305bf606605de9382609864a69ad92699b` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
