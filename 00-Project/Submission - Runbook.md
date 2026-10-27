---
tags: [project, submission, runbook]
updated: 2026-10-27
---

# Submission - Runbook

**Bagian dari:** [[00 - Project]] · Item: HNK-14.T4 di [[Backlog]] · Terkait: [[Submission - Deskripsi]] · [[Submission - Checklist Publikasi Repo]] · [[VID-01 - Naskah 2 Menit]] · [[VID-02 - Storyboard dan Shot List]] · [[VID-03 - Checklist Rekaman]] · [[VID-04 - Checklist Export dan Upload]] · [[ZECATHON - Aturan dan Deadline]]

> Disusun 2026-10-27 oleh agent. Agent **tidak** men-submit, tidak membuka repo, dan tidak mengunggah apa pun. Deadline: **28 Okt 2026 23:59 UTC = 29 Okt 06:59 WIB**. Target internal: 27 Okt.

## Yang harus dikerjakan user (urut)
1. **Review deskripsi v3** di [[Submission - Deskripsi]] (1.978 karakter) dan setujui atau ubah (D-35: Hans me-review).
2. **Perbarui README `jitsuinfi-zcash`** dengan tabel txid production (teks siap tempel di [[Submission - Checklist Publikasi Repo]] bagian 2), atau minta agent mengerjakannya di sesi kode. Tanpa ini, kalimat "Full txids in the README" di deskripsi tidak benar. Baris README lain yang usang ada di catatan yang sama.
3. **Konfirmasi** bahwa `jitsuinfi-frontend` dan `jitsuinfi-backend` memang sengaja sudah PUBLIC, lalu catat di [[Decision Log]] (hanya node yang tercatat, D-53).
4. **Rekam video** sesuai [[VID-02 - Storyboard dan Shot List]] v3 dan [[VID-03 - Checklist Rekaman]] v3 (passkey, HP, konsol production, wallet testnet, suara). Edit ≤ 2:00, export, unggah.
5. **Buka `jitsuinfi-zcash` ke publik** setelah butir 2 (Settings → Danger Zone → Change visibility → Public). Waktu diputuskan user; paling lambat sebelum Submit.
6. **Login di `https://thezecathon.com`** (Sign in → Submit project) dan cocokkan field form dengan tabel di bawah. Form ada di balik login, jadi agent belum bisa membacanya; daftar field berasal dari catatan vault.
7. Jalankan **checklist akhir** di bawah, isi form, **Submit**, lalu jangan simpan draft lagi.

## Halaman resmi
- Situs: `https://thezecathon.com` (dibaca 2026-10-27 dengan WebFetch saat logout). Isinya hanya menyebut bahwa "the submission form are all inside" setelah Sign in, akun "GitHub, Google or email", dan submission tersegel sampai penjurian. Link di halaman: RULES, RESOURCES, REGISTER, SIGN IN, SUBMIT PROJECT, YOUR ACCOUNT.
- Aturan dan field tersalin di `../Info/` dan [[ZECATHON - Aturan dan Deadline]]. SPK-12 (pertanyaan ke organizer soal alamat payout dan format video) tidak pernah dijawab, jadi kedua hal itu dicek langsung di form.
- Bantuan organizer: `bladet928@gmail.com` (dari halaman resmi).

## Field form dan isian persis
| Field (menurut vault) | Isi | Catatan |
|---|---|---|
| Nama proyek | `JitsuinFi` | Nama yang sama di landing, app, repo |
| Track (tepat satu) | **Private Markets** | D-40; "the price should be public and the participants should not" |
| Deskripsi (≤ 2.000 karakter) | Blok "Draf v3" di [[Submission - Deskripsi]], disalin tanpa pagar ``` | 1.978 karakter; hitung lagi bila diubah |
| Repo | `https://github.com/JitsuinFi/jitsuinfi-zcash` | Repo inti (crate, CLI `jitsuin verify`, spesifikasi, txid). Bila form menerima beberapa repo, tambahkan `https://github.com/JitsuinFi/jitsuinfi-node`, `https://github.com/JitsuinFi/jitsuinfi-frontend`, `https://github.com/JitsuinFi/jitsuinfi-backend`. Bila hanya satu dan boleh org: `https://github.com/JitsuinFi` hanya setelah zcash publik |
| Demo URL (wajib, harus jalan) | `https://jitsuinfi.vercel.app` | Landing dengan tombol "Open the demo" ke `/app`. Alternatif bila juri sebaiknya langsung masuk app: `https://jitsuinfi.vercel.app/app`. Konsol demo disebut di deskripsi |
| Video dua menit (wajib) | Tautan video (lihat "Unggah video") | Format dan host dicek di form |
| Checkbox repo publik | Centang **hanya setelah** `jitsuinfi-zcash` publik dan terbuka saat logout | Aturan "open source at submission" |
| Alamat payout shielded (bila ada) | Alamat **mainnet** shielded (unified address) dari wallet milik pendaftar | FAQ menyebut hadiah dibayar ke alamat shielded yang diberikan saat submission; vault mencatat form tidak punya field ini. Bila tidak ada, tanyakan organizer setelah submit |
| Nama / akun pendaftar | Akun yang mendaftar (satu orang, hadiah ke akun itu) | Satu submission per akun dan per tim |

