---
tags: [fe-tool, "FE-13"]
type: fe-tool
id: FE-13
layer: skill
status: AKTIF
updated: 2026-10-20
---

# FE-13 - genjutsu

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Skill creative coding untuk antarmuka: gerak, micro-interaction, sistem visual, dan situs utuh oleh tim agent. Dipakai untuk landing JitsuinFi.

## Akar
| | |
|---|---|
| Versi | v4.1.1 |
| Sumber | https://genjutsu.athevon.dev (well-known), zip dari `github.com/AThevon/genjutsu/releases/download/v4.1.1/genjutsu.zip`, digest `sha256:2d74fddd…034f` |
| Dipasang | 2026-10-10 lewat `npx skills add` (tercatat di `~/.agents/.skill-lock.json`) |
| Lokasi | `~/.agents/skills/genjutsu/`, ditautkan ke `~/.claude/skills/genjutsu` (symlink), jadi aktif di semua proyek |
| Pemanggilan | `/genjutsu` (router), `/genjutsu:cast`, `/genjutsu:paint`, `/genjutsu:bunshin`, atau skill `genjutsu` |

## Tiga pipeline
| Pipeline | File | Untuk | Catatan |
|---|---|---|---|
| cast | `cast/GUIDE.md` | Memperhalus atau menganimasikan UI yang sudah ada | Default. Langkah: SCAN (deteksi stack) → DISCOVER → SCOPE → THESIS (satu kalimat) → LOAD sub-skill → bangun → Preview Gate |
| paint | `paint/GUIDE.md` | Identitas visual dari nol atau redesign penuh | Dipakai untuk landing (HNK-18.T4); ada jalur pendek "Light scope" |
| bunshin | `bunshin/GUIDE.md` | Situs utuh oleh tim subagent | Hanya bila diminta dengan nama; biaya jutaan token; user lebih suka tanpa banyak agent |

## Sub-skill `_jutsu/` (17)
| Modul | Isi |
|---|---|
| `motion-principles` | Dasar gerak: timing, easing, enter/exit, aksesibilitas, performa |
| `css-native` | Animasi tanpa dependensi: scroll-driven, View Transitions, `@starting-style` |
| `framer-motion` | Motion / Framer Motion (lihat [[FE-09 - Motion]]) |
| `gsap` | GSAP, timeline, ScrollTrigger (tidak dipakai; MASTER menolak GSAP Flip) |
| `threejs-r3f` | three.js dan React Three Fiber, shader, post-processing (lihat [[FE-07 - three.js]]) |
| `canvas-generative` | Seni generatif Canvas 2D |
| `ui-ux-pro-max` | Basis data desain: 84 gaya, 192 palet, 74 pasangan font, 25 chart, 99 pedoman UX untuk 22 stack; skrip Python `scripts/search.py`, `design_system.py`, `core.py`, `validate_data.py` |
| `design-audit` | Checklist audit: celah gerak, aksesibilitas, warna, responsif, performa (ada `scripts/`) |
| `tells` | Refleks model yang harus dihindari (data karangan, hiasan kosong, layout seragam, copy hampa) |
| `orchestration` | Menjalankan tim subagent untuk bunshin |
| `desktop-principles`, `mobile-principles` | Prinsip UX desktop dan mobile |
| `compose-motion`, `compose-graphics`, `compose-multiplatform` | Android / Jetpack Compose (di luar cakupan web) |
| `swiftui-motion`, `swiftui-graphics` | Apple / SwiftUI (di luar cakupan web) |
| `VERSIONS.md` | Tanggal verifikasi tiap klaim versi; tanda `VERIFY-NEEDED` |

## Dipakai di JitsuinFi
- Landing (HNK-18.T4) lewat pipeline paint: tesis visual dan interaksi, larangan, token warna dan gerak di `jitsuinfi-frontend/MASTER.md`.
- `MASTER.md` mencatat "Dials" yang dikirim ke `ui-ux-pro-max` (variance 8, motion 8, density 3), apa yang dipakai (pola storytelling scroll) dan yang dibuang (Bento grid, palet cyan, GSAP Flip, Noto Serif JP).

## Batasan
- Saran kode genjutsu bisa memakai CDN atau React; terjemahkan ke vanilla TS dan aset lokal ([[FE-01 - Batasan Platform FE]]).
- bunshin melanggar preferensi "tanpa banyak agent" kecuali user meminta.

## Cek cepat
```bash
ls ~/.agents/skills/genjutsu/_jutsu && cat ~/.agents/.skill-lock.json
```

## Status
AKTIF.
