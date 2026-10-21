---
tags: [fe-tool, mandate, "FE-M0"]
type: fe-mandate
id: FE-M0
status: AKTIF
updated: 2026-10-20
---

# FE-M0 - Mandat FE

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[Landing Page - Brief]] · [[FE-29 - PortoWeb Benchmark|PortoWeb]] · [[DS-00 - Peta Visual Design|Peta visual]]

Mandat user untuk frontend JitsuinFi, terutama landing page (HNK-18.T4). Diulang di vault ini (2026-10-20) supaya setiap keputusan FE bisa dicek terhadapnya. Sumber pertama: [[Landing Page - Brief]].

## Teks mandat (kata-kata user)
> buat selevel dengan landing page ini (selevel brati sma bagusnya dan kerennya dan immersivenya dan motionfullnya, bukan berarti km tiru plek ketiplek FEnya) : /Users/Shenhan/HansProject/PortoWeb
> Km harus temukan esensi dari JitsuinFi dan brainstorm visual yg anti mainstream, buat kayak sebuah visualisasi dan imajinasi yg benar" beda, liar sedikit tidak apa biar out of the box tp tetap user friendly yak. Visual landing page harus 65%, caption maksimal 35%. Visual hrs benar" immersive, motionfull dan bukan sekedar object card" kotak karena saya tidak suka itu jadi hindari, buat UI atau visual yg benar" relevan dan inklusif benar" merepresentasikan apa yg mau kita sampaikan dan mendukung informasi caption, bukan sekedar tempel dan placing kayak Ui card kotak" yg biasanya km pakai sebagai textbox gitu, itu larangan keras. Gunakan seluruh mcp yg ada untuk memaksimalkannya dan tools" ini :
>
> https://github.com/AThevon/genjutsu
> reactbits : npx shadcn@latest mcp init --client claude
> https://reactbits.dev/get-started/introduction
> https://animejs.com/documentation
> https://animejs.com/
>
> http://github.com/lucasmarkes/hairline
> https://github.com/Tejashmakwana/motionmaxxing
> https://github.com/motiondivision/motion

## Aturan yang bisa dicek
| ID | Aturan | Cara mengecek | Status landing sekarang (2026-10-20) |
|---|---|---|---|
| M1 | **Level** sama dengan PortoWeb (bagus, keren, imersif, penuh gerak), bukan tiruan | Bandingkan dengan teknik di [[FE-29 - PortoWeb Benchmark]]: satu karya WebGL khas, satu momen intro, scroll sebagai cerita, pointer yang direspons, token gerak, performa, reduced motion | Sebagian besar ada (diorama three.js, Lenis, token motionmaxxing, reduced motion); belum ada penilaian berdampingan |
| M2 | **Esensi JitsuinFi** jadi metafora visual anti-mainstream, sedikit liar, tetap ramah pengguna | Satu kalimat tesis visual yang hanya cocok untuk JitsuinFi; uji "apakah ini bisa jadi landing produk lain?" | Tesis di `MASTER.md` (kertas washi, segel jitsuin, kota piutang); belum diuji pengguna |
| M3 | **Visual 65%, caption maksimal 35%** | Per adegan, di 1440×900 dan 375×812: luas kotak teks (`getBoundingClientRect` node teks) dibagi luas viewport ≤ 35% | Audit app 2026-10-21: semua layar app 0% visual (gagal). `#/try` setelah HNK-30.T13: visual 76% / caption 24% (1440×900), 79% / 21% (375×812), diukur sebagai luas elemen visual dibanding luas glyph teks di luar visual. Layar lain: HNK-30.T14 – T17 |
| M4 | **Imersif dan penuh gerak** | Setiap bab punya gerak yang menceritakan sesuatu (bukan fade-up seragam); ada interaksi pointer atau scroll | Ada per bab; belum diaudit dengan `design-audit` genjutsu atau `/impeccable critique` |
| M5 | **Larangan keras: kartu kotak sebagai wadah teks** | Tidak ada elemen ber-latar + border/radius yang membungkus paragraf; informasi diset di atas kertas atau di dalam adegan | `MASTER.md` melarang kartu; belum diaudit visual. **App (D-36, D-37, 2026-10-20)**: gaya iOS dari `09-Design` dengan palet DS-PAL; panel mengelompokkan isian dan data, paragraf tidak pernah dalam kotak; verdict cap hanko (jitsuinfi-frontend `ba9383a`, PR #8) |
| M6 | Visual **relevan, inklusif, mewakili pesan, mendukung caption** | Setiap visual menjawab "informasi apa yang ia jelaskan?"; teks alternatif; kontras; tidak bergantung warna saja | Belum diaudit (a11y: `/impeccable audit`) |
| M7 | **Pakai semua MCP dan tool** yang ada | Tabel di bawah | Sebagian |
| M8 | Batas proyek (bukan dari mandat, tetap mengikat) | [[FE-01 - Batasan Platform FE]]: CSP same-origin, tanpa CDN, izin dependensi | Berlaku |

## M7: tool di mandat vs status
| Tool | Status di JitsuinFi | Catatan |
|---|---|---|
| genjutsu | Dipakai (pipeline paint untuk landing) | [[FE-13 - genjutsu]] |
| React Bits (shadcn MCP) | **Belum**; React tidak ada di JitsuinFi | Jalan tanpa React: port shader WebGL2 React Bits ke vanilla ([[FE-25 - React Bits shadcn MCP]]) |
| anime.js | Dipakai (7 file landing) | [[FE-08 - anime.js]] |
| hairline | **Terpasang, belum dipakai** | Figur relevan: vault, relay, settle, branches, loupe, exploded ([[FE-11 - hairline]]) |
| motionmaxxing | Dipakai sebagai sumber ease | [[FE-26 - motionmaxxing]] |
| Motion | Dipakai (`inView`, `hover`, `press`) | [[FE-09 - Motion]] |
| MotionSites | Dipakai (prompt 1 – 4 untuk hero) | [[FE-20 - MotionSites]] |
| Motion.so | Dicoba, hasil ditolak | [[FE-23 - Motion.so]] |
| Mobbin, ScreensDesign, Refero | **Belum dipakai untuk landing** | [[FE-18 - Mobbin]], [[FE-19 - ScreensDesign]], [[FE-21 - Refero]] |
| impeccable, frontend-design | **Baru dipasang**, belum dipakai | [[FE-14 - impeccable]], [[FE-28 - frontend-design]] |

## Cara memakai mandat ini
1. Sebelum desain baru: baca mandat + [[DS-PAL - Palet Utama JitsuinFi]] + `MASTER.md`.
2. Riset referensi dengan MCP (Refero, Mobbin, MotionSites), catat sebagai `DS-xx` di `09-Design`.
3. Tesis visual dan rencana token (genjutsu paint, frontend-design), uji terhadap M2 dan "tell" desain AI.
4. Bangun dengan library di [[FE-00 - Peta Tools FE]]; tanpa kartu kotak (M5).
5. Ukur M3 (rasio 65/35) dan audit M4 – M6 sebelum minta push.
