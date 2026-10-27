---
tags: [video, "VID-03"]
---

# VID-03 - Checklist Rekaman

**Bagian dari:** [[Video-Workspace]] · Terkait: [[VID-02 - Storyboard dan Shot List]] · [[VID-04 - Checklist Export dan Upload]]

## Checklist v3 (2026-10-27, untuk shot list v3 di [[VID-02 - Storyboard dan Shot List]])
Semua langkah di bawah dikerjakan user: passkey, HP, konsol production, wallet testnet, dan suara tidak bisa dipegang agent.

### Layar dan resolusi
- [ ] Export akhir 1920 × 1080, 30 fps, H.264 + AAC ([[VID-04 - Checklist Export dan Upload]]).
- [ ] Desktop: jendela Chrome dengan isi halaman **1440 × 810** (16:9). Cara cepat: `open -na "Google Chrome" --args --user-data-dir="$HOME/jf-video/<profil>" --window-size=1440,900 <url>` lalu rekam area halaman saja (QuickTime → File → New Screen Recording → Record Selected Portion, atau OBS crop). Layar Retina merekam 2880 × 1620, diturunkan ke 1080p saat export.
- [ ] Zoom browser **100 %** (layout dicek di 1440 dan 390 px, HNK-34.T14). Kalau teks terlalu kecil di 1080p, naikkan ke 110 % untuk `/try` dan `/verify` saja, dan cek tidak ada scroll samping.
- [ ] Bookmark bar disembunyikan (Cmd + Shift + B), tanpa ekstensi, tanpa autofill, tab lain ditutup.
- [ ] Kursor diperbesar (System Settings → Accessibility → Display → Pointer size) atau sorotan klik di editor.
- [ ] macOS Focus / Do Not Disturb aktif; notifikasi chat, email, dan wallet mati; jam menu bar boleh tampil.

### Profil dan akun uji (siapkan H-1, semua berlabel `TES-`)
| Profil Chrome | Untuk shot | Isi |
|---|---|---|
| `TES-video` | S01 – S06 | Baru dan logout (pengunjung). Buka landing sekali sebelum rekam agar figur sudah di cache, lalu tutup tab |
| `TES-supplier` (desktop) | S07, S09 | Akun supplier di `/account` dengan passkey Mac (atau "Use test data instead" bila passkey tidak memberi PRF). Kontak: buyer `TES-buyer` sudah ditambahkan lewat tautan kontak atau kartu; alamat terima advance = alamat testnet shielded milik user (jangan sampai alamat penuh tersorot lama) |
| `TES-buyer` (HP, PWA) | S07, S09 | Akun buyer dengan passkey HP (Face ID / sidik jari, harus mendukung PRF: iCloud Keychain iOS 18+ atau Google Password Manager). Kunci invoice sudah dibagikan ke supplier. Kalau HP tidak memberi PRF, app menawarkan data tes: ganti kalimat "one passkey touch signs it" di S07 |
| `TES-financier` (desktop) | S08 | Konsol production `https://jitsuinfi-console.vercel.app/console` dengan passkey user yang sudah dipasangkan (bukan konsol demo). Mandat publik 0.0001 – 1 ZEC, tenor ≤ 90 hari; mandat privat diatur sehingga invoice video mendapat cap "Fits your private mandate" |

### Data yang di-seed agar layar terlihat penuh
- [ ] H-1: jalankan dua deal `TES-INV-VID-01` (sampai settled) dan `TES-INV-VID-02` (berhenti di 印, menunggu segel) dengan profil yang sama, sehingga daftar Invoices supplier dan buyer berisi "Needs your move", "Waiting on others", dan "Settled", dan buyer punya minimal satu sertifikat riwayat.
- [ ] Deal yang direkam: `TES-INV-VID-03`, nominal kecil (mis. 0.001 ZEC, advance 0.0009), jatuh tempo 30 – 60 hari, PDF invoice uji tanpa data pribadi.
- [ ] Inbox semua profil dibersihkan ("Remove from inbox" untuk surat lama) agar hitungan lonceng tepat 1 saat S07.
- [ ] Wallet node financier production punya cukup TAZ untuk advance + biaya (cek di konsol sebelum rekam; tidak ada endpoint saldo, jadi cek lewat wallet node atau advance uji H-1).
- [ ] Wallet testnet buyer berisi TAZ untuk pelunasan; bayar lewat "Copy payment link" (ZIP-321) di wallet di luar layar.
- [ ] Papan: 55 entri per 27 Okt; `/rates` sudah menampilkan kelas 31 – 60 hari (dari `TES-INV-IDX-…`). Tidak perlu seed papan.
- [ ] Jangan reload saat mengisi Write (isian hilang saat reload, sisa HNK-34.T16) dan rekam supplier di satu perangkat saja (data per perangkat, sinkronisasi relay belum selesai).

### PWA di HP
- [ ] iPhone: Safari → `https://jitsuinfi.vercel.app/app` → tombol Share → "Add to Home Screen" → buka dari ikon (mode standalone, tanpa bar URL). Android: Chrome → menu ⋮ → "Install app".
- [ ] Rekam HP: iPhone dengan kabel ke Mac → QuickTime → File → New Movie Recording → pilih iPhone sebagai kamera (gambar bersih), atau Screen Recording dari Control Center (mikrofon mati). Android: `scrcpy --record` atau perekam bawaan.
- [ ] Focus / Do Not Disturb di HP, baterai dan sinyal tidak dalam keadaan merah.
- [ ] Di editor, tampilkan HP potret di tengah dengan latar kertas atau blur; label kecil "phone, installed app".

### Gladi dan saat rekam
- [ ] Gladi penuh satu kali (S01 – S11) dengan stopwatch; total narasi ≤ 1:58.
- [ ] Rekam tiap shot sebagai file sendiri: `Video-Workspace/assets/20261027-s04-try.mov` dan seterusnya.
- [ ] Tunggu blok direkam utuh, dipercepat saat edit dengan label "sped up".
- [ ] Catat txid deal video (entry, advance, pelunasan, settled) untuk README.
- [ ] Tidak ada seed, kunci, kode pairing / `SETUP_CODE`, tautan kontak, email, atau alamat wallet penuh yang terbaca di frame.
- [ ] Suara: ruangan tenang, mikrofon diuji, baca naskah VID-01 v3 persis.

## Checklist v2 (diganti v3)

## Lingkungan
- [ ] Profil browser bersih (tanpa bookmark, ekstensi, riwayat, atau akun pribadi).
- [ ] Notifikasi OS dan chat dimatikan (Do Not Disturb).
- [ ] Hanya wallet dan akun `TES-` yang terbuka; seed dan key tidak pernah tampil.
- [ ] Desktop dan menu bar bersih.
- [ ] Ukuran font terminal dan browser diperbesar.

## Data demo
- [ ] Invoice demo memakai ID `TES-INV-xxxx` dan nama fiktif.
- [ ] Wallet demo terdanai cukup untuk semua shot (lihat SPK-10 di [[Spikes Hub]]).
- [ ] Alur sudah dijalankan sekali penuh sebelum rekam (gladi).
- [ ] Txid yang akan tampil dicatat untuk README.

## Teknis
- [ ] Rekam layar 1920×1080, 30 fps (OBS atau QuickTime; diuji di SPK-15).
- [ ] Mikrofon diuji; ruangan tenang.
- [ ] Setiap shot direkam terpisah dengan nama file sesuai konvensi di [[Video-Workspace]].
- [ ] Waktu tunggu konfirmasi direkam utuh, lalu dipercepat saat edit (diberi label).
