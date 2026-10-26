---
tags: [design-ref, rules, mobile, layout, "DS-MOB"]
type: design-rule
id: DS-MOB
status: AKTIF
updated: 2026-10-26
---

# DS-MOB - Aturan Layout Mobile JitsuinFi

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]] · [[FE-M0 - Mandat FE|Mandat FE]] · [[FE-00 - Peta Tools FE|Tools FE]]

Aturan **layout dan struktur** untuk app dan PWA JitsuinFi di HP. Catatan ini tidak mengatur gaya visual: warna, font, kertas, segel, dan gerak tetap milik [[DS-PAL - Palet Utama JitsuinFi|DS-PAL]], `MASTER.md`, dan [[FE-M0 - Mandat FE|FE-M0]].

**Masalah yang diselesaikan:** web yang dirancang desktop-first lalu dijadikan PWA terasa sesak, karena semua informasi dipaksa masuk ke satu layar HP (paling besar sekitar 6,7"). **Solusinya kedalaman, bukan pemerasan:** satu tugas per layar, progressive disclosure, dan lebih banyak tap yang masing-masing jelas. Fungsi tetap sama di semua ukuran; yang berubah hanya berapa banyak yang terlihat sekaligus (HIG, Size classes).

## Sumber
| Kode | Sumber | Dibaca |
|---|---|---|
| M3-BP | Material 3, Breakpoints: overview, compact, medium, expanded (`m3.material.io/foundations/layout/breakpoints/*`; URL lama `applying-layout/window-size-classes` dialihkan ke sini) | 2026-10-26, browser pane |
| M3-LD | Material 3, Canonical layout examples: list-detail (`…/canonical-examples/list-detail`) | 2026-10-26 |
| M3-SP | Material 3, Grids & spacing: spacing (`…/grids-spacing/spacing`) | 2026-10-26 |
| M3-NB | Material 3, Navigation bar guidelines | 2026-10-26 |
| M3-A11Y | Material 3, Accessibility designing: structure (target sentuh 48 × 48 dp) | 2026-10-26 |
| AND-WSC | Android Developers, Use window size classes (pembagian 600 / 840 / 1200 / 1600 dp dan persentase perangkat) | 2026-10-26 |
| HIG-L | Apple HIG, Layout (hierarki, progressive disclosure, size class, safe area; diubah 2026-09-09) | 2026-10-26 |
| HIG-TB / HIG-SH / HIG-BT / HIG-A11Y | Apple HIG: Tab bars, Sheets, Buttons (hit region 44 × 44 pt), Accessibility (kontrol 44 × 44 pt, teks 17 pt) | 2026-10-26 |
| MDN-RD | MDN, Responsive design (viewport meta, breakpoint dari konten, jangan teks dengan `vw` saja) | 2026-10-26 |
| MDN-MF | MDN, PWA Responsive: Mobile first (URL ini sekarang menampilkan isi yang sama dengan MDN-RD) | 2026-10-26 |
| SK-NAT | Skill [[FE-64 - mobile-native (Emil Kowalski)\|mobile-native]] | `2d22863` |
| SK-RD | Skill responsive-design [[FE-65 - responsive-design (Mindrally)\|Mindrally]] dan [[FE-67 - responsive-design (flitzrrr)\|flitzrrr]] | `7682ca7`, `d607ba3` |
| SK-MRU | Skill [[FE-68 - mobile-responsive-ux (jacob-balslev)\|mobile-responsive-ux]] | `ee6f58e` |
| SK-AUI | Skill [[FE-69 - mobile-app-ui-design (ceorkm)\|mobile-app-ui-design]] (hanya bagian struktur) | `4c67a0e` |
| SK-MDS | Skill [[FE-70 - mobile-design-skill (evgeniyvorobey)\|mobile-design-skill]] | `0c0ce13` |
| SK-MUX | Skill [[FE-71 - mobile-ux-design (phazurlabs)\|mobile-ux-design]] | `3a3693b` |
| SK-HD | Skill [[FE-72 - mobile-design (HDShinobi)\|mobile-design]] (bagian sentuh saja) | `d10a862` |

**Satuan.** Di web, 1 dp Material = 1 pt Apple = 1 CSS px. Semua angka di bawah dalam CSS px.

**Ukuran uji.** Compact: **360 × 800** (Android kecil), **390 × 844** (iPhone standar), **430 × 932** (HP besar, ±6,7"), dan **320 px** sebagai batas bawah tanpa scroll horizontal. Medium: 768 × 1024. Expanded: 1024 × 768 dan 1280 × 800.

## Kondisi sekarang (dicek di `jitsuinfi-frontend` `aa03dde`, 2026-10-26)
- Layout HP shell aktif di `max-width: 720px` (`AppShell.tsx`, `style.css`), bukan di 600 px.
- Ada sekitar 20 nilai breakpoint berbeda di CSS (1360, 1100, 1000, 760, 720, 719, 700, 640, 560, 420, dan lain-lain).
- `index.html` sudah memakai `viewport-fit=cover`; gutter HP 16 px memakai `env(safe-area-inset-left)`; tab bar memakai `env(safe-area-inset-bottom)`.
- Belum ada web app manifest, service worker, atau `theme-color`. Jadi "PWA" belum bisa dipasang sebagai app standalone.
- Tab bar HP berisi 5 layar (`src/lib/screens.ts`), dan bisa digeser horizontal bila tidak muat (`AppShell.tsx`).
- Inbox ditaruh sebagai section di dalam halaman buyer dan member (`MailboxCard`), bukan sebagai permukaan sendiri.
- `button:hover` di `style.css` (baris 174) tidak dibungkus `@media (hover: hover)`, jadi hover bisa lengket setelah tap (T3).
- Tombol di kepala deal (`.deal-head button`, `style.css` baris 268) tingginya 36 px, di bawah 44 px (T1).

---

## A. Ukuran jendela dan pane

### L1. Tiga kelas lebar, ditentukan oleh lebar jendela, bukan jenis perangkat
- **Aturan:** compact `< 600 px`, medium `600 – 839 px`, expanded `≥ 840 px` (large `≥ 1200 px` boleh dipakai untuk konsol). Semua keputusan layout memakai tiga token ini. Breakpoint tambahan hanya untuk komponen, sebaiknya dengan container query, dan tidak untuk mengubah struktur layar.
- **Kenapa:** M3-BP memakai lima breakpoint ini untuk Android dan web. AND-WSC: compact mencakup 99,96 % HP portrait, dan lebar lebih penting dari tinggi karena konten di-scroll vertikal. HIG-L: "Determine layout based on size classes, not device type or orientation." MDN-RD dan SK-RD: breakpoint dipilih karena konten, bukan karena ukuran perangkat.
- **Cek:** `grep -rhoE "@media[^{]*" src | sort -u` hanya berisi 600 / 840 / 1200 (+ `prefers-*`, `hover`, `pointer`) untuk struktur layar. Di 599 px layout HP; di 600 px layout medium.
- **JitsuinFi:** pindahkan batas HP shell dari 720 ke 600 px. Rentang 600 – 839 px (tablet portrait, HP lipat terbuka) mendapat layout medium (L3), bukan layout desktop yang dipersempit.

### L2. Compact = satu pane, satu view
- **Aturan:** di compact hanya ada satu pane. Daftar dan detail tidak pernah tampil bersebelahan. Tidak ada sidebar, tidak ada kolom kedua.
- **Kenapa:** M3-BP compact: "Use a single pane in compact layouts", "A compact breakpoint focuses on a single view". M3-LD: di compact "Only one view is visible at a time, either list or detail".
- **Cek:** di 390 × 844, tidak ada dua elemen dengan `getBoundingClientRect().width < 0.6 * innerWidth` yang berdampingan di baris yang sama sebagai kolom konten (chip dan tombol kecil tidak dihitung).
- **JitsuinFi:** daftar invoice supplier, daftar tagihan buyer, dan in-tray konsol masing-masing satu layar; detailnya layar berikutnya.

### L3. Medium = satu pane disarankan; dua pane hanya untuk konten jarang
- **Aturan:** di 600 – 839 px pakai satu pane. Dua pane (masing-masing 50 %, spacer 24 px) hanya untuk konten berdensitas rendah dengan aksi jelas, seperti pengaturan Account.
- **Kenapa:** M3-BP medium: "a single pane is recommended because of limited screen width"; "Don't use two panes in medium layouts with high information density". M3-LD: dua pane di medium hanya untuk menelusuri koleksi dan berpindah item dengan cepat.
- **Cek:** di 768 × 1024, layar deal supplier dan bayar buyer satu pane; Account boleh dua pane.
- **JitsuinFi:** Account (daftar grup kiri, isi grup kanan) boleh dua pane; deal, bayar, dan fund tetap satu pane.

### L4. Expanded = list–detail dua pane
- **Aturan:** mulai 840 px, layar yang punya pasangan daftar → item memakai list–detail: pane daftar tetap 360 px, pane detail fleksibel, spacer 24 px, margin 24 px. Item terpilih ditandai di daftar; tombol Back tidak ada. Tanpa item terpilih, pane detail menampilkan empty state, bukan kosong.
- **Kenapa:** M3-BP expanded: "Two-pane layouts are often best", "the fixed pane should have a width of 360dp". M3-LD: "Back button: Appears in detail view only for single-pane layouts"; "Selected state: Appears only in list view for two-pane layouts".
- **Cek:** di 1280 × 800, `/supplier` menampilkan daftar invoice (360 px) + deal terpilih; resize ke 600 px menampilkan detail yang sama dengan app bar + Back; scroll dan item terpilih tidak hilang.
- **JitsuinFi:** supplier (invoice → deal), buyer (tagihan → review/bayar), konsol (in-tray → item), member (riwayat payout → kuitansi).

### L5. Ganti ukuran tanpa kehilangan state
- **Aturan:** saat lebar berubah (rotasi, lipat, split screen), item terpilih, posisi scroll, isian yang sedang diketik, dan sheet yang terbuka tetap ada. Dari dua pane ke satu pane dengan item terpilih, tampilkan detail; tanpa item terpilih, tampilkan daftar.
- **Kenapa:** M3-LD (Transitioning between layouts, Persistent states). SK-MDS `docs/adaptive-layout.md`: "Resize without state loss is the hard requirement".
- **Cek:** buka deal, ketik di satu field, ubah viewport 1280 → 390 → 1280: field dan pilihan masih sama.
- **JitsuinFi:** state terpilih disimpan di URL (`/supplier?deal=…` atau path), bukan hanya di state komponen.

### L6. Margin dan gutter
- **Aturan:** compact margin kiri-kanan 16 px (`max(16px, env(safe-area-inset-left))`); medium dan expanded 24 px; spacer antar pane 24 px.
- **Kenapa:** M3-BP compact "Margins are 16dp"; medium dan expanded "margins of 24dp", "The spacer between panes is also 24dp".
- **Cek:** di 390 px, `getComputedStyle(main).paddingLeft` = 16 px; di 768 dan 1280 px = 24 px.
- **JitsuinFi:** compact sudah 16 px (`--gutter`); medium dan expanded masih memakai clamp landing (5vw). Samakan ke 24 px di app.

---

## B. Navigasi

### N1. Tab bar bawah: 3 – 5 tujuan, posisi tetap, selalu terlihat
- **Aturan:** di compact (dan medium satu pane), navigasi utama adalah tab bar di bawah dengan 3 – 5 tujuan tingkat atas. Setiap tab punya ikon + label. Tab tidak pernah digeser, diurutkan ulang, atau disembunyikan, dan tidak dipakai untuk aksi. Tab bar tetap terlihat di semua layar tingkat atas; hanya sheet modal yang boleh menutupinya.
- **Kenapa:** M3-NB: "three to five destinations"; "Navigation bar destinations have fixed positions. Don't scroll them or modify their positions"; "Don't swipe between destinations". HIG-TB: "Use a tab bar to support navigation, not to provide actions"; "Make sure the tab bar is visible"; "aim for a default list of five or fewer"; hindari tab More. SK-MRU dan SK-MUX: ikon tanpa label ambigu.
- **Cek:** di 320, 360, dan 390 px, `nav.scrollWidth === nav.clientWidth` (tidak ada scroll), jumlah tab 3 – 5, setiap tab punya teks label yang terlihat.
- **JitsuinFi:** tab bar sekarang berisi 5 tab (Home, Try, Verify, peran, Account), tetapi bisa digeser. Pastikan lima tab muat di 320 px tanpa scroll. Logika geser di `AppShell.tsx` boleh tetap sebagai pengaman, tetapi tidak boleh pernah aktif di ukuran uji. Untuk pengguna yang sudah masuk, apakah Try dan Verify layak mendapat slot tab adalah keputusan IA user (lihat Pertanyaan terbuka).

### N2. Medium/expanded: tab bar berganti jadi rail di sisi kiri
- **Aturan:** di medium satu pane dan di expanded, tab bar diganti navigation rail di tepi kiri dengan tujuan dan urutan yang sama. Di medium dua pane, tab bar bawah tetap dipakai supaya kedua pane mendapat lebar penuh.
- **Kenapa:** M3-BP: "Swap a navigation bar in a compact layout for a navigation rail in a medium or expanded layout"; medium: "Single-pane layouts: Navigation rail. Two-pane layouts: Navigation bar". Komponen yang ditukar harus setara fungsinya.
- **Cek:** daftar tujuan rail = daftar tujuan tab bar (`screens.ts`), urutannya sama.
- **JitsuinFi:** nav desktop atas yang sekarang menjadi rail di ≥ 600 px. Bisa juga tetap nav atas untuk ≥ 840 px asal tujuannya sama.

### N3. Top app bar per layar: judul + Back + maksimal satu aksi ikon
- **Aturan:** setiap layar di bawah tingkat atas punya app bar atas: Back di kiri, judul layar, maksimal satu aksi ikon di kanan (misalnya Inbox). Judul besar boleh mengecil saat di-scroll. Aksi utama layar **tidak** di app bar (lihat P2).
- **Kenapa:** SK-MUX (iOS: navigation bar di atas dengan Back, judul besar mengecil). SK-MRU: zona atas 20 % sulit dijangkau, jadi isinya aksi jarang. M3-BP medium: hindari interaksi penting di 25 % atas.
- **Cek:** di 390 × 844, app bar memuat ≤ 2 kontrol (Back + 1 ikon); tidak ada tombol aksi utama di 20 % atas layar.
- **JitsuinFi:** deal supplier, review invoice buyer, bayar, kuitansi, item in-tray konsol.

### N4. Back dan kedalaman
- **Aturan:** Back selalu kembali ke layar sebelumnya dalam tumpukan yang sama, dengan scroll dan pilihan yang sama. Back browser, gestur Back sistem, dan tombol Back app memberi hasil yang sama (satu entri history per layar; sheet ditutup oleh Back). Kedalaman maksimal 4 level dari tab.
- **Kenapa:** SK-MUX: hindari stack lebih dari 4 level; deep link harus mendarat di posisi tumpukan yang benar. HIG-SH: menutup sheet harus kembali ke induknya. M3-LD: posisi scroll dipertahankan.
- **Cek:** tab → daftar → detail → sheet, lalu Back tiga kali: kembali ke daftar dengan item dan scroll yang sama. Hitung level: tab = 1, maksimal 4.
- **JitsuinFi:** Supplier (1) → deal (2) → stasiun/surat (3) → konfirmasi segel sebagai sheet (bukan level). Deep link dari Inbox membuka deal dengan Back ke daftar, bukan ke halaman kosong.

### N5. Sheet vs halaman
- **Aturan:** pakai **sheet** untuk tugas pendek yang selesai lalu kembali ke induk: konfirmasi, pilih satu dari beberapa, filter, satu isian kecil, Inbox. Pakai **halaman** untuk tugas panjang atau bertahap, isi yang perlu di-link, dan apa pun yang punya sub-langkah. Hanya satu sheet terbuka pada satu waktu. Sheet punya tombol Close/Cancel yang terlihat; bila ada Done, selalu ada Cancel atau Back. Tinggi sheet: peek ±25 %, setengah ±50 %, penuh ±90 % viewport. Pada sheet tinggi penuh, tombol Close selalu tersedia.
- **Kenapa:** HIG-SH: sheet untuk "a simple task that they can complete before returning to the parent view"; "For complex or prolonged user flows, consider alternatives to sheets"; "Display only one sheet at a time"; Done dipasangkan dengan Cancel. M3-BP: bottom sheet adalah komponen aksi di compact; menu di medium dan expanded. SK-MRU: tinggi peek/half/full.
- **Cek:** buka setiap sheet: ada Close yang terlihat, Back browser menutupnya, tidak ada sheet yang membuka sheet kedua di atasnya.
- **JitsuinFi:** sheet untuk konfirmasi segel/tanda tangan, pilih financier, filter daftar, Inbox. Halaman untuk review invoice buyer, deal supplier, bayar ke dana.

### N6. Inbox = satu sheet dari app bar, bukan section di setiap halaman
- **Aturan:** Inbox dibuka dari satu ikon dengan badge jumlah di app bar (atau sebagai tab bila user memilihnya, lihat Pertanyaan terbuka). Di compact, Inbox adalah sheet setinggi ±90 % yang berisi daftar pesan; tap satu pesan menutup sheet dan membuka layar tujuannya (deep link). Di expanded, Inbox boleh jadi sheet samping atau pane pendukung kanan. Halaman peran tidak lagi menempelkan section Inbox penuh; paling banyak satu baris "2 pesan baru" yang membuka sheet itu.
- **Kenapa:** HIG-SH (tugas pendek, kembali ke induk). HIG-TB: badge untuk informasi baru. SK-MDS: "Act where it is shown": setiap pesan membawa aksinya. M3-LD: "Email inbox + selected email" adalah pasangan list–detail.
- **Cek:** di 390 × 844, halaman buyer dan member tidak berisi daftar pesan Inbox; ada satu kontrol Inbox dengan badge; membuka dan menutupnya tidak mengubah scroll halaman di bawahnya.
- **JitsuinFi:** `MailboxCard` di BuyerPage dan MemberPage dipindah ke satu sheet bersama di shell.

---

## C. Satu tugas per layar dan progressive disclosure

### P1. Satu layar = satu tugas utama
- **Aturan:** sebelum mendesain, tulis satu kalimat: "Layar ini untuk ___." Layar 1 menjawab pertanyaan utama dan memuat aksi untuk tugas itu. Semua yang lain ada di balik satu tap.
- **Kenapa:** SK-MDS §1: tentukan momen dan 1 – 3 tugas, lalu "the primary job is finished on this screen". SK-MUX: "One primary action per screen", "Design for interruption". SK-MRU: HP dipakai untuk cek cepat dan satu aksi, bukan analisis desktop. HIG-L: "too much content and too many choices makes it harder to find information quickly".
- **Cek:** setiap layar punya kalimat tugas di komentar file halaman atau di catatan desain; reviewer bisa menunjuk satu elemen yang menjawabnya di layar pertama 390 × 844 tanpa scroll.
- **JitsuinFi:** lihat tabel "Layar 1 vs di balik tap".

### P2. Maksimal satu aksi utama per layar, di zona jempol
- **Aturan:** setiap layar punya **paling banyak satu** tombol aksi utama (gaya primer). Aksi lain jadi sekunder (teks/outline) atau masuk menu/sheet. Di compact, aksi utama berada di 50 % bawah layar, sebaiknya di bar bawah yang menempel, di atas tab bar dan safe area. Aksi merusak (tolak, batalkan) tidak diletakkan di posisi aksi utama.
- **Kenapa:** SK-MUX ("resist the urge to present multiple equal-weight choices"). SK-MRU (aksi utama di 50 % bawah; jangan aksi utama di atas). SK-AUI (CTA di thumb zone). SK-HD (aksi merusak jauh dari jangkauan mudah).
- **Cek:** di 390 × 844, tombol primer (`main button:not(.secondary)`, gaya dasar `button` di `style.css`) yang terlihat di viewport ≤ 1; titik tengahnya `y > 0.5 * innerHeight`.
- **JitsuinFi:** deal supplier: hanya aksi stasiun yang sedang aktif yang primer; buyer: "Tanda tangani" atau "Bayar", bukan keduanya; member: "Bayar ke dana" hanya bila memang tugas utama layar itu.

### P3. Tampilkan jawabannya, bahan hitungannya di balik tap
- **Aturan:** bila pengguna harus menjumlah, membandingkan, atau mengingat sesuatu untuk mendapat yang ia cari, hitung dan tampilkan hasilnya di layar 1 (misalnya "Jatuh tempo 3 hari lagi, 12.500.000"). Nilai mentah (hash, salt, commitment, txid, key) ada di detail, ditandai sebagai bukti.
- **Kenapa:** SK-MDS §1.2 "Show the answer, not its inputs". SK-AUI: nilai lebih menonjol dari label.
- **Cek:** di layar 1 setiap peran tidak ada string hex/base58 lebih dari 16 karakter; string seperti itu hanya muncul setelah tap "Bukti" atau "Detail".
- **JitsuinFi:** supplier: "Advance diterima sesuai kesepakatan" di layar 1; `Advance transaction id`, `Commitment salt`, `Letter document hash` di detail stasiun. Member: "Dana menutup unit Anda: ya" di layar 1; komposisi dan bukti di balik tap.

### P4. Aturan layar 1 (yang terlihat tanpa scroll di 390 × 844)
- **Aturan:** layar 1 berisi, berurutan: (1) judul layar, (2) status atau jawaban utama, (3) satu aksi utama bila ada, (4) awal daftar atau ringkasan berikutnya. Paragraf penjelasan lebih dari 2 baris, catatan "apa yang tidak dibuktikan", dan data publik masuk ke disclosure ("Selengkapnya", baris yang membuka halaman/sheet).
- **Kenapa:** HIG-L: "Use progressive disclosure… disclosure triangles, menus, or nested views to reduce how much content to initially display". SK-MRU: "show the headline, tap to see details". SK-RD (flitzrrr): ubah penyajian di HP, jangan sekadar `display:none`.
- **Cek:** di 390 × 844, ukur `innerHeight` pertama: tidak ada blok teks > 3 baris di atas lipatan; ada maksimal 1 aksi utama.
- **JitsuinFi:** member "What this does not prove" dan "What others can see" menjadi baris disclosure; buyer "History certificate" menjadi halaman dari "My payment history".

### P5. Disclosure tetap terlihat dan bisa dijangkau
- **Aturan:** setiap yang disembunyikan punya pintu yang terlihat dengan label kata kerja atau nama isi ("Lihat 12 kuitansi", "Bukti teknis"), bukan ikon saja. Jangan sembunyikan fungsi berdasarkan lebar: fungsi sama di semua ukuran, hanya jumlah yang terlihat sekaligus yang berubah.
- **Kenapa:** HIG-L: "Don't change your app's functionality based on the space it occupies… you can change the amount of functionality that's visible". SK-RD (flitzrrr): jangan menyembunyikan konten di HP hanya dengan `display:none`.
- **Cek:** bandingkan daftar aksi di 1280 px dan 390 px: setiap aksi desktop bisa dicapai di 390 px dalam ≤ 2 tap.
- **JitsuinFi:** berlaku untuk semua halaman peran dan konsol.

### P6. Langkah bertahap: hanya langkah aktif yang terbuka
- **Aturan:** alur bertahap (stasiun deal, review → tanda tangan, rantai tiga segel) di compact menampilkan stepper ringkas: langkah selesai = satu baris ringkasan dengan centang; langkah aktif = terbuka penuh dengan aksinya; langkah berikutnya = nama saja. Tap langkah selesai membuka detailnya.
- **Kenapa:** SK-MUX (progressive disclosure di form; "Ask only what is absolutely necessary for the current step"). SK-MDS (design the peak moment). [[DS-00 - Peta Visual Design|DS-00]]: stepper DS-06 = rantai tiga segel.
- **Cek:** di 390 × 844, pada deal dengan 6 stasiun, hanya 1 stasiun yang terbuka; tinggi stepper tertutup ≤ 56 px per langkah.
- **JitsuinFi:** stasiun deal supplier (Invoice created → Board entry signed → Offer → Advance → Letter → Settlement), review buyer.

---

## D. Sentuh dan jangkauan

### T1. Target sentuh minimal 44 × 44 px, disarankan 48 × 48 px, jarak 8 px
- **Aturan:** setiap kontrol berulang (tombol, link di daftar, chip, checkbox, ikon, baris daftar) punya area sentuh ≥ 44 × 44 px; aksi utama ≥ 48 px tinggi. Jarak antar target ≥ 8 px. Ikon kecil (16 – 24 px) diperbesar area sentuhnya dengan padding, bukan diperbesar gambarnya.
- **Kenapa:** HIG-BT: "a button needs a hit region of at least 44x44 pt". HIG-A11Y: kontrol default 44 × 44 pt, minimum 28 × 28 pt. M3-A11Y: "touch targets at least 48 x 48dp", jarak 8 dp. WCAG 2.2 AA 2.5.8: minimum 24 × 24 CSS px; SK-MRU memakai 44 sebagai lantai ergonomis.
- **Cek:** skrip di 390 px: untuk setiap `a, button, [role=button], input, select, summary, label[for]` yang terlihat, `getBoundingClientRect()` (termasuk padding) ≥ 44 × 44; laporkan yang gagal.
- **JitsuinFi:** semua layar; perhatikan ikon Inbox, tombol salin hash, chip filter, dan link di board gelap.

### T2. Zona jempol
- **Aturan:** di compact, 50 % bawah untuk aksi utama dan tab bar; tengah untuk konten dan aksi sekunder; 20 % atas untuk judul, Back, dan aksi jarang. Jangan menaruh kontrol custom di area safe-area bawah (indikator home).
- **Kenapa:** SK-MRU (peta zona: atas 20 %, tengah 30 %, bawah 50 %). SK-MUX (Hoober; HP 6,5" ke atas membuat kiri atas sulit). M3-BP medium (25 % atas di luar jangkauan, jangan terlalu mepet tepi bawah). SK-MDS `platform.md`: kontrol custom di luar inset safe-area bawah.
- **Cek:** di 430 × 932, titik tengah aksi utama berada di `0.5 – 0.9 × innerHeight` dan di atas `env(safe-area-inset-bottom)`.
- **JitsuinFi:** tombol Tanda tangani, Bayar, Segel, Tawarkan.

### T3. Tidak ada aksi yang hanya lewat hover atau hanya lewat gestur
- **Aturan:** semua yang muncul saat hover (tooltip, aksi baris, menu) punya padanan tap atau tampil langsung. Gaya hover dibungkus `@media (hover: hover) and (pointer: fine)`. Gestur (geser untuk aksi, tarik untuk tutup sheet) selalu punya tombol yang terlihat.
- **Kenapa:** SK-NAT (hover lengket setelah tap; "Media queries over device sniffing"). SK-MRU dan SK-MUX ("Never use swipe as the only way"). SK-RD (flitzrrr).
- **Cek:** `grep -rn ":hover" src` → setiap aturan ada di dalam blok media `hover: hover`; tidak ada `title=""` yang menjadi satu-satunya tempat informasi.
- **JitsuinFi:** board gelap, tabel rate index, loupe di `/verify`, aksi baris konsol.

---

## E. Safe area, viewport, dan PWA standalone

### S1. Konten di dalam safe area, latar boleh sampai tepi
- **Aturan:** `viewport-fit=cover` di meta viewport; app bar atas memakai `padding-top: env(safe-area-inset-top)`; tab bar, bar aksi bawah, sheet, dan toast memakai `env(safe-area-inset-bottom, 0px)`; gutter kiri-kanan `max(16px, env(safe-area-inset-left/right))`. Setiap tepi diatur sendiri.
- **Kenapa:** SK-NAT §7: tanpa `viewport-fit=cover` nilai `env()` = 0. HIG-L: menghormati safe area "is essential to make sure system UI and hardware features like the Dynamic Island don't obstruct content and controls". SK-MDS `platform.md`: safe area tidak simetris.
- **Cek:** mode standalone di iPhone asli (atau Simulator): judul tidak di bawah Dynamic Island; tab bar tidak menimpa indikator home; landscape: konten tidak di bawah notch kiri/kanan.
- **JitsuinFi:** meta dan gutter sudah ada; cek `env(safe-area-inset-right)` dan inset atas di app bar.

### S2. Tinggi layar memakai `dvh`/`svh`, bukan `100vh`
- **Aturan:** shell app dan sheet memakai `100dvh`; layar pertama yang tidak boleh terpotong memakai `100svh`. `100vh` tidak dipakai untuk elemen yang punya tombol di bawah.
- **Kenapa:** SK-NAT §3: `100vh` = viewport terbesar, tombol bawah tertutup bar URL.
- **Cek:** `grep -rn "100vh" src` kosong untuk app dan konsol.
- **JitsuinFi:** konsol sudah `100dvh`.

### S3. PWA standalone: manifest, `theme-color`, dan status bar
- **Aturan:** sediakan web app manifest (`display: "standalone"`, `theme_color`, `background_color`, ikon), `<meta name="theme-color">` per `prefers-color-scheme` yang sama dengan warna paling atas layar (app bar), dan status bar iOS yang serasi (`apple-mobile-web-app-status-bar-style`). Uji sebagai app terpasang, karena mode standalone mengubah viewport, safe area, dan status bar.
- **Kenapa:** SK-NAT §10 dan §11. MDN-RD: selalu sertakan meta viewport.
- **Cek:** Chrome DevTools → Application → Manifest tanpa error; dipasang ke Home Screen iPhone: warna status bar sama dengan app bar; tidak ada pita warna lain di atas.
- **JitsuinFi:** **belum ada manifest** (lihat Kondisi sekarang). Ini syarat sebelum menyebut app "PWA". Manifest harus same-origin sesuai [[FE-01 - Batasan Platform FE|FE-01]].

### S4. Jangan pernah mematikan zoom
- **Aturan:** tidak ada `user-scalable=no` atau `maximum-scale=1`. Masalah zoom pada input diselesaikan dengan font input ≥ 16 px (F2).
- **Kenapa:** SK-NAT Hard Rule 4; SK-RD (Mindrally): uji sampai zoom 200 %.
- **Cek:** `grep -n "user-scalable\|maximum-scale" index.html` kosong.
- **JitsuinFi:** sekarang sudah benar; jaga.

---

## F. Tipografi dan panjang baris di compact

### Y1. Panjang baris dan ukuran teks
- **Aturan:** teks isi ≥ 16 px; teks bantu ≥ 13 px; baris isi 40 – 75 karakter (di 390 px dengan margin 16 px biasanya 40 – 48, sudah pas). Di medium dan expanded, kolom teks dibatasi `max-width: 65ch` (atau ~640 px), bukan melebar penuh. Ukuran teks tidak memakai `vw` saja; selalu `clamp(rem, …, rem)` atau `calc(rem + vw)`.
- **Kenapa:** M3-BP: "adjust margins and type styles to keep text between 40–60 characters per line". SK-RD (flitzrrr) dan SK-MUX: 45 – 75 karakter. MDN-RD: "you should never set text using viewport units alone". HIG-A11Y: teks default iOS 17 pt, minimum 11 pt.
- **Cek:** di 390 px, `getComputedStyle(p).fontSize ≥ 16px`; di 1280 px, lebar `p` ≤ 75 karakter (≈ `65ch`).
- **JitsuinFi:** `main` app sudah dibatasi 880 px; paragraf panjang di dalam `main.wide` (1440 px) perlu batas `ch` sendiri.

### Y2. Teks membesar tanpa memecah layout
- **Aturan:** layout tetap bisa dipakai dengan teks 200 % (zoom browser atau Dynamic Type lewat pengaturan teks). Tidak ada kotak tinggi tetap di sekitar teks; baris berdampingan boleh ditumpuk vertikal saat sempit. Judul panjang boleh 2 baris (`text-wrap: balance`), tidak dipotong `…` bila itu satu-satunya tempat informasi.
- **Kenapa:** HIG-L "Be prepared for text-size changes… horizontally adjacent views may need to stack vertically". SK-MDS §3 (teks sampai 200 %, tanpa kotak tinggi tetap). SK-MDS §2: di baris tersempit, rapatkan jarak dulu sebelum memotong teks.
- **Cek:** di 390 px dengan zoom 200 %, tidak ada teks terpotong atau tumpang tindih; tidak ada scroll horizontal.
- **JitsuinFi:** nama pihak dan nominal di daftar invoice, nameplate board gelap.

---

## G. Form di HP

### F1. Satu kolom, label di atas, tombol utama menempel di bawah
- **Aturan:** form di compact satu kolom; label di atas field; field multi-baris di akhir form; tombol utama di bar bawah yang menempel (di atas safe area) atau tepat setelah field terakhir, tidak di atas form. Validasi saat blur, pesan error di bawah field.
- **Kenapa:** SK-MUX ("One column only"; "Top-aligned labels"; "validate on blur"). Referensi SK-MUX `mobile-form-navigation.md`: field multi-baris di bawah agar keyboard tidak menutup field lain. SK-MRU (aksi utama di bawah).
- **Cek:** di 390 px, setiap `form` punya satu kolom (`input` tidak berdampingan); tombol submit terlihat saat keyboard terbuka (uji di perangkat).
- **JitsuinFi:** Apply, tawaran supplier ke financier, bayar ke dana, pairing konsol, Sign in.

### F2. Keyboard yang tepat dan font input 16 px
- **Aturan:** nominal: `inputmode="decimal"`; kode: `inputmode="numeric"` + `autocomplete="one-time-code"` bila OTP; email: `type="email"`; pencarian: `type="search"` + `enterkeyhint="search"`; key/alamat/hash: `autocapitalize="none" autocorrect="off" spellcheck="false"`. Font input ≥ 16 px agar iOS tidak zoom. `enterkeyhint` sesuai aksinya (`next`, `done`, `send`). Meta viewport memakai `interactive-widget=resizes-content` supaya bar bawah naik bersama keyboard di Android.
- **Kenapa:** SK-NAT §4 dan Baseline. SK-MRU (tabel input mobile). SK-MUX (autofill, keyboard).
- **Cek:** `grep` setiap `<input` di `src/pages` punya `type`/`inputmode` yang sesuai isinya; `getComputedStyle(input).fontSize ≥ 16px` di 390 px.
- **JitsuinFi:** nominal invoice dan advance, key financier, txid, alamat Zcash.

### F3. Kurangi yang diketik
- **Aturan:** pilih daripada ketik (chip, segmented control, picker) untuk pilihan umum; isi default dari konteks; minta hanya yang perlu untuk langkah ini. Rentang tanggal memakai preset ("Bulan ini", "30 hari") + opsi custom di sheet.
- **Kenapa:** SK-MUX (Form Reduction). SK-MRU (anti-pattern date range picker desktop). SK-AUI (Selection Over Manual Input).
- **Cek:** hitung field yang wajib diketik per layar form; target ≤ 3 di compact.
- **JitsuinFi:** pilih financier dari direktori, bukan ketik key; jatuh tempo dengan preset.

---

## H. Daftar panjang, tabel, dan data lebar

### D1. Daftar panjang: kelompok, cari, tampilkan lebih banyak
- **Aturan:** daftar > 7 item dikelompokkan dengan judul kelompok (status atau waktu: "Perlu tindakan", "Menunggu", "Selesai"); daftar > 20 item punya pencarian di atas dan memuat 20 pertama + "Tampilkan lebih banyak" (atau muat saat scroll). Kelompok "Perlu tindakan" selalu paling atas. Daftar kosong punya empty state dengan langkah berikutnya.
- **Kenapa:** HIG-L ("Group related items"). M3-SP (pengelompokan implisit lewat jarak, eksplisit lewat garis). SK-AUI (jangan layar pencarian kosong; empty state dengan CTA). SK-MDS §3 (state kosong, loading, error, offline).
- **Cek:** isi data contoh 40 item: layar 1 di 390 × 844 menampilkan judul kelompok pertama dan ≥ 4 baris; ada kotak cari; tidak ada lebih dari 20 baris yang dirender sekaligus sebelum "Tampilkan lebih banyak".
- **JitsuinFi:** daftar invoice supplier, tagihan buyer, riwayat pembayaran, kuitansi member, in-tray konsol, direktori di lobby.

### D2. Tabel lebar di HP menjadi baris ringkas + detail
- **Aturan:** di compact tidak ada tabel dengan > 3 kolom dan tidak ada tabel yang di-scroll horizontal. Setiap baris menjadi satu baris daftar dengan 3 – 4 data: judul (pihak atau nomor) + status di baris atas, nominal dan tanggal di baris bawah, chevron ke detail. Semua kolom lain ada di layar detail. Baris ini adalah baris daftar, bukan kartu kotak berisi paragraf (M5 di [[FE-M0 - Mandat FE|FE-M0]]).
- **Kenapa:** SK-MRU ("Show 3-4 data points per card, not 8+ columns"; "Never horizontal scroll a data table on mobile"). SK-RD (flitzrrr): tidak ada elemen lebih lebar dari viewport.
- **Cek:** di 390 px, `document.documentElement.scrollWidth === innerWidth`; tidak ada elemen `table` dengan `scrollWidth > clientWidth`.
- **JitsuinFi:** rate index (`RatesPage`), fund ledger konsol, riwayat pembayaran buyer, daftar unit member.

### D3. Board gelap (pita data gelap) di compact: ringkasan, bukan papan penuh
- **Aturan:** board publik gelap (strip verify, board outsider, rate band, strip buyer dan financier, buku registry try) di compact menampilkan nameplate + maksimal 3 entri atau 2 – 4 angka (tata letak 2 kolom), lalu satu baris "Lihat board lengkap" ke halaman atau sheet. Tinggi pita ≤ 40 % `innerHeight` di 390 × 844. Tidak ada scroll horizontal di dalam pita.
- **Kenapa:** SK-MRU (KPI 2-up di bawah 640 px; detail di balik tap; tidak ada grafik di dalam kartu KPI di HP). HIG-L (progressive disclosure). M3-BP (yang disembunyikan di layar kecil bisa ditampilkan di layar besar).
- **Cek:** di 390 × 844, setiap board gelap: `height ≤ 0.4 × innerHeight`, `scrollWidth === clientWidth`, jumlah entri ≤ 3.
- **JitsuinFi:** kelas `.by-board-in`, `.fi-board`, `.vf-board-k`, `.os-bd-head`, `.ri-src`, `.tcase .bd-k` (`style.css`).

---

## I. Yang tidak boleh

| Larangan | Kenapa | Cara cek |
|---|---|---|
| Mengecilkan layout desktop ke HP (font, jarak, dan target dikecilkan supaya semua muat) | SK-MRU: "Mobile is not a smaller desktop"; SK-RD (flitzrrr): retrofit desktop = konten tersembunyi dan kompromi | Di 390 px: teks isi ≥ 16 px, target ≥ 44 px, maksimal 1 aksi utama |
| Scroll horizontal halaman atau tabel | SK-MRU, SK-RD | `scrollWidth === innerWidth` di 320, 360, 390 px |
| Multi kolom di compact (sidebar, dua pane, grid > 2 kolom untuk konten) | M3-BP, M3-LD | L2 |
| Aksi hanya lewat hover atau gestur | SK-NAT, SK-MRU, SK-MUX | T3 |
| Tab bar yang di-scroll, > 5 tab, atau ikon tanpa label | M3-NB, HIG-TB | N1 |
| Aksi utama di app bar atas | SK-MRU, M3-BP | P2, N3 |
| Sheet di atas sheet; sheet tanpa Close | HIG-SH | N5 |
| Modal tengah gaya desktop dengan tombol tutup kecil di compact | SK-MRU anti-pattern 2; M3-BP (bottom sheet di compact) | Tidak ada dialog tengah selain konfirmasi singkat |
| Mematikan zoom | SK-NAT, MDN | S4 |
| `100vh` untuk shell dengan tombol bawah | SK-NAT | S2 |
| Memilih layout dari user agent atau orientasi | HIG-L, SK-NAT | Tidak ada `navigator.userAgent` untuk layout |
| Menyembunyikan fungsi hanya karena layar kecil | HIG-L, SK-RD | P5 |
| Mengambil gaya visual dari skill (Tailwind, Lucide, glassmorphism, kartu `rounded-2xl`, Liquid Glass) | Gaya JitsuinFi milik DS-PAL, `MASTER.md`, FE-M0 | Review visual terhadap DS-PAL |

---

## Layar 1 vs di balik tap (compact, 390 × 844)

| Layar | Tugas utama (satu kalimat) | Layar 1 | Di balik satu tap | Aksi utama | Expanded (≥ 840 px) |
|---|---|---|---|---|---|
| Lobby `/app` | "Ke mana saya sekarang?" | Siapa Anda (peran/tamu), satu langkah berikutnya (`NextRoom`), pengingat jatuh tempo bila ada | Direktori (rate index, outsiders), penjelasan produk | Langkah berikutnya | Lobby + direktori di pane kedua |
| Supplier: invoice | "Invoice mana yang perlu saya tindak?" | Kelompok "Perlu tindakan" + 4 baris invoice (pihak, status, nominal, tanggal) | Invoice lain (kelompok lain), filter (sheet), buat invoice baru | "Invoice baru" atau tindakan baris teratas | List 360 px + deal terpilih |
| Supplier: deal | "Apa langkah berikutnya untuk deal ini?" | Status deal dalam satu kalimat, stepper stasiun ringkas, stasiun aktif terbuka | Detail stasiun selesai, bukti teknis (hash, salt, txid), surat pengalihan | Aksi stasiun aktif (Tawarkan, Segel, Catat advance) | Pane detail |
| Supplier: stasiun | "Apa yang terjadi di langkah ini?" | Hasil langkah ("Advance diterima sesuai kesepakatan") | Nilai mentah dan unduhan bundle | "Simpan bundle" bila itu langkahnya | Bagian dari pane detail |
| Buyer: tagihan | "Apa yang harus saya bayar dan kapan?" | Tagihan berikutnya (nominal, jatuh tempo), lalu daftar tagihan berkelompok | Tagihan selesai, riwayat | Buka tagihan teratas | List + tagihan terpilih |
| Buyer: review/tanda tangan | "Apakah invoice ini benar?" | Ringkasan invoice (pihak, nominal, jatuh tempo) | Detail baris, pengakuan pengalihan, kunci | "Tanda tangani" (konfirmasi di sheet) | Pane detail |
| Buyer: bayar | "Bayar ke mana dan berapa?" | Nominal dan tujuan pembayaran | Cara membayar, bukti | "Bayar" | Pane detail |
| Buyer: riwayat | "Seberapa baik riwayat saya?" | Ringkasan riwayat (jumlah tepat waktu, terlambat) | Daftar pembayaran, sertifikat riwayat (halaman) | — (atau "Bagikan sertifikat") | List + sertifikat |
| Member: dana | "Apakah dana menutup unit saya?" | Jawaban ya/tidak + nilai unit Anda | "What the fund holds", "What this does not prove", "What others can see" (disclosure) | "Bayar ke dana" hanya bila tugas utama | Ringkasan + komposisi di pane kedua |
| Member: unit/payout | "Apa yang sudah dibayarkan?" | Total dibayarkan + 4 baris kuitansi | Kuitansi lain, detail kuitansi | — | List + kuitansi |
| Inbox (sheet) | "Pesan apa yang perlu saya tindak?" | Pesan belum dibaca, terbaru di atas | Isi pesan = layar tujuannya | Buka pesan teratas | Sheet samping / pane pendukung |
| Account | "Siapa saya di app ini dan apa yang bisa saya ubah?" | Identitas peran + grup pengaturan (daftar) | Isi tiap grup (halaman), keluar, hapus data lokal | — | Dua pane (grup + isi), juga di medium (L3) |
| Konsol node | "Apa yang perlu saya putuskan sekarang?" | In-tray (jumlah + item teratas) | Rules for offers, Fund ledger, Keys and cards (masing-masing halaman/segmen) | Putuskan item teratas | List in-tray + item; bagian lain di rail |

`/try` dan `/verify` adalah adegan imersif (65/35, M3 di [[FE-M0 - Mandat FE|FE-M0]]): satu adegan per layar, kontrol adegan di zona jempol, aturan T1, S1, S2, dan I tetap berlaku.

---

## Audit mobile per layar

Jalankan per layar, di 390 × 844 dulu, lalu 320, 430 × 932, 768 × 1024, dan 1280 × 800. Catat hasil sebagai `lulus / gagal + elemen`.

1. **Tugas:** tulis satu kalimat tugas layar. Elemen yang menjawabnya terlihat tanpa scroll di 390 × 844. (P1)
2. **Aksi utama:** tombol primer terlihat ≤ 1; titik tengahnya di 50 % bawah dan di atas safe area. (P2, T2)
3. **Layar 1:** tidak ada blok teks > 3 baris dan tidak ada string hex/key > 16 karakter di atas lipatan. (P3, P4)
4. **Pane:** satu pane di < 600 px; satu pane di 600 – 839 kecuali Account; list–detail di ≥ 840 px dengan list 360 px. (L2 – L4)
5. **Resize:** 1280 → 390 → 1280 mempertahankan item terpilih, scroll, dan isian. (L5)
6. **Margin:** 16 px di compact, 24 px di medium/expanded. (L6)
7. **Tab bar:** 3 – 5 tab berlabel, `scrollWidth === clientWidth` di 320 px, terlihat di semua layar tingkat atas. (N1)
8. **App bar dan Back:** ≤ 2 kontrol di app bar; Back app = Back browser; kedalaman ≤ 4. (N3, N4)
9. **Sheet:** maksimal satu; ada Close; Back menutupnya; tidak dipakai untuk alur panjang. Inbox dibuka sebagai sheet, bukan section halaman. (N5, N6)
10. **Target sentuh:** semua kontrol ≥ 44 × 44 px, jarak ≥ 8 px (skrip T1). (T1)
11. **Hover/gestur:** semua `:hover` di dalam `@media (hover: hover) and (pointer: fine)`; setiap gestur punya tombol. (T3)
12. **Safe area dan tinggi:** konten tidak tertutup notch/indikator home (standalone); tidak ada `100vh`. (S1, S2)
13. **PWA:** manifest valid, `theme-color` cocok dengan app bar, zoom tidak dimatikan. (S3, S4)
14. **Teks:** isi ≥ 16 px, baris 40 – 75 karakter, zoom 200 % tanpa potong atau scroll horizontal. (Y1, Y2)
15. **Form:** satu kolom, label di atas, `inputmode`/`type` benar, font input ≥ 16 px, tombol submit terlihat saat keyboard terbuka. (F1 – F3)
16. **Daftar:** > 7 item dikelompokkan; > 20 item ada cari dan "Tampilkan lebih banyak"; empty state punya langkah berikutnya. (D1)
17. **Data lebar:** tidak ada tabel > 3 kolom di compact; `documentElement.scrollWidth === innerWidth` di 320/360/390 px. (D2)
18. **Board gelap:** tinggi ≤ 40 % viewport, ≤ 3 entri, tanpa scroll horizontal, ada "Lihat board lengkap". (D3)
19. **Perangkat asli:** hover lengket, keyboard, safe area, dan standalone dicek di HP asli atau Simulator, bukan hanya emulasi DevTools. (SK-NAT §11)

Skrip cepat untuk butir 2, 10, dan 17 (jalankan di konsol browser atau `javascript_tool` Claude Browser pane, [[FE-16 - Claude Browser Pane|FE-16]]):

```js
(() => {
  const vw = innerWidth, vh = innerHeight, out = { hscroll: document.documentElement.scrollWidth > vw, small: [], primaryInView: 0 };
  for (const el of document.querySelectorAll('a,button,[role=button],input,select,textarea,summary')) {
    const r = el.getBoundingClientRect();
    if (!r.width || !r.height || getComputedStyle(el).visibility === 'hidden') continue;
    if (r.width < 44 || r.height < 44) out.small.push(`${el.tagName}.${el.className}`.slice(0, 60) + ` ${Math.round(r.width)}x${Math.round(r.height)}`);
  }
  // tombol primer app = <button> tanpa kelas .secondary (style.css)
  for (const el of document.querySelectorAll('main button:not(.secondary):not(:disabled)')) {
    const r = el.getBoundingClientRect(); if (r.width && r.top < vh && r.bottom > 0) out.primaryInView++;
  }
  return out;
})()
```

## Pertanyaan terbuka (perlu user)
1. **Tab untuk pengguna yang sudah masuk:** tetap Home, Try, Verify, peran, Account? Atau Home, peran, Inbox, Account (Try dan Verify pindah ke lobby)? Aturan N1 terpenuhi dua-duanya; ini keputusan IA.
2. **Inbox:** sheet dari ikon app bar (usulan catatan ini) atau tab sendiri?
3. **Batas HP 720 → 600 px:** setuju dipindah? Rentang 600 – 719 px sekarang memakai layout HP; setelah dipindah memakai layout medium (L3).

## Riwayat
- 2026-10-26: dibuat dari Material 3 (breakpoints, list-detail, spacing, navigation bar, accessibility), Apple HIG (layout, tab bars, sheets, buttons, accessibility), MDN (responsive design, mobile first), dan 8 skill FE-64 – FE-72 yang dipasang hari ini.
