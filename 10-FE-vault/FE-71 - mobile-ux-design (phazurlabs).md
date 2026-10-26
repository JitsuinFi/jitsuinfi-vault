---
tags: [fe-tool, "FE-71", mobile]
type: fe-tool
id: FE-71
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-26
---

# FE-71 - mobile-ux-design (phazurlabs)

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-01 - Batasan Platform FE|Batasan platform]] · [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]]

Mobile-first (Wroblewski), satu aksi utama per layar, desain untuk interupsi, zona jempol (Hoober), target 44 pt / 48 dp + jarak 8 pt, konvensi iOS dan Material 3, tab bar maks. 5 dengan label, stack maks. 4 level, form satu kolom dengan label di atas dan keyboard yang tepat, pola reflow/reveal/collapse.

## Akar
| | |
|---|---|
| Jenis | Skill (agent, teks) |
| Sumber | https://github.com/phazurlabs/ux-ui-mastery (`skills/mobile-ux-design`) |
| Commit | `3a3693b02c0968ef2d299044119faef8f3a24624` |
| Lisensi | Apache-2.0 |
| Isi | `SKILL.md` (12,3 KB) + 4 referensi (`ios-android-patterns.md`, `mobile-form-navigation.md`, `ios26-liquid-glass-material3-expressive.md`, `wearable-iot-patterns.md`) + `LICENSE`; 172 KB |
| Lokasi | `~/.claude/skills/mobile-ux-design` (scope user) |
| Asal catatan | Daftar user `Notes/mobileResources.md` (2026-10-26) |

## Kecocokan dengan JitsuinFi
Sumber utama aturan navigasi dan form di DS-MOB. Referensi Liquid Glass dan Material 3 Expressive adalah gaya visual platform; **jangan** dipakai sebagai gaya JitsuinFi.

Aturan layout yang disarikan dari skill ini dan pedoman resmi ada di [[DS-MOB - Aturan Layout Mobile JitsuinFi|DS-MOB]].

## Review keamanan (2026-10-26)
Di-clone `--depth 1` ke folder sementara; tidak ada yang dijalankan; `npx skills add` tidak dipakai. SKILL.md dibaca utuh; semua file teks dipindai untuk perintah shell, instruksi tersembunyi, dan karakter Unicode tak terlihat.

Hanya teks. Tidak ada script. Menyebut skill lain dari kumpulan yang sama (`ui-visual-design-system`, `component-patterns-code`) yang tidak dipasang; rujukan itu diabaikan saja.

## Tumpang tindih
Tumpang tindih dengan FE-68 dan FE-72.

## Terpasang
- Lokasi: `~/.claude/skills/mobile-ux-design/` (tanpa `.git`)
- Commit: `3a3693b02c0968ef2d299044119faef8f3a24624` (sama dengan yang direview)
- Bukti asal: file `.reviewed-commit` di folder skill
- Update: jangan `git pull` atau pasang ulang tanpa review commit baru

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
