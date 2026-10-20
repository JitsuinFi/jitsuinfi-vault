---
tags: [fe-tool, "FE-26"]
type: fe-tool
id: FE-26
layer: skill-referensi
status: REFERENSI-DIPAKAI
updated: 2026-10-20
---

# FE-26 - motionmaxxing

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Skill agent untuk motion graphics ("looksmaxxing for motion graphics"). Belum terpasang, tetapi kurva ease-nya sudah dipakai di landing.

## Akar
| | |
|---|---|
| Repo | https://github.com/Tejashmakwana/motionmaxxing, lisensi Apache-2.0 |
| Isi repo | `SKILL.md`, `install.sh`, `library/`, `references/`, `runtime/`, `taste/`, `templates/`, `studies/`, `examples/`, `docs/` |
| Asal permintaan | [[Landing Page - Brief]] |
| Terpasang | **Tidak** (tidak ada di `~/.claude/skills`, `~/.agents/skills`, atau `.claude/skills`) |

## Yang sudah dipakai
- `jitsuinfi-frontend/src/landing/motion.ts`: "motionmaxxing's exact ease functions": softLand (expo-out k = 3.41), snapSettle (snap ramp w = 0.942, τ = 0.118), glide, softInOut, accelExit, popOver (pegas c = 2.67, ω = 4.36).
- `MASTER.md` §5 "Easings (motionmaxxing)": padanan `cubic-bezier` untuk CSS dan bentuk anime.js v4.

## Pilihan tindak lanjut
- Pasang sebagai skill (perlu izin) bila dibutuhkan untuk video demo atau gerak tambahan; isinya berorientasi video, bukan UI web.

## Status
REFERENSI (nilai disalin), BELUM TERPASANG.
