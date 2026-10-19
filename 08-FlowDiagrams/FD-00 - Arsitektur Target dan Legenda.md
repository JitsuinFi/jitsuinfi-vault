---
tags: [flow, architecture]
status: DRAF
updated: 2026-10-19
---

# FD-00 - Arsitektur Target dan Legenda

**Bagian dari:** [[08 - FlowDiagrams]] · Kembali: [[START-HERE]] · Terkait: [[Arsitektur JitsuinFi]] · [[Desain Jitsuin Seal]] · [[Format Data]] · [[Threat Model]] · [[Decision Log]]

> Dibuat 2026-10-19 atas permintaan user: halaman internal web app sekarang baru simulasi (salin-tempel kode antar tab, tanpa login, tanpa peran). Folder ini menggambarkan **bagaimana seharusnya** JitsuinFi berjalan end to end, dari auth sampai pelunasan, dan menandai mana yang **sudah ada** di kode dan mana yang **usulan**. Usulan P-xx di bawah belum diputuskan; tiap usulan perlu jawaban Hans sebelum dibangun (D-29: pekerjaan baru diutamakan untuk Dex dan Dave).

## 1. Status yang dipakai di semua diagram

| Tanda | Arti | Contoh |
|---|---|---|
| **ADA** | Kode ada di repo dan teruji (unit test atau testnet) | `jitsuin-flow::financier::Flow`, `buyerSignInvoice` di `jitsuin-wasm` |
| **PARSIAL** | Inti ada (core, flow, wasm), tapi layar, API, atau integrasinya belum | Supplier menandatangani entri register: fungsi wasm ada, kartu di layar supplier belum |
| **USULAN** | Belum ada; desain target yang perlu keputusan | Kotak surat terenkripsi (P-04) |

Di sequence diagram, catatan hijau = ADA, kuning = USULAN, biru = PARSIAL. Di DFD, proses atau penyimpanan bergaris putus-putus kuning = USULAN.

## 2. Notasi DFD

DFD memakai notasi gaya Gane–Sarson dengan garis siku (PlantUML `linetype ortho`):

| Bentuk | Arti |
|---|---|
| Kotak biru tebal | Entitas eksternal (orang atau sistem di luar JitsuinFi) |
| Kotak sudut membulat merah | Proses (bernomor: 1.0, 1.1, …) |
| Kotak abu-abu berawalan `D` | Penyimpanan data |
| Teks di tengah garis (`F…`) | Aliran data; detailnya di tabel aliran di bawah tiap diagram |

Aliran data selalu bernomor (`F1`, `F1.3`, `F2.4.1`, …) supaya garis tidak dipenuhi teks. Arti lengkap tiap aliran ada di tabel di bawah diagram.

## 3. Komponen target

