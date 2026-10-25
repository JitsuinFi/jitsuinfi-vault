---
tags: [fe-tool, "FE-32", monad-blitz]
type: fe-tool
id: FE-32
layer: skill
status: TERSEDIA-BELUM-DIPAKAI
updated: 2026-10-23
---

# FE-32 - colorfigures

> **Peta link:** [[FE-00 - Peta Tools FE|Peta tools]] · [[10 - FE Vault|Hub modul]] · [[FE-01 - Batasan Platform FE|Batasan platform]]

Objek isometrik bertinta tangan, warna flat, bisa diputar; mode See-through berlabel untuk mesin.

## Akar
| | |
|---|---|
| Jenis | Skill (April Zhu) |
| Sumber | https://april-zhu.com/colorfigures |
| Pasang | `curl … | tar -xz -C ~/.claude/skills` |
| Bobot | Berat dibuat: 15–30 menit dan 200k–400k token per figur |
| Lisensi | MIT |
| Lokasi | `~/.claude/skills/colorfigures` (scope user, ikut tersedia di sesi JitsuinFi) |
| Asal catatan | Disalin dari vault Monad Blitz (`/Users/Shenhan/HansProject/MOnadBlitz/vault`), catatan FE-07 (2026-10-23) |
| Vonis di Monad Blitz | **DIPAKAI (uji 2026-10-23)**; dipakai di: — |

## Kecocokan dengan JitsuinFi
- [[FE-01 - Batasan Platform FE|FE-01]]: Output satu HTML dengan engine ter-inline, tanpa CDN; satu-satunya link keluar adalah footer kredit (matikan dengan `credit: false`). Aman untuk FE-01 setelah SVG/JS dipindah ke modul TS.

## Catatan
Dibangun di atas iso-glow, [[FE-48 - iso-figure|iso-figure]], dan [[FE-49 - Anatomy|Anatomy]]; gaya paling pas untuk mesin fotokopi berlabel, tapi terlalu mahal untuk 7 jam. Membuatnya sebelum H termasuk aset pra-event (tunggu SPK-13 - Aturan Blitz dan kriteria juri (vault Monad Blitz)).

## Review keamanan (2026-10-23)
Tarball `colorfigures.tar.gz` (76.181 byte, sha256 `b74809acd591a7f209c8ba964b0b29bb050a953328aa6577581e6778d26257ff`) diunduh ke folder sementara dan diperiksa sebelum dipasang.

| Cek | Hasil |
|---|---|
| Isi | 8 file, semua di dalam `colorfigures/` (tidak ada path keluar folder): SKILL.md, README, LICENSE, `assets/core.js`, 3 contoh, `scripts/build.py` |
| `scripts/build.py` | Hanya membaca figur + `core.js`, menyisipkan engine, menulis satu file output. Tanpa jaringan/proses/hapus |
| `assets/core.js` | Tanpa `fetch`, `eval`, storage, atau WebSocket. Satu-satunya link keluar: footer kredit "Made with Colorfigures" (bisa dimatikan dengan `credit: false`) |
| Lisensi | MIT (April Zhu; turunan iso-glow dan iso-figure) |

**Vonis: AMAN.** Terpasang di `~/.claude/skills/colorfigures` (asal tercatat di `.reviewed-commit`). Langkah Verify bawaan skill menjalankan Chrome headless berkali-kali; untuk menjaga suhu laptop, verifikasi dilakukan lewat browser pane.

