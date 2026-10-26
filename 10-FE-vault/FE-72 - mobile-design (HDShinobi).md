---
tags: [fe-tool, "FE-72", mobile]
type: fe-tool
id: FE-72
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-72 - mobile-design (HDShinobi)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

Desain mobile untuk aplikasi native (React Native, Flutter): psikologi sentuh dan Fitts, zona jempol, konvensi iOS/Android, performa list, navigasi tab/stack/drawer, tipografi dan warna mobile, checkpoint wajib sebelum kerja.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/HDShinobi/ai-agentic-kit (`plugins/aak-frontend/skills/mobile-design`), listing https://www.skillsdirectory.com/skills/hdshinobi-mobile-design (grade A) |
| Commit | `d10a862ce78e8eddb7b54723b61368ed341bc8c6` |
| Lisensi | MIT |
| Isi | `SKILL.md` (15,6 KB) + 12 file referensi + `scripts/mobile_audit.py` + `LICENSE`; 16 file, 248 KB |
| Lokasi | `~/.claude/skills/mobile-design` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Rendah untuk JitsuinFi: deskripsinya sendiri berkata **"NOT for web apps"**, dan sebagian besar isi (FlatList, `useNativeDriver`, SecureStore) khusus RN/Flutter. Bagian sentuh, zona jempol, dan navigasi tetap berguna sebagai bacaan.

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

`scripts/mobile_audit.py` dibaca: hanya `os.walk` + `open(...,'r')` lalu regex dan `print`; tidak ada proses, jaringan, git, hapus file, `eval`, atau akses kredensial; hanya memeriksa file RN/Flutter, jadi tidak berguna untuk kode web JitsuinFi. Frontmatter `allowed-tools: Read, Glob, Grep, Bash`. SKILL.md menyuruh "execute, don't read" script itu; abaikan untuk proyek ini.

## Tumpang tindih
Tumpang tindih dengan FE-68 dan FE-71.

## Catatan
Checkpoint "ask platform/framework" di skill tidak relevan: JitsuinFi adalah web app React + Vite.

## Terpasang
- Lokasi: `~/.claude/skills/mobile-design/` (tanpa `.git`)
- Commit: `d10a862ce78e8eddb7b54723b61368ed341bc8c6` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
