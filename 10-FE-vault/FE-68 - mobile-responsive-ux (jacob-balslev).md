---
tags: [fe-tool, "FE-68", mobile]
type: fe-tool
id: FE-68
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-68 - mobile-responsive-ux (jacob-balslev)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

UX mobile untuk dashboard dan aplikasi operasional: HP = panel kendali saku, bukan desktop yang dipersempit. Hirarki kebutuhan mobile, target 44 × 44 CSS px, peta zona jempol, bottom nav 3 – 5 item dengan label, bottom sheet (peek 25 %, half 50 %, full 90 %), tabel → kartu 3 – 4 data, gestur selalu punya tombol, input mobile, KPI 2-up.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/jacob-balslev/skill-graph (`marketplace/skills/mobile-responsive-ux`) |
| Commit | `ee6f58e2f4adb9a9ac8fb43556e4c5f633a8361c` |
| Lisensi | Apache-2.0 (repo); frontmatter skill menulis MIT |
| Isi | 1 file (`SKILL.md`, 20,2 KB) + `LICENSE` |
| Lokasi | `~/.claude/skills/mobile-responsive-ux` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Paling dekat dengan masalah JitsuinFi (layar operasional supplier, buyer, financier, konsol). Sumber utama aturan tabel → ringkasan dan progressive disclosure di DS-MOB.

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

Hanya teks. Tidak ada script. Frontmatter memuat `allowed-tools: Read Grep Bash`, jadi saat skill aktif agent boleh memakai Bash tanpa tanya; SKILL.md tidak meminta menjalankan perintah apa pun.

## Tumpang tindih
Tumpang tindih dengan FE-71 (zona jempol, bottom nav) dan FE-72 (target sentuh).

## Catatan
Kata "View on desktop" untuk eksplorasi data penuh tidak cocok untuk PWA JitsuinFi; di DS-MOB detail tetap bisa dibuka di HP, satu tap lebih dalam.

## Terpasang
- Lokasi: `~/.claude/skills/mobile-responsive-ux/` (tanpa `.git`)
- Commit: `ee6f58e2f4adb9a9ac8fb43556e4c5f633a8361c` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