## Uji: figur mesin fotokopi (2026-10-23)
- File: `Project/assets/figures/fotokopi/fotokopi.html` (sumber) → `mesin-fotokopi.html` (satu file, 91.617 byte, engine ter-inline).
- Model: plinth, cabinet + 2 laci A4, badan ungu Monad (palet custom `monad`), unit scanner + kaca, tutup berengsel (alas putih di bawahnya), panel kontrol (layar, tombol COPY), slot keluar + tray miring.
- See-through (± 30 part): rel + carriage lampu scan, carriage cermin (setengah kecepatan), lensa, CCD, unit laser + braket + sinar, drum fotokonduktor (berputar), developer roller, cartridge toner, transfer roller, heat roller (memanas) + pressure roller, rol keluar, rol pengambil + lengan, rol feed, baki + tumpukan kertas, power supply, papan utama + chip, kabel. 11 label berbahasa Indonesia yang menyala saat bekerja.
- Interaksi: Angkat tutup, Taruh dokumen, Jumlah (1/3/5), Copy!, Ambil hasil; klik tutup/dokumen/tombol COPY/tumpukan juga bekerja. Urutan salah ditangani ("Taruh dokumen di kaca dulu").
- Dicek: yaw 45, 110 (tutup terbuka), 200 (belakang), 230 (see-through + scan), 300 (sisi kanan + tray); `?press=Taruh@200,Copy@2200` → `done 1`, `stack 1`, tanpa error.
- Perbaikan saat uji: tutup ikut memudar di see-through; toner dan laser diperkecil, drum diperpanjang supaya tidak tertutup.
- Belum: tampilan HP (390 px) dan sudut bawah (`pitch` tinggi) belum dicek; integrasi ke halaman React belum.
- Catatan aturan: figur dibuat sebelum hari H (aset pra-event, ikut risiko D-12).

## Figur tambahan + gerak interaktif (2026-10-23)

| Figur | File (satu file) | Gerak interaktif | Dicek |
|---|---|---|---|
| Mesin fotokopi (diperbarui) | `Project/assets/figures/fotokopi/mesin-fotokopi.html` | Tutup berengsel, lampu scan menyapu, drum berputar, fuser memanas, kertas mengalir ke tray; **baru:** laci atas bisa ditarik + isi ulang otomatis, kertas habis (lampu oranye), **kertas macet** tiap lembar ke-4 (lampu merah berkedip, layar `JAM!`), **pintu depan berayun** memperlihatkan drum + fuser, kertas macet ditarik keluar, tombol COPY tenggelam saat ditekan | Pintu + jam, laci terbuka, alur `Copy 5 lembar` → macet di lembar 4 → buka pintu → tarik → idle (done 3, kertas 8), tanpa error |
| Printer inkjet (baru) | `Project/assets/figures/printer/printer-inkjet.html` | Tombol power/print tenggelam, carriage memeriksa rel saat dinyalakan, **flashdisk melayang lalu tercolok** di port samping (LED kedip saat membaca), pilih file (`New Folder.exe` = virus → lampu merah + ditolak), baki keluar sendiri + stopper berdiri, kertas turun dari baki belakang, **carriage CMYK bolak-balik** sambil baris tinta muncul di kertas, cover terbuka → carriage ke tengah, **ganti tinta** (kartrid terangkat lalu turun), tinta dan kertas berkurang | Tampak depan, cover terbuka (yaw 20), see-through saat cetak; alur Nyalakan → Colok → Pilih file → Print → `printed 1`, tinta 92%, kertas 19 |
| Laminator (baru) | `Project/assets/figures/laminator/laminator-a4.html` | Saklar rocker, lampu READY berkedip lalu hijau saat suhu naik (25 → 110/130 C), **dial ketebalan berputar**, pouch (ijazah/KTP/menu) ditarik **rol silikon yang berputar** dengan roda gigi + motor, pemanas menyala, hasil **mengilap** atau **keruh bergelombang** bila dial terlalu rendah, tombol **ABS** memundurkan pouch, pouch baru muncul setelah hasil diambil, pouch otomatis masuk saat READY bila ditekan lebih awal | Tampak depan, see-through saat jalan, hasil gagal (ijazah 125 mic di dial 80), alur dari keadaan mati → auto-feed, tanpa error |

Semua dicek lewat browser pane (bukan Chrome headless berulang). Belum: tampilan HP, sudut bawah, dan integrasi ke halaman React.

## Status
TERSEDIA BELUM DIPAKAI (untuk JitsuinFi).
