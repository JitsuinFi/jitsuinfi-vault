---
tags: [project, landing, brief]
---

# Landing Page - Brief

**Bagian dari:** [[00 - Project]] · Kembali: [[START-HERE]] · Item: HNK-18.T4 di [[Backlog]] · Terkait: [[JitsuinFi - Ringkasan Proyek]] · [[Desain Jitsuin Seal]]

> Panduan wajib untuk landing page JitsuinFi. Prompt user dicatat **verbatim** (2026-10-19); setiap keputusan desain landing page harus bisa dicek terhadap prompt ini.

## Prompt user (verbatim)

> Nah yauda kalau begitu tolong handle landing page ya, buat selevel dengan landing page ini (selevel brati sma bagusnya dan kerennya dan immersivenya dan motionfullnya, bukan berarti km tiru plek ketiplek FEnya) : /Users/Shenhan/HansProject/PortoWeb
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

Konfirmasi user atas pemahaman awal (2026-10-19): "Gasssss, itu oke, dan pastikan sesuai dengan prompt saya".

## Aturan turunan (checklist)
- [ ] Setara kualitas PortoWeb (`/Users/Shenhan/HansProject/PortoWeb`) dalam kebagusan, imersi, dan gerak; **tidak menyalin** FE-nya.
- [ ] Esensi JitsuinFi ditemukan dan dijadikan satu metafora visual yang anti-mainstream, sedikit liar, tetap ramah pengguna.
- [ ] Rasio **visual 65% / caption maksimal 35%**.
- [ ] Visual imersif dan penuh gerak; **larangan keras: kartu kotak / textbox UI** sebagai wadah informasi.
- [ ] Visual relevan, inklusif, mewakili pesan, dan **mendukung** caption (bukan tempelan).
- [ ] Memakai MCP yang ada dan tools: genjutsu, React Bits (shadcn MCP), anime.js, hairline, motionmaxxing, Motion.
- [ ] Batas teknis proyek: CSP same-origin, tanpa CDN (semua aset dibundel), lokal dulu (D-25).

## Progres per bab

| Bab | Isi | Status | Tanggal | Bukti |
|---|---|---|---|---|
| 1. Hero | Kertas dokumen WebGL2 dengan sobekan ke kolam terlindung (simulasi riak height field, sentuhan pointer, napas ambient 30fps, berhenti di luar layar). Invoice uji `TES-INV-0007` dengan tepi sobek; jitsuin 実印 turun (snapSettle 367ms, squash 67ms, angkat accelExit 433ms), tinta meresap 1,2 dtk; sidik jari N asli (`8ee58d12…dc8354`, dari jitsuin-wasm via `scripts/hero-n.mjs`) muncul digit demi digit; 16 digit tenggelam ke kolam dan memicu riak. Tombol segel dengan gestur Motion; Lenis untuk scroll. | Selesai lokal, menunggu validasi user | 2026-10-19 | `npm run build` lulus (tsc strict); preview 870×992 desktop dan 375×812 ponsel: tanpa scroll horizontal, judul muat; konsol bersih. Mode reduced motion belum dicek visual. |
| 2–7 | Satu sidik jari, ke dalam kolam, rantai segel, ditekan dua kali, lunas dan diingat, penutup | Belum | | |

Catatan: `--t-hero` diturunkan ke `clamp(36px, 5.6vw, 104px)` (MASTER.md) karena "double-financing." melewati kolom kertas. Tautan "Read the spec" mengarah ke repo privat; baru bisa dibuka publik saat repo dibuka mendekati submit.
