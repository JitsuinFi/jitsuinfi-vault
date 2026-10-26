---
tags: [fe-tool, "FE-69", mobile]
type: fe-tool
id: FE-69
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-69 - mobile-app-ui-design (ceorkm)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

Proses desain layar mobile: konteks, struktur dulu (aksi utama di sepertiga bawah, elemen MVP saja), lalu UI (maks. 4 ukuran font, 60/30/10, grid 8 pt, bayangan lembut), peak-end, pola pencarian dan status.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/ceorkm/mobile-app-ui-design (akar repo) |
| Commit | `4c67a0e71727b6afaaafbcbb1b11c7660de5fac9` |
| Lisensi | **Tidak ada file LICENSE** di repo |
| Isi | `SKILL.md` (8 KB), `references/industry-conventions.md`, `README.md`, `INDEX.md` |
| Lokasi | `~/.claude/skills/mobile-app-ui-design` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Pakai **hanya bagian struktur** (Step 1 – 2, anti-pattern). Bagian gaya visual (Tailwind, Lucide, Recharts, `rounded-2xl`, glassmorphism, 60/30/10) bertentangan dengan sistem visual JitsuinFi ([[DS-PAL - Palet Utama JitsuinFi|DS-PAL]], `MASTER.md`, M5 tanpa kartu) dan [[FE-01 - Batasan Platform FE|FE-01]].

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

Hanya teks. Tidak ada script. Tanpa lisensi berarti hak cipta penuh pada penulis; dipakai sebagai bacaan agent lokal saja, jangan salin isinya ke repo atau publikasi.

## Tumpang tindih
Tumpang tindih dengan FE-70 (proses desain).

## Terpasang
- Lokasi: `~/.claude/skills/mobile-app-ui-design/` (tanpa `.git`)
- Commit: `4c67a0e71727b6afaaafbcbb1b11c7660de5fac9` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
