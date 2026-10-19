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
| 1. Hero (v2, Amendment 2) | v1 (kertas kiri, kolam kanan, diam setelah intro) ditolak user: "terlalu boring, kurang immersive dan motionful, kurang iconic". Referensi level: Reeve (loop kamera) dan `MotionSites-References/prompt1–4`. v2: kolam terlindung dilihat dari atas di siang hari, full-bleed (WebGL menggantikan video CDN: caustics, lantai bergaris ledger = papan publik, kilau matahari, grain, riak di seluruh layar). Loop 10,6 dtk: invoice `TES-INV-0007` mengapung masuk, jitsuin raksasa menghantam (gelombang kejut, layar bergetar), N asli muncul, invoice tenggelam dan 16 digit N tinggal sebagai cincin cahaya; salinan invoice yang sama masuk ke cincin itu, distempel lagi, stempel retak, cincin tergambar merah dan air memerah ("Same N already on the board. Financing refused."), salinan didorong keluar, ulang. Rail 4 beat + tombol pause (WCAG 2.2.2), "Watch it catch a double" lompat ke beat 3. Dari prompt: veil blur bawah, judul blur-in per kata, kapsul liquid glass, ikon segel di judul; dari Reeve: tombol magnet. Bukti testnet asli di bawah tombol (`33b8…0a56`, blok 4509299). | Selesai lokal, menunggu validasi user | 2026-10-19 | `npm run build` lulus (tsc strict). Chrome headless real-time via CDP: 61 fps; tangkapan 1440×900, 1280×800, 900×1000, 390×844 di tiap beat; reduced motion menampilkan akhir cerita tanpa loop dan rail disembunyikan. Panel browser bawaan di-throttle 2,5 fps (juga di halaman app), jadi waktu animasi diuji di Chrome headless. |
| 1. Hero (v3, Kota Piutang) | Diorama 3D cel-shaded (three.js) kota piutang di atas lautan awan, 6 episode 第一話–第六話: invoice lahir, jitsuin, N ke papan publik dan invoice ke vault terlindung, financier A membiayai, salinan ke financier B ditolak (拒否), lunas (済). Slogan "Real invoices. Private capital. Financed once." + lede gabungan kategori dan fund. Truk berjalan di jalan lingkar tanpa teleport. | Divalidasi user ("Oke udh bagus, lanjut") | 2026-10-19 | Commit frontend `f0f1ce4`…`5d4eb2a`; Chrome real-time 61 fps; 6 ukuran layar tanpa tumpang tindih. Water field dan video Motion.so ditolak user (Amendment 2 dan 3 di MASTER.md). |
| 2. One fingerprint (指紋) | Invoice uji bisa diedit (jumlah zat ±1, jatuh tempo); N dihitung ulang langsung di browser oleh jitsuin-wasm, digit berubah satu per satu, sidik jari pusaran dari 64 digit N ber-morph, baris papan menyatakan "already on the board" atau "new fingerprint". | Divalidasi user ("Nice gas lanjut"), sidik jari versi ilustrasi garis | 2026-10-19 | 40000 → 40001 zat: 62/64 digit berubah; kembali ke 40000 memberi N semula. CSP landing + `'wasm-unsafe-eval'`. Sidik jari: ilustrasi SVG dari 32 byte N (pola whorl/spiral/loop, jumlah ridge, inti, tilt) dengan callout byte. |
| 3. Three seals (連署, Sign-to-Pay) | Surat pengalihan TES-INV-0007 dengan tiga slot segel (売 supplier, 買 buyer, 融 financier); tiap tekan membuat segel Ed25519 asli di browser, rantai tergambar, pin gembok Sign-to-Pay naik; segel ketiga membuka gembok dan advance mengalir ke supplier. "Change one zat" memeriksa ulang surat terhadap invoice yang diubah: wasm menolak ("seal is for another document"), segel retak, gembok menutup. | Divalidasi user ("Nice keren") | 2026-10-19 | jitsuin-wasm ditambah `financierSealAssignment` dan `assignmentStatus` (zcash `1cbd33d`, 7/7 test wasm lulus). Invoice landing kini memakai kunci buyer turunan master TES (indeks 7): N hero `f9755d22…5cd5`, baris papan ikut (`scripts/landing-keys.mjs`). Kunci uji diturunkan dari label `TES-` lewat SHA-256 di browser, tidak disimpan. |
| 4. Pressed twice (二重) | Adegan garis: supplier, papan publik, financier A, financier B. Empat langkah nyata: entri registrasi untuk N dengan komitmen ke A masuk papan; entri kedua untuk N yang sama ke B; B menemukan N sudah terdaftar dengan komitmen lain dan menolak (拒否); bukti tanda tangan ganda JTSP dibangun dan diverifikasi offline. | Selesai lokal, menunggu validasi | 2026-10-19 | jitsuin-wasm ditambah `supplierRegisterEntry` dan `doubleSignProof` (zcash `513112d`, 8/8 test wasm lulus). Bukti di browser: JTSP 477 byte, komitmen A `2b95f986…43e3`, B `b24124b7…4e9a`, kunci supplier `ed7ed2ff…af8b`. |
| 5–6 | Lunas dan diingat, penutup | Belum | | |

Catatan: `--t-hero` sekarang `clamp(36px, 4.6vw, 88px)`; aturan baru (glass hanya untuk kapsul di atas kolam, kapsul satu-satunya elemen bulat, `--lift-pool`) tercatat di MASTER.md Amendment 2. Sebelumnya `--t-hero` diturunkan ke `clamp(36px, 5.6vw, 104px)` (MASTER.md) karena "double-financing." melewati kolom kertas. Tautan "Read the spec" mengarah ke repo privat; baru bisa dibuka publik saat repo dibuka mendekati submit.
