---
tags: [fe-tool, "FE-64", mobile]
type: fe-tool
id: FE-64
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-64 - mobile-native (Emil Kowalski)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

Skill perbaikan lapisan platform supaya web terasa terpasang di HP: hover yang lengket, kilatan tap, bug `100vh` (pakai `dvh`/`svh`), input yang membuat zoom (font input ≥ 16 px), tap lambat (`touch-action: manipulation`, umpan balik di `:active`), pull-to-refresh (`overscroll-behavior`), notch (`viewport-fit=cover` + `env(safe-area-inset-*)`), long-press memilih teks tombol, carousel, `theme-color` per skema, dan uji di perangkat asli.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/emilkowalski/skills (`skills/mobile-native`) |
| Commit | `2d228630ba1446365f614a108cb8252f1feda202` |
| Lisensi | MIT |
| Isi | 1 file (`SKILL.md`, 16,8 KB) + `LICENSE` |
| Lokasi | `~/.claude/skills/mobile-native` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Paling langsung berguna untuk JitsuinFi: semuanya CSS dan meta, tanpa dependensi, cocok dengan [[FE-01 - Batasan Platform FE|FE-01]]. `index.html` app sudah punya `viewport-fit=cover`; `theme-color`, `interactive-widget=resizes-content`, dan gate `(hover: hover) and (pointer: fine)` belum dicek.

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

Hanya teks. Tidak ada script. Skill lain di repo yang sama (`improve-animations`, `break-ui`) memuat karakter Unicode tersembunyi; keduanya **tidak** dipasang.

## Tumpang tindih
Sebagian tumpang tindih dengan FE-68 (target sentuh, hover) dan FE-71 (font 16 px). Hanya skill ini yang membahas meta PWA dan `dvh`.

## Catatan
Saat dipanggil tanpa pertanyaan, skill hanya menjawab satu kalimat pembuka; beri pertanyaan konkret.

## Terpasang
- Lokasi: `~/.claude/skills/mobile-native/` (tanpa `.git`)
- Commit: `2d228630ba1446365f614a108cb8252f1feda202` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
