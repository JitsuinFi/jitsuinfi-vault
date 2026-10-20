---
tags: [design-ref, "DS-09"]
type: design-ref
id: DS-09
source_file: refero.design 31fd7d97-406b-497e-9f25-bb9a595cc0e2.jpg
kind: landing-page
mode: persuade
updated: 2026-10-20
---

# DS-09 - ROX Landing Dark Gold

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]] · [[FE-21 - Refero|Refero]]

![DS-09](refero.design%2031fd7d97-406b-497e-9f25-bb9a595cc0e2.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/refero.design 31fd7d97-406b-497e-9f25-bb9a595cc0e2.jpg`, 2732×11872 (tangkapan satu halaman penuh, skala 2×) |
| Sumber | Refero (nama file memuat UUID layar Refero `31fd7d97-406b-497e-9f25-bb9a595cc0e2`); situs ROX, "Revenue Agents" |
| Catatan pasangan | `09-Design/rox.md` ada tetapi **kosong** |
| Mode | **Persuade** (landing B2B enterprise) |
| Cara dibaca | Dipotong jadi 8 segmen 1500 px, dibaca berurutan |

## 2. Yang terlihat (apa adanya, urut dari atas)
1. **Nav pill bergaris:** logo bintang empat + "ROX", Customers, Products ▾, Pricing, Company ▾; "Log In" (garis abu), "Try Now" (garis emas + lingkaran panah).
2. **Hero tengah:** serif "Revenue Agents for the **Global 2000**" (kata akhir emas); tagline "Warehouse Native | Pre-Built Agents | Revenue outcomes in 90 Days"; dua tombol "Contact Sales" (emas) dan "Try Now". Latar: busur lingkaran konsentris tipis. Di bawah: **mockup aplikasi miring 3D** (tablet dengan sidebar Agents/Workflows, perintah "Generate an outreach campaign for @NVIDIA Corporation…", kotak "Thinking" dengan progres, daftar langkah dengan chip alat) dan ponsel di kiri.
3. **Strip logo** "AI Transformation Partner to the Best": Snorkel, Webflow, hightouch, bynder, groq; logo di tepi memudar.
4. **Bingkai grid terlihat:** garis tipis membagi section, titik bintang kecil di persilangan.
5. "**Grow Revenue**" (serif emas, kiri) + paragraf abu (kanan).
6. "**Consolidate your legacy SaaS workflows**": akordeon kiri (Sales Engagement terbuka dengan garis emas, lalu Sales Enrichment, Revenue Intelligence, Conversation Intelligence, Command, Recommended Actions); kanan: **alur langkah** "Step 1: Agent Generated, New Thread" → jeda "3 days" → "Step 2 … Reply" → "3 days" → "Step 3: Automatic Email" dengan isi email.
7. "**Transforming** enterprise revenue" (dua warna: emas dan putih).
8. **Testimoni:** "90% reduction in rep prep time", kutipan serif "I close more when I use ROX. That's the bottom line.", "Max Freeman, VP of Sales", tombol "Read The Full Case Study"; tab logo (ramp aktif emas, wsp, SCAI); potret video dengan berkas cahaya hangat, tombol putar bergaris emas.
9. "**Enterprise Ready**" + tiga kolom bernomor (`01`, `02`, `03` dalam lencana emas): ilustrasi **garis isometrik** (kotak perangkat, piringan dengan kunci, gedung) untuk "Integrates with your existing stack", "Compliant with Security Standards", "Enterprise Deployment & Training On Us".
10. "**Revenue OS**": tumpukan lapisan isometrik meledak (lima pelat + empat sumber data di bawah), daftar lapisan di kiri (Application, Agent Swarm™, Layer, System of Context, **✦ Data Sources** aktif emas), teks kanan "Any source, format or cloud — Unified data from all public and private sources."
11. **CTA penutup:** "No need to wait." + "Contact Sales", "Start Now".
12. **Footer:** logo, kolom Products, Solutions, Resources, About, Terms and policies, Social Media; **sakelar tema** (sistem, terang, gelap); globe wireframe pudar; alamat dan hak cipta.

## 3. Style
- **Gelap mewah:** hitam `#0F0F0F` + putih + **emas pucat** `#DCC1A1`; abu `#898989` untuk teks kedua.
- **Serif display ringan kontras tinggi** untuk judul (gaya editorial), sans netral untuk isi.
- **Garis konstruksi terlihat** (grid section, titik bintang di persilangan, busur konsentris): kesan cetak biru.
- **Ilustrasi garis isometrik** emas dan abu, tanpa isian warna.
- Tombol pill bergaris, tanpa isian; satu tombol emas per kelompok.

## 4. POV dan komposisi
- **Halaman:** satu kolom terpusat dengan bingkai grid 12 kolom yang terlihat; ritme kiri-judul / kanan-paragraf berulang.
- **Mockup produk:** sudut pandang miring (perspektif 3D) agar terasa "nyata dan dalam".
- **Ilustrasi:** sudut isometrik murni (tanpa titik hilang): netral, teknis, seperti gambar arsitek.
- Kepadatan rendah, banyak ruang hitam; setiap section punya satu ide.

## 5. Makna
- **Kepercayaan enterprise**: hitam = serius, emas = premium dan pendapatan, serif = institusi.
- **Garis konstruksi dan isometrik = sistem yang direkayasa dengan teliti**, bukan sekadar AI ajaib.
- **Tumpukan lapisan = arsitektur yang bisa dipahami** dari data sampai aplikasi.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#0F0F0F` | Latar halaman (±91%) | `--raw-color-neutral-975` → `--background` |
| `#1E1D1B` | Panel dan kartu | `--surface-raised` |
| `#232323` | Garis grid section | `--border-subtle` |
| `#FFFFFF` | Judul utama | `--foreground` |
| `#DCC1A1` / `#D8C2A9` | Kata kunci judul, garis tombol utama, lencana nomor | `--raw-color-gold-200` → `--accent`, `--action-primary-border` |
| `#898989` | Paragraf dan menu | `--foreground-muted` |

Kontras: emas `#DCC1A1` di atas `#0F0F0F` ±11:1; abu `#898989` ±5.7:1 (cukup).

## 7. Tipografi
- Judul: serif display ringan kontras tinggi (mirip Canela atau Tobias; tidak terverifikasi), ±48 – 56 px, dua warna dalam satu judul.
- Isi: sans netral (mirip Inter), ±18 px abu.
- Label kecil emas di atas kutipan ("90% reduction…") sebagai eyebrow.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Nav pill bergaris | Navigasi + dua CTA | CTA utama emas dengan lingkaran panah |
| Hero serif terpusat + mockup miring | Janji + bukti produk | Mockup memotong tepi bawah |
| Strip logo memudar | Bukti sosial | Tepi kiri dan kanan memudar |
| Grid konstruksi | Struktur halaman terlihat | Titik bintang di persilangan |
| Akordeon + alur langkah | Fitur + cara kerja | Jeda waktu "3 days" di antara langkah |
| Testimoni dengan tab logo + video | Bukti pelanggan | Tab logo memilih kisah |
| Fitur bernomor dengan ilustrasi isometrik | Tiga jaminan | Lencana `01` – `03` |
| **Tumpukan lapisan meledak** | Arsitektur produk | Daftar lapisan kiri menyorot lapisan aktif |
| Footer dengan sakelar tema | Navigasi lengkap + tema | Sistem, terang, gelap |

## 9. Gerak yang tersirat
- `Inview`: judul serif muncul per kata; garis grid tergambar; ilustrasi isometrik tergambar garis demi garis.
- `Handle`/scroll: tumpukan lapisan "Revenue OS" meledak dan menyorot lapisan sesuai posisi gulir.
- `SpringTrigger`: akordeon membuka; alur langkah berganti sesuai item.
- `Hover`: lingkaran panah pada tombol bergeser; logo memudar masuk.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| **Tumpukan lapisan meledak** | "Cara kerja" JitsuinFi: perangkat dan passkey → jitsuin-wasm → relay → papan publik di chain Zcash → pool terlindung; daftar lapisan menyorot sesuai gulir |
| **Ilustrasi garis isometrik** | Persis jenis figur **hairline** (33 figur garis isometrik, sudah terpasang, belum dipakai: [[FE-11 - hairline]]) |
| Garis konstruksi dan grid terlihat | Sejalan dengan papan publik "bergaris seperti buku besar" di `MASTER.md` |
| Serif display + sans isi | Sejalan dengan Shippori Mincho B1 + Geist |
| Alur langkah dengan jeda waktu | Alur deal: tanda tangan → (jatuh tempo) → pelunasan; jumlah konfirmasi sebagai jeda |
| Satu warna aksen hangat di atas netral | Peran sama dengan Dark Raspberry (segel) di atas kertas |
| Sakelar tema di footer | App punya mode gelap; landing satu dunia (siang) |

| Bertentangan | Alasan |
|---|---|
| Strip logo pelanggan dan testimoni bernama | JitsuinFi belum punya pelanggan; mengarang logo atau testimoni tidak boleh |
| Emas `#DCC1A1` dan dunia gelap penuh | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]]; landing berkomitmen pada kertas siang |
| Mockup produk dengan nama perusahaan nyata (NVIDIA) | Merek pihak lain |
| Kartu bergaris di bagian fitur | Landing melarang kartu; ilustrasi bisa berdiri tanpa kotak |

## 11. Pertanyaan terbuka
- `rox.md` mau diisi apa? Catatan ini bisa jadi isinya.
- Tumpukan lapisan meledak dipakai untuk bab "cara kerja" di landing, dengan figur hairline?
