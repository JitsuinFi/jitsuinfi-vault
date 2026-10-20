---
tags: [fe-tool, "FE-29"]
type: fe-tool
id: FE-29
layer: benchmark
status: REFERENSI
updated: 2026-10-20
---

# FE-29 - PortoWeb Benchmark

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[FE-M0 - Mandat FE|Mandat FE]] · [[10 - FE Vault|Hub modul]]

Landing portofolio Hans di `/Users/Shenhan/HansProject/PortoWeb`: **tolok ukur level** landing JitsuinFi menurut mandat ("selevel, bukan tiru plek ketiplek"). Folder ini sumber eksternal: dirujuk, tidak diubah.

## Akar
| | |
|---|---|
| Lokasi | `PortoWeb/Hans_Porto_Web` (aplikasi), `PortoWeb/_resources` (riset), `PortoWeb/.mcp.json` |
| Repo | `Shenhan01-sys/...` (PR #3 – #6 sudah di-merge; terakhir `3f47e4a`, makalah dan sertifikat ICIC 2026) |
| Stack | React 18.3 + Vite 5.4 + TypeScript 5.6 + Tailwind 3.4 + `framer-motion` 11 + `animejs` 4.5.0 + `lenis` 1.3.26 + `@lucasmarkes/hairline` 0.5.1; server Express (chatbot Groq/Gemini, MCP portofolio) |
| Sistem desain | `Hans_Porto_Web/MASTER.md` ("single source of truth", palet violet), sama polanya dengan `jitsuinfi-frontend/MASTER.md` |
| Target kualitas PortoWeb sendiri | codapress.co.uk; visual 65% / caption 35% (`_resources/README.md`) |

## Teknik yang membuatnya "selevel"
| Teknik | File | Inti |
|---|---|---|
| Medan dither WebGL2 di hero | `client/src/components/fx/dither-field.tsx`, `lib/dither.ts` | Plasma terwarp, dither berurutan ke ramp 11 tingkat; 30 fps idle, 60 fps saat pointer mendorong; berhenti di luar layar, tab tersembunyi, reduced motion |
| Intro tile-wipe setiap muat | `fx/intro.tsx` | Dua lapis tile mengecil diagonal (softLand); bisa dilewati dengan tombol, klik, atau scroll |
| Kursor dua kotak | `fx/cursor.tsx` | Kotak besar membesar di atas link, berganti nama aksi (`view`, `drag`, `open`); hanya mouse dan trackpad |
| Reveal gambar dalam masker | `fx/reveal.tsx` | Masker membuka 800 ms, gambar turun dari 1.1× 1000 ms, sekali di 90% viewport |
| Label scramble, efek teks | `site/scramble-label.tsx`, `fx/text.tsx` | Judul ter-decode huruf demi huruf |
| Smooth scroll | `fx/smooth-scroll.tsx` | Lenis |
| Figur hairline | `fx/hairline.tsx` | Import vanilla per figur, dimuat dekat viewport |
| Token gerak | `lib/motion.ts` | Cermin MASTER §5 (ease motionmaxxing) |

## Basis pengetahuan FE di `PortoWeb/_resources/notes/`
| Catatan | Isi | Dipakai di vault ini |
|---|---|---|
| `site-teardown.md` | Bongkar codapress.co.uk dan agenticwebteam.com: dither plasma WebGL2 (GLSL verbatim), intro, reveal teks, carousel busur, kursor, scramble, transisi halaman, 15 teknik berperingkat | Inspirasi teknik, FE-29 |
| `reactbits-catalog.md` | 218 komponen React Bits (TS-TW): dependensi, bobot, isu Tailwind 3, shortlist | [[FE-25 - React Bits shadcn MCP]] |
| `animejs-v4.md` | Digest API anime.js 4.5.0 dicek ke source | [[FE-08 - anime.js]] |
| `motionmaxxing-web-rules.md` | 12 ease persis, statistik waktu, slop tell, token gerak web | [[FE-26 - motionmaxxing]] |
| `hairline.md` | API, 33 figur, tema, ukuran bundle | [[FE-11 - hairline]] |
| `mobbin-patterns.md` | Pola Mobbin per bagian portofolio (hero, timeline, kontak, aksesibilitas gelap) | Pola timeline dan aksesibilitas |
| `profile-brief.md`, `new-projects.md` | Isi portofolio | Tidak relevan untuk JitsuinFi |

Klon tool di `PortoWeb/_resources/repos/`: genjutsu (`1f518a7`), hairline (`37d2e78`), motionmaxxing (`8c8ec0f`), react-bits (`310fc73`), anime (`01b81be`). `_resources/sites/` berisi HTML/CSS/JS situs referensi yang diunduh: **tidak tepercaya, hanya dibaca, jangan dijalankan**.

## Yang dipinjam vs yang tidak
| Dipinjam (level) | Tidak dipinjam (identitas) |
|---|---|
| Satu karya WebGL khas di hero dengan aturan performa yang sama | Palet violet, dither, kursor dua kotak |
| Satu momen intro, scroll sebagai alur cerita | Komponen React, Tailwind, framer-motion |
| Token gerak dari motionmaxxing, satu MASTER sebagai sumber tunggal | Isi portofolio |
| Reduced motion menampilkan keadaan akhir | Server chatbot |

## Status
REFERENSI.
