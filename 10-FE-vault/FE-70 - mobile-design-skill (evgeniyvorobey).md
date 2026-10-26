---
tags: [fe-tool, "FE-70", mobile]
type: fe-tool
id: FE-70
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-70 - mobile-design-skill (evgeniyvorobey)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

Skill desain mobile versi 2.4.0: mulai dari tugas, bukan layout (momen + 1 – 3 tugas; tindakan di tempat informasi ditampilkan; tampilkan jawaban, bukan inputnya; desain momen puncak), putuskan semuanya, lantai (state kosong/loading/error/offline, 44 pt / 48 dp, kontras 4,5:1, teks sampai 200 %), fakta platform 2025 – 2026 di `skill/platform.md`, katalog pola di `docs/patterns-catalog.md` dan `docs/adaptive-layout.md`.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/evgeniyvorobey/mobile-design-skill (skill kanonik di akar repo) |
| Commit | `0c0ce131267ccb23d70fd9b2a1a5e80ccd97f804` |
| Lisensi | MIT |
| Isi | `SKILL.md` (9,2 KB), `skill/platform.md`, `skill/metadata.yaml`, `docs/` (34 file, tanpa `docs/proposals/`), `LICENSE`; 39 file, 496 KB |
| Lokasi | `~/.claude/skills/mobile-design-skill` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Kuat untuk merancang dan mereview satu layar atau alur. Aturan "show the answer, not its inputs" dipakai di DS-MOB (angka hasil di layar 1, bahan perhitungan di balik tap).

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

Dipasang **sebagian**: hanya teks. Yang **tidak** disalin: `scripts/` (alat rilis maintainer: `install.sh` memakai `rm -rf` pada folder target saat uninstall; `validate_release.py` dan `run_rubric_judge.py` memanggil `subprocess`), `.github/`, `examples/`, `agents/`, `CHANGELOG.md`, `docs/proposals/` (catatan pengembangan 420 KB). SKILL.md tidak pernah meminta menjalankan script. Wrapper `.claude/skills/mobile-design-skill/` di repo memakai path `../../../` yang hanya jalan di dalam clone, jadi yang dipasang adalah SKILL.md kanonik dari akar.

## Tumpang tindih
Tumpang tindih dengan FE-69 (proses) dan FE-71 (konvensi platform).

## Catatan
`docs/judged-mode.md` menyebut agent juri `mobile-design-judge`; agent itu tidak dipasang.

## Terpasang
- Lokasi: `~/.claude/skills/mobile-design-skill/` (tanpa `.git`)
- Commit: `0c0ce131267ccb23d70fd9b2a1a5e80ccd97f804` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