| Komponen | Isi | Status | Repo |
|---|---|---|---|
| Web app | Halaman per peran, statis, CSP same-origin, tanpa CDN | PARSIAL (layar simulasi, HNK-10) | `jitsuinfi-frontend` |
| `jitsuin-wasm` | Semua kriptografi di browser: invoice, tanda tangan, seal, kuitansi, sertifikat, verifikasi bundel, bukti, riwayat | ADA | `jitsuinfi-zcash/crates/jitsuin-wasm` |
| Authenticator passkey | Platform authenticator (iCloud Keychain, Google Password Manager, kunci keamanan) dengan ekstensi WebAuthn PRF | ADA untuk buyer (`src/lib/passkey.ts`); peran lain USULAN | perangkat pengguna |
| Relay dokumen | Kotak surat terenkripsi end-to-end antar pihak + endpoint snapshot papan | USULAN (P-04, P-06) | `jitsuinfi-backend` (D-17) |
| Node financier | `jitsuin-flow` (state machine, watchdog) + wallet `zcash-devtool` (spending key) + key financier + API untuk konsol financier | PARSIAL: flow ADA, API HNK-05.T3 belum | `jitsuinfi-zcash` + backend financier |
| Pemindai papan | Wallet watch-only dengan UFVK papan (D-11 usulan): `scan`, `lookup`, `settled`, `rate_index` | ADA | `jitsuin-board` |
| `jitsuin` CLI | `jitsuin verify`, `jitsuin index` untuk juri dan auditor | ADA (PR #4, #6) | `jitsuin-cli` |
| lightwalletd | `zec.rocks` (D-12) | eksternal | — |
| Zodl | Wallet pengguna: menerima advance (supplier), membayar QR ZIP-321 (buyer) | eksternal, opsional (D-15, SPK-04) | — |

## 4. Usulan yang perlu keputusan

| ID | Usulan | Alasan | Dampak |
|---|---|---|---|
| P-01 | **Akun = passkey.** Tanpa email, password, OTP, atau akun di server. Daftar = membuat passkey; masuk = meminta output PRF. Identitas bisa dibangun ulang hanya dari passkey (uji "stateless": localStorage dikosongkan atau perangkat baru, key tetap sama) | Pola Mera / WebAuthn PRF ([[Desain Jitsuin Seal]] §9); server tidak menyimpan apa pun yang bisa dibocorkan | Halaman login dan daftar baru; tidak ada database pengguna |
| P-02 | **Satu salt per peran dan kegunaan:** `jitsuin/buyer/master/v1` (sudah dipakai), `jitsuin/supplier/master/v1`, `jitsuin/financier/operator/v1`, `jitsuin/<peran>/inbox/v1`. Satu orang boleh memegang beberapa peran; key tiap peran terpisah, sehingga aturan `SelfApproval` tetap berlaku | Satu passkey, banyak key terisolasi | Pilihan peran setelah masuk; key tiap peran berbeda |
| P-03 | **Key per invoice supplier diturunkan dari master supplier dan `invoice_id`** (keyed BLAKE2b, pola sama dengan key buyer), menggantikan key acak + unduh JSON plaintext | Menutup temuan pra-review TM #10 (secret diunduh plaintext) | Fungsi baru di `jitsuin-core` dan `jitsuin-wasm` |
| P-04 | **Relay dokumen = kotak surat end-to-end.** Dokumen deal (invoice, tanda tangan, entri, surat, seal, sertifikat, memo advance) dienkripsi di browser untuk kunci kotak surat penerima (X25519 dari salt inbox + AEAD). Server hanya menyimpan ciphertext, id kotak surat, dan masa simpan (misalnya 30 hari) | Menggantikan salin-tempel; server tidak bisa membaca isi deal | Repo `jitsuinfi-backend` (Railway), endpoint `POST/GET /mailbox` |
| P-05 | **Key financier tinggal di node financier**, bersama spending key wallet. Operator masuk ke konsol node dengan assertion passkey (WebAuthn standar, diverifikasi node) | Watchdog harus menandatangani `settled` otomatis begitu pembayaran ditambang (D-23); advance memo dibangun di node | API HNK-05.T3 memakai sesi dari assertion passkey |
| P-06 | **Endpoint snapshot papan** di relay: hasil `scan` dengan UFVK papan (D-11) sebagai JSON `[{txid, height, tx_index, output_index, memo}]`. Browser memverifikasi sendiri; kelengkapan snapshot tetap kepercayaan pada relay, jadi verifikasi yang menentukan memakai `jitsuin verify` | wasm tidak punya I/O jaringan; temuan pra-review Spec #23 | Satu endpoint baca-saja; tanpa data pengguna |
| P-07 | **Sesi:** key hanya di memori tab; terkunci setelah 15 menit idle atau tab ditutup. Setiap seal (印) meminta passkey ulang dengan user verification: satu sentuhan = satu stempel | Tanda tangan adalah tindakan hukum (Pasal 613 KUHPerdata untuk surat pengalihan) | Pola UX konsisten di semua peran |
| P-08 | **Salt komitmen financier dibuat library** (CSPRNG 32 byte per deal), tidak pernah diisi pengguna | Temuan pra-review TM #7 | Perubahan kecil di `jitsuin-flow` dan `jitsuin-wasm` |
| P-09 | **Indeks invoice buyer `k` dihitung otomatis** dari rantai sertifikat buyer sendiri (disimpan terenkripsi di kotak suratnya), bukan diketik | Salah ketik `k` merusak rantai riwayat | Layar buyer |
| P-10 | **Anggota dana tidak pernah mengirim UFVK ke server.** Pemindaian dengan UFVK berjalan di CLI lokal anggota; halaman anggota hanya membaca hasil pindaian lokal | UFVK membuka semua nominal dana (Threat Model) | Halaman HNK-15.T3 menerima snapshot lokal |

## 5. Apa yang tidak berubah

- Semua aturan protokol di [[Format Data]] dan [[Desain Jitsuin Seal]]: N, entri papan, seal berantai, Sign-to-Pay, `settled` dua tanda tangan, rantai riwayat, bukti tanda tangan ganda.
- Uang hanya bergerak di pool shielded; papan hanya menerima memo.
- Tidak ada smart contract, TEE, CDN pihak ketiga, atau AI sebagai hakim (D-05, D-23).
