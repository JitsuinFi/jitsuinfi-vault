---
tags: [fe-tool, "FE-49", monad-blitz]
type: fe-tool
id: FE-49
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-23
---

# FE-49 - Anatomy

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Mesin isometrik detail (ratusan part), shading 4 nada, urutan cat benar, audit geometri; SVG, opsional WebGL dan 3D; HTML atau React.

## Akar
| | |
|---|---|
| Jenis | Skill |
| Sumber | https://github.com/wheresryan22/anatomy |
| Pasang | `npx skills add wheresryan22/anatomy -g -a claude-code` atau `git clone` ke `~/.claude/skills/anatomy` |
| Bobot | Install ~10 MB; butuh Node ≥ 20.10 dan Chrome untuk cek; tanpa key |
| Lisensi | MIT |
| Lokasi | `~/.claude/skills/anatomy` (scope user, ikut tersedia di sesi JitsuinFi) |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-29 (2026-10-23) |
| Vonis di Monad Blitz | **DIPAKAI**; dipakai di: Figur utama mesin fotokopi di `/layar` |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: Mode SVG tanpa dependensi runtime; mode WebGL menambah shader. Script cek memakai Chrome headless lokal (bukan bagian bundle).

## Catatan
19.001★, push terakhir 2026-10-18 (GitHub API dicek 2026-10-22). Salah satu induk colorfigures. Script memakai `node:child_process` dan membuka Chrome lewat port DevTools; review dulu. Untuk HP: mode SVG saja, batasi jumlah part.

## Review keamanan (2026-10-22)
Commit `1482e84`, di-clone `--depth 1` (40 MB, 25 MB di antaranya `examples/`); tidak dipasang, tidak ada yang dijalankan. 61 file kode dipindai.

| Bagian | Temuan | Penilaian |
|---|---|---|
| `kit/` (masuk ke figur) | Geometri murni: tidak ada proses, jaringan, git, hapus file, atau `eval` | Aman |
| `scripts/capture.mjs`, `drive.mjs`, `lines.mjs`, `turn-check.mjs`, `print.mjs` | `spawn` Chrome headless dengan profil sementara (`mkdtempSync`), kendali lewat DevTools di `http://127.0.0.1`; `rmSync` hanya menghapus profil sementara itu; env hanya `CHROME_PATH`, `LOCALAPPDATA` | Aman, tapi menjalankan proses lokal |
| `scripts/publish.mjs` | Menyalin figur ke clone lokal galeri komunitas. `git push` + `gh` **hanya** dengan `--submit`, dan tetap bertanya dulu kecuali `--yes`. SKILL.md: dipakai "only when the user asks" | Aman bila tidak pernah diminta publish |
| `eval` / `new Function` | Tidak ada | Aman |
| Lisensi | MIT (Ryan, 2026) | Aman |

**Vonis: AMAN dengan catatan.** Jangan pernah meminta agent mem-publish ke galeri, dan jangan izinkan flag `--submit --yes`. Butuh Node ≥ 20.10 (ada: v26) dan Chrome untuk cek.

## Biaya waktu (dari SKILL.md)
| Ukuran | Part | Waktu |
|---|---|---|
| Figure | 40–80, maks. 1 layer WebGL | < 1 jam |
| Hero | 80–150 | 2–4 jam |
| Epic | Banyak sistem | ≥ 6 jam (skill menolak memulai tanpa persetujuan) |

Untuk hari H: hanya ukuran **Figure**, mode SVG tanpa WebGL di HP.

## Cara pakai untuk project
1. Pasang (setelah disetujui): `git clone` ke `~/.claude/skills/anatomy` atau `npx skills add wheresryan22/anatomy -g -a claude-code`.
2. Minta satu Figure: mesin fotokopi dengan lampu scan yang bergerak dan kertas keluar.
3. Build lewat script Node seperti `examples/dial-indicator/build.mjs`; untuk satu file SVG pakai `figureSvg({ standalone: "dark" })`.
4. Tempel SVG ke `/layar` sebagai figur utama; jangan muat WebGL di `/pesan`.

## Terpasang (2026-10-22)
- Lokasi: `~/.claude/skills/anatomy/` (27 MB, tanpa `.git`)
- Commit: `1482e8469b0a9e0d8cc18ea2740a01423d29ae80` (sama persis dengan yang direview; `diff -rq` kosong)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` / pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
