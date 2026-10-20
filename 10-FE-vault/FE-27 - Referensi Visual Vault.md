---
tags: [fe-tool, "FE-27"]
type: fe-tool
id: FE-27
layer: referensi
status: REFERENSI
updated: 2026-10-20
---

# FE-27 - Referensi Visual Vault

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Bahan referensi visual yang disimpan di vault (di luar `09-Design`).

## `MotionSites-References/`
| File | Isi | Stack yang diminta prompt | Yang diambil `MASTER.md` |
|---|---|---|---|
| `prompt1.md` | Hero sinematik layar penuh, video latar, mask blur bawah | React, Tailwind, Lucide, Inter (Google Fonts), video CloudFront | Mask blur bawah (diwarnai pool), pill liquid-glass |
| `prompt2.md` | Hero dengan video latar berulang | Fustat, Inter, video CloudFront | Tidak ada yang disebut eksplisit |
| `prompt3.md` | Hero aplikasi password manager "VaultShield" | React, TypeScript, Tailwind, Framer Motion, Lucide, Inter | Tanda segel di dalam judul |
| `Prompt4.rtf` | Landing agensi gelap, liquid glass, dua section | React, Vite, TypeScript, Tailwind | Judul blur-in per kata dengan jeda acak, pill liquid-glass |

Tambahan dari referensi lain (Reeve): tombol utama magnetik. Ditolak: kartu dan kotak statistik, Inter/Barlow/Fustat, hitam pekat, CTA putih di atas hitam, video dari CDN ([[FE-01 - Batasan Platform FE]]). Sumber prompt: [[FE-20 - MotionSites]].

## `ColorPalette-JitsuinFi/`
- Dua gambar palet (`870121ac….jpg`, `ffc1eb9c….jpg`).
- Diterjemahkan ke token di `jitsuinfi-frontend/MASTER.md` §2 (Cetacean Blue, Catalina Blue, Absolute Zero, Button Blue, Dark Raspberry, Brown Coffee, Japanese Violet, Classic Rose, Pearly Purple, Vodka) dengan rasio kontras WCAG. Catatan MASTER: label chart Vodka `29B4D1` salah; nilai benar RGB 196,199,242.

## Status di git
- Kedua folder **belum di-commit** ke repo vault (untracked). Putuskan: commit, atau pindahkan ke `09-Design`.

## Status
REFERENSI.