Jangan menulis alamat wallet testnet, kode pairing, `SETUP_CODE`, tautan kontak, atau email tim di field mana pun.

## Unggah video
1. Export sesuai [[VID-04 - Checklist Export dan Upload]]: mp4 H.264 1080p 30 fps, AAC, ≤ 2:00 dicek di player, label "sped up", subtitle disarankan.
2. Bila form menerima unggahan file: unggah mp4 langsung. Bila form meminta tautan: YouTube **Unlisted** (atau Public), judul `JitsuinFi: private invoice financing without double financing (ZECATHON 2026, Private Markets)`, deskripsi video berisi tiga tautan (landing, konsol demo, repo zcash). Matikan iklan dan komentar bila bisa.
3. Buka tautan video di jendela private / perangkat lain saat logout: harus bisa diputar, durasi ≤ 2:00, 1080p tersedia.
4. Tempel tautan di form.

## Checklist akhir sebelum Submit
Semua dicek di jendela private (logout), lalu satu kali di HP.

**Tautan**
- [ ] `https://jitsuinfi.vercel.app` terbuka; hero berjalan; "Open the demo" membuka `/app`.
- [ ] `https://jitsuinfi.vercel.app/app`, `/try`, `/verify`, `/outsider`, `/rates` terbuka tanpa error di console (2026-10-27: semua HTTP 200).
- [ ] `https://jitsuinfi-console-demo.vercel.app/console` terbuka (2026-10-27: 200).
- [ ] `https://github.com/JitsuinFi/jitsuinfi-zcash` terbuka saat logout (2026-10-27: **404, masih private**); `jitsuinfi-node`, `jitsuinfi-frontend`, `jitsuinfi-backend` terbuka.
- [ ] Tautan video bisa diputar saat logout.

**Demo jalan**
- [ ] `/try`: "Offer it to financier B" sesudah ubah nominal → 偽; sesudah "Put back the original" → 重 dari papan live (bukan "saved board").
- [ ] Konsol demo: "Create a passkey to try it" (tanpa undangan) → masuk → In-tray dan daftar deal tampil, label "Demo node · nothing here moves money".
- [ ] `/verify` dengan contoh: "Use Case File #0417's Exhibit A" → "Hand it to the registry" → 重 "Double signature on the board", Entry ① dan ② berposisi di papan.
- [ ] `/verify` dengan bundle: tempel isi `jitsuinfi-zcash/examples/testnet/e2e-tes-inv-e2e1/bundle.txt` → "Hand it to the registry" → registrasi sekali dan settled terlihat (atau bundle deal video dari "Check it on Verify" → 真).
- [ ] `/rates` menampilkan kelas 31 – 60 hari; `/outsider` menampilkan palang sensor dan pita papan.
- [ ] HP: `https://jitsuinfi.vercel.app/app` → Add to Home Screen → buka dari ikon → tab bar tampil, tanpa scroll samping.
- [ ] Node production menjawab: `https://jitsuinfi-console.vercel.app/node/board` (2026-10-27: 55 entri, tip 4547249).

**Repo dan rahasia**
- [ ] Keempat repo publik; lisensi ganda MIT / Apache-2.0 ada (sudah, 2026-10-27).
- [ ] README zcash berisi tabel txid production dan langkah verifikasi juri (lihat checklist publikasi).
- [ ] Pindai rahasia ulang hanya bila ada commit baru sesudah 2026-10-27 (pola dan cara di [[Submission - Checklist Publikasi Repo]] bagian 3). Hasil 2026-10-27: bersih.
- [ ] Tidak ada seed, kunci, kode pairing, tautan kontak, email, atau alamat wallet penuh di video dan deskripsi.

**Form**
- [ ] Track = Private Markets; deskripsi ditempel dan dihitung ulang ≤ 2.000; demo URL, repo, video, checkbox publik terisi.
- [ ] Tekan **Submit**. **Jangan menyimpan draft setelah Submit** (status submitted ditarik kembali). Edit masih bisa sampai deadline, tetapi setiap edit harus diakhiri Submit lagi.
- [ ] Cek status "submitted" dari perangkat lain; simpan tangkapan layar dan waktunya di [[ES-HNK-14 - Submission video deskripsi dan demo URL]], lalu tandai HNK-14.T4 di [[Backlog]].

## Setelah submit
- Jangan mengubah demo URL, menghapus deploy, atau mematikan node / relay sampai penjurian selesai (29 Okt – 22 Nov). Risiko host pihak ketiga: W-23 (`/try` dan `/verify` tetap jalan dengan papan tersimpan).
- Juri diumumkan 29 Okt 16:00 UTC; pemenang 23 Nov.
