---
tags: [design-ref, palette, "DS-PAL"]
type: design-palette
id: DS-PAL
source_folder: ColorPalette-JitsuinFi
status: UTAMA
updated: 2026-10-20
---

# DS-PAL - Palet Utama JitsuinFi

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[FE-27 - Referensi Visual Vault|Referensi vault]]

**Palet utama JitsuinFi** (ditetapkan user 2026-10-20). Setiap referensi di `09-Design` dibandingkan dengan palet ini. Sumber gambar ada di folder vault `ColorPalette-JitsuinFi/`.

| Keluarga biru (Zcash, ruang terlindung) | Keluarga plum (manusia, tinta, segel) |
|---|---|
| ![Biru](../ColorPalette-JitsuinFi/870121ac664eba8cb65ce9d46b8dd9a1.jpg) | ![Plum](../ColorPalette-JitsuinFi/ffc1eb9c83961d47d230fd8106adc2c8.jpg) |
| `ColorPalette-JitsuinFi/870121ac664eba8cb65ce9d46b8dd9a1.jpg` (736×1308) | `ColorPalette-JitsuinFi/ffc1eb9c83961d47d230fd8106adc2c8.jpg` (736×1308) |

## 1. Sepuluh warna
| Nama | Hex resmi | RGB | CMYK (dari gambar) | Hex terukur dari swatch | Token di landing (`src/landing/tokens.css`) |
|---|---|---|---|---|---|
| Cetacean Blue | `#020D2F` | 2, 13, 47 | 96, 72, 0, 82 | `#060C2C` | `--head`, `--pool` |
| Catalina Blue | `#032C7D` | 3, 44, 125 | 98, 65, 0, 51 | `#0A2C76` | `--pool-2` |
| Absolute Zero (Crayola) | `#0841C9` | 8, 65, 201 | 96, 68, 0, 21 | `#143FBF` | `--wave` |
| Button Blue | `#1D97F1` | 29, 151, 241 | 88, 37, 0, 6 | `#3192E3` | `--glint` |
| Vodka | `#C4C7F2` | 196, 199, 242 | 19, 18, 0, 5 | `#BDBFE8` | `--mist` |
| Brown Coffee | `#461D3A` | 70, 29, 58 | 0, 59, 17, 73 | `#461D3B` | `--ink` |
| Japanese Violet | `#502A50` | 80, 42, 80 | 0, 48, 0, 69 | `#502A51` | `--ink-2` |
| Dark Raspberry | `#7E2A53` | 126, 42, 83 | 0, 67, 34, 51 | `#7F2A53` | `--seal` (dan `--seal-hi` `#6B2347`, 15% lebih gelap) |
| Pearly Purple | `#BA71A2` | 186, 113, 162 | 0, 39, 13, 27 | `#BA70A1` | `--fold` |
| Classic Rose | `#ECD0EC` | 236, 208, 236 | 0, 12, 0, 8 | `#EDD0EC` | `--fiber` |

Turunan (bukan dari gambar): `--paper` `#F6F5FC` (Vodka 14% + Classic Rose 6% di atas putih) dan `--sheet` `#FCFCFE` (Vodka 5%), lihat `jitsuinfi-frontend/MASTER.md` §2.

**Koreksi:** label hex Vodka di gambar tertulis `29B4D1`; itu salah. RGB 196, 199, 242 = `#C4C7F2`, dan swatch terukur `#BDBFE8` cocok dengan nilai RGB. Swatch biru diukur dari foto dengan latar gelap, jadi sedikit bergeser; yang dipakai adalah hex resmi.

## 2. Gaya gambar palet
- **Biru:** kartu warna di atas foto anggrek biru gelap yang buram. Judul serif kontras tinggi kapital, kode dalam sans kecil. Suasana malam, dalam, dingin.
- **Plum:** pita warna penuh selebar gambar, judul serif bergaya editorial (huruf tebal, kontras tinggi), kode dalam sans condensed. Suasana hangat, padat, seperti tinta.
- Serif kontras tinggi di kedua gambar sejalan dengan pilihan **Shippori Mincho B1** untuk display ([[FE-12 - Font Fontsource]]).

