---
tags: [fe-tool, "FE-11"]
type: fe-tool
id: FE-11
layer: library-ilustrasi
status: TERPASANG-TIDAK-DIPAKAI
updated: 2026-10-20
---

# FE-11 - hairline

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

33 figur garis isometrik yang bereaksi ke pointer.

## Akar
| | |
|---|---|
| Paket | `@lucasmarkes/hairline` 0.5.1 (MIT, https://hairline.lucasmarkes.com, repo https://github.com/lucasmarkes/hairline) |
| Asal permintaan | Daftar tool di [[Landing Page - Brief]] |
| Dipasang | Commit frontend `7fd1e49` (landing: design system MASTER.md, bab 1) |
| Rencana | `MASTER.md` §1 "Allowed patterns": figur garis hairline untuk dokumen |
| Klon referensi | `PortoWeb/_resources/repos/hairline` (commit `37d2e78`, 2026-10-14) |
| Catatan lengkap | `PortoWeb/_resources/notes/hairline.md` (API, 33 figur, tema, ukuran bundle, gotcha, skill `hairline-create` dan `hairline-adopt`) |
| Contoh pakai yang sudah jalan | PortoWeb `client/src/components/fx/hairline.tsx`: import vanilla per figur, dimuat saat figur 400 px dari viewport, satu loop frame yang tidur di luar layar |

## Temuan audit 2026-10-20
- **Tidak di-import di file mana pun** di `src/`, `index.html`, atau `app.html`. Paket ada di `dependencies` dan `node_modules`, tetapi tidak masuk bundle.
- Figur dokumen di landing sekarang digambar sendiri (SVG dan canvas).

## Cara pakai (dari catatan PortoWeb)
- API fungsi untuk DOM apa pun: `terrain(el, { play: true })` mengembalikan `Figure` dengan `update({ intensity })` dan `destroy()`. Cocok untuk vanilla TS JitsuinFi; varian React tidak perlu.
- **Ukuran:** import vanilla bernama satu figur ±7 kB brotli; semua 33 figur ±46 kB brotli. Varian React menarik ke-33 engine walau hanya satu komponen dipakai.
- Hanya `phosphor` dan `slow` yang bergerak sendiri; figur lain diam sampai ada pointer, atau berjalan dengan `play`. `riffle` satu-satunya yang menerima keyboard.

## Figur yang relevan dengan JitsuinFi
| Figur | Gambar | Calon pemakaian |
|---|---|---|
| `vault` | Pintu brankas, dial, tiga baut | Pool terlindung, dana shielded |
| `padlock`, `lockers` | Gembok; dua belas loker, satu terbuka | Privasi, data yang hanya terbuka untuk pemiliknya |
| `exploded` | Jendela aplikasi dalam empat lapisan | "Cara kerja" berlapis (bandingkan [[DS-09 - ROX Landing Dark Gold]]) |
| `relay` | Hub dengan empat cabang tile | Relay dokumen (HNK-23) |
| `settle` | Dua belas tile miring mengelilingi hub | Pelunasan dan entri `settled` |
| `hub` | Hub dengan delapan tile pada garis putus | Papan publik dengan banyak entri |
| `branches` | Graf commit bercabang dan menyatu | Riwayat buyer, rantai sertifikat |
| `loupe` | Kaca pembesar di atas lembar bergaris | Verify, auditor membaca bukti |
| `drawer` | Lemari arsip tiga laci | Dokumen deal di perangkat (HNK-24.T3) |
| `sieve` | Tiga saringan di atas wadah | Deteksi pembiayaan ganda (yang tersaring) |

## Pilihan tindak lanjut
1. Pakai: cocok untuk ilustrasi dokumen di layar app (HNK-21, Dex) atau bab landing.
2. Hapus dari `package.json` bila tidak dipakai sampai submit (perlu izin user).

## Status
TERPASANG, BELUM DIPAKAI.