## 3. Makna (dari `MASTER.md`)
- **Biru = Zcash**: kolam terlindung yang dalam (Cetacean, Catalina), riak (Absolute Zero), cahaya dari dalam air (Button Blue), teks di atas air (Vodka).
- **Plum = manusia**: tinta tulisan (Brown Coffee, Japanese Violet), **segel jitsuin terdaftar** (Dark Raspberry, satu-satunya merah), serat dan tepi tinta (Pearly Purple, Classic Rose).
- Amendment 1: merah maroon adalah merah resmi segel pada dokumen piutang, bukan warna lembut; Classic Rose dan Pearly Purple diperkecil jadi tepi tinta dan serat. Hasilnya tegas dan profesional.

## 4. Kontras (WCAG, dihitung 2026-10-20)
| Pasangan | Rasio | Lulus |
|---|---|---|
| Cetacean di atas paper | 17.60 | AAA |
| Brown Coffee di atas paper | 12.95 | AAA |
| Catalina di atas paper | 11.68 | AAA |
| Japanese Violet di atas paper | 10.84 | AAA |
| Dark Raspberry di atas paper | 8.27 | AAA |
| Sheet di atas Dark Raspberry (teks tombol) | 8.75 | AAA |
| Absolute Zero di atas paper | 7.43 | AAA |
| Vodka di atas Cetacean | 11.62 | AAA |
| Vodka di atas Catalina | 7.71 | AAA |
| Classic Rose di atas Dark Raspberry | 6.32 | AA (AAA teks besar) |
| Button Blue di atas Cetacean | 6.13 | AA |
| Vodka di atas Absolute Zero | 4.90 | AA |
| Button Blue di atas Catalina | 4.07 | AA teks besar saja |
| Pearly Purple di atas paper | 3.25 | Dekoratif saja |
| Button Blue di atas paper | 2.87 | **Gagal**: jangan pernah di kertas |

Selisih kecil dengan angka `MASTER.md` (Button Blue di atas paper tertulis 2.58, sheet di atas seal 8.68): angka di sini dihitung ulang dari hex; perbedaannya tidak mengubah aturan.

## 5. Aturan pakai
- Warna di luar tabel ini tidak boleh; tidak ada `#000` atau `#FFF` murni.
- Satu merah saja: Dark Raspberry untuk segel, aksi utama, tanda tangan, link.
- Button Blue hanya di dalam "air" (latar biru tua) atau sebagai cincin fokus.
- Classic Rose dan Pearly Purple hanya dekoratif (serat, tepi tinta), bukan teks.

## 6. Usulan token tiga tingkat (kerangka panduan ai-design-vault)
| Tingkat 1, primitive | Tingkat 2, semantic | Pengganti di landing sekarang |
|---|---|---|
| `--raw-color-cetacean-950: #020D2F` | `--heading`, `--surface-deep` | `--head`, `--pool` |
| `--raw-color-catalina-800: #032C7D` | `--surface-deep-raised` | `--pool-2` |
| `--raw-color-absolute-zero-600: #0841C9` | `--accent-water` | `--wave` |
| `--raw-color-button-blue-500: #1D97F1` | `--focus-ring`, `--light-in-water` | `--glint` |
| `--raw-color-vodka-200: #C4C7F2` | `--foreground-on-deep` | `--mist` |
| `--raw-color-brown-coffee-900: #461D3A` | `--foreground` | `--ink` |
| `--raw-color-japanese-violet-800: #502A50` | `--foreground-muted` | `--ink-2` |
| `--raw-color-raspberry-700: #7E2A53` | `--action-primary`, `--seal` | `--seal` |
| `--raw-color-pearly-400: #BA71A2` | `--decoration-strong` | `--fold` |
| `--raw-color-rose-100: #ECD0EC` | `--decoration-soft` | `--fiber` |

Landing sekarang memakai satu tingkat (nama peran langsung berisi hex). Ini usulan, belum keputusan.

## 7. Dipakai di mana sekarang
| Permukaan | Memakai palet utama? |
|---|---|
| Landing (`index.html`, `src/landing/tokens.css`) | **Ya**, semua sepuluh warna |
| App (`app.html`, `src/style.css`) | **Ya** sejak 2026-10-20 (D-36, jitsuinfi-frontend `0cce4e8`): token landing di-import, tanpa mode gelap; status ok/menunggu/ditolak memakai Catalina, Japanese Violet, Dark Raspberry |
| Video, slide, logo | Belum ada; catat di [[VID-05 - Aset dan Lisensi]] bila dipakai |
