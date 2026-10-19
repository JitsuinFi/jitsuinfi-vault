---
tags: [architecture, review]
---

# Pra-review Spesifikasi dan Threat Model

**Bagian dari:** [[Backlog]] · Untuk: HNK-12.T3 (review teknis spesifikasi) dan HNK-11.T3 (review kebocoran Zcash) · Terkait: [[Threat Model]] · [[Format Data]] · [[Desain Jitsuin Seal]] · [[Decision Log]]

> Disiapkan 2026-10-19 oleh agent (dua pemeriksa terpisah, hanya baca, kode dicocokkan baris per baris). **Ini bukan review-nya.** HNK-11.T3 dan HNK-12.T3 tetap direview Hans sendiri (DEV-11): Hans memutuskan tiap temuan (terima, tolak, tunda) di kolom Keputusan. Path kode relatif ke `jitsuinfi-zcash/crates/` kecuali disebut lain. Temuan bertanda ✔ sudah dicek ulang langsung di kode oleh agent utama.

Dokumen yang diperiksa: `jitsuinfi-zcash/docs/zip-shielded-receivable-registry.md` (spesifikasi, "Spec L…") dan [[Threat Model]] ("TM L…").

## Perlu keputusan Hans dulu

1. **Griefing riwayat buyer (Spec #1) ✔.** Cek penerus (`jitsuin-board/src/history.rs:158-163`) menghitung **semua** entri `0x03` dengan tag berikutnya, bertanda tangan atau tidak (`tagged`, baris 168-172). Verifier tidak bisa memeriksa tanda tangannya karena key supplier invoice berikutnya belum diketahui. Akibatnya siapa pun yang tahu `identity_pk` (tag pertama) atau pernah menerima rantai sertifikat (tag berikutnya) bisa memposting satu entri palsu dan membuat riwayat buyer selalu ditolak (`UndisclosedSuccessor`). Ini bertentangan dengan Spec "Griefing: ... griefers only add noise". Opsi: (a) penerus menjadi peringatan, bukan kegagalan, plus buyer bisa membantah; (b) tag berikutnya diikat ke sesuatu yang hanya buyer yang punya (misalnya ditandatangani identity key buyer di entri); (c) dokumentasikan sebagai batasan yang diketahui.
2. **Salt komitmen financier (TM #7) ✔.** Salt diterima dari pemanggil tanpa cek entropi atau keunikan (`jitsuin-flow/src/supplier.rs:20`, `jitsuin-wasm/src/api.rs:422`). Salt dipakai ulang: komitmen sama untuk financier sama (portofolio terhubung). Salt lemah: bisa ditebak terhadap allowlist financier yang kecil. Usul: library membuat salt 32 byte CSPRNG sendiri.
3. **Tor (TM #2) ✔.** TM L36 menyebut `zcash-devtool --connection tor` sebagai mitigasi, tetapi wrapper tidak pernah meneruskan flag itu (`jitsuin-wallet/src/lib.rs:121-127`) dan `jitsuin-board/src/lwd.rs` memanggil lightwalletd langsung. Ditambah TM #1: operator lightwalletd melihat IP yang menyiarkan entri papan, dan karena viewing key papan publik, ia bisa membuka entri itu. Pilih: implementasikan, atau ubah klaim menjadi "belum diimplementasikan".
4. **OVK dan alamat supplier di dana (TM #4, belum pasti).** Kalau `zcash-devtool` mengirim dengan OVK akun (perlu dicek dengan `list-tx` di wallet UFVK-saja), anggota dana yang memegang UFVK melihat alamat penerima advance (alamat shielded supplier). TM L22 menyatakan anggota tidak melihat supplier.
5. **Nama jaringan "NU7, Ironwood" (Spec #22, TM #8).** Tidak bisa dibuktikan dari kode; dipakai di spesifikasi, README, deskripsi submission, dan halaman orang luar. Hans mengonfirmasi penamaan dan semantik pool.

## Threat model (HNK-11.T3)

| # | TM | Klaim | Kenyataan | Tingkat | Usul | Keputusan |
|---|---|---|---|---|---|---|
| 1 | L25 | lightwalletd hanya melihat IP dan pola sync | Juga melihat tiap `GetTransaction(txid)` (`jitsuin-wallet/src/lib.rs:150`, dipakai `jitsuin-board/src/lib.rs:364`, `jitsuin-flow/src/settlement.rs:153`), IP penyiar tiap `pay`, `block_time` blok pelunasan, `block_txids` tinggi papan. Viewing key papan publik, jadi operator bisa membuka entri dari IP itu dan menautkan IP financier ke entri register/settled | ancaman hilang (tinggi) | Nyatakan; pakai node sendiri atau Tor | |
| 2 | L36 | Mitigasi `--connection tor` | ✔ Tidak diteruskan; `lwd.rs` langsung | dilebih-lebihkan | "Belum diimplementasikan" | |
| 3 | L16, L32 | `settled` tidak bisa ditautkan ke register | Siapa pun yang memegang N bisa menghitung `settled_tag(N)` (`jitsuin-core/src/entry.rs:218`): financier B, penerima riwayat, anggota dana (N ada di receivable note, `jitsuin-flow/src/financier.rs:403-407`), pemegang QR bocor. Bucket tenor publik (`entry.rs:13`): blok register + tenor ≈ blok settled di papan sepi | dilebih-lebihkan | "Tidak tertaut bagi pihak tanpa N, kecuali korelasi waktu/tenor" | |
| 4 | L22 | Anggota dana tidak melihat supplier | Lihat keputusan 4 (OVK, belum pasti) | salah (protokol, belum pasti) | Alamat terdiversifikasi per deal; ungkapkan | |
| 5 | L33 | Indeks hanya tampil bila ≥ k entri per kelas | Tidak ada kode HNK-08 atau ambang k; bucket ada di tiap memo dan ditampilkan per entri (`jitsuin-wasm/src/api.rs:559-560`) | dilebih-lebihkan | "Bucket tiap entri terbaca pemegang viewing key papan; ambang k hanya untuk agregat (belum ada)" | |
| 6 | L34, L21 | Hanya pihak KYC tahu `identity_pk` | `identity_pk` ada di tiap sertifikat (`jitsuin-core/src/history.rs:80`) dan semua financier yang dilamar (termasuk yang menolak) menerima sertifikat. Pemegang ujung rantai bisa menghitung `next_tag` (`history.rs:207`) dan memantau invoice berikutnya buyer: N, bucket, waktu, lalu hasil tepat waktu lewat `settled_tag` | dilebih-lebihkan + ancaman hilang | Risiko sisa; ini trade-off dari cek `UndisclosedSuccessor` | |
| 7 | L16, L18 | Financier tersembunyi di balik komitmen bersalt | Lihat keputusan 2 ✔ | ancaman hilang | Salt CSPRNG di library | |
| 8 | L15 | Explorer melihat jumlah action dan fee | Juga txid, nullifier, note commitment, anchor, expiry, ukuran. Perpindahan antar-pool membuka nominal lewat valueBalance | ancaman hilang (sedang) | Semua pihak satu pool; sebutkan | |
| 9 | L35 | QR bocor membuka alamat dan nominal | Memo di URI juga membawa kuitansi dan seal klaim: N, nominal, jatuh tempo (`jitsuin-flow/src/buyer.rs:39-52`). URI juga lewat tombol Copy (`jitsuinfi-frontend/src/lib/ui.ts:89`, `pages/buyer.ts:163`) dan argv devtool (`jitsuin-wallet/src/lib.rs:203-212`, terlihat di `ps`) | ancaman hilang (rendah-sedang) | Tambahkan N, clipboard, argv | |
| 10 | L23, L63 | Key tidak pernah disimpan | ✔ Halaman supplier mengunduh secret per invoice sebagai JSON plaintext (`jitsuinfi-frontend/src/pages/supplier.ts:115-118`) | dilebih-lebihkan | "Kecuali backup unduhan pengguna (plaintext)" | |
| 11 | L37 | Input transparan ditandai `touches_transparent` | ✔ Hanya memeriksa output (`jitsuin-wallet/src/lib.rs:89-93`) dan tidak pernah dipanggil di `pay` | dilebih-lebihkan | Cek input juga, atau tulis "hanya output" | |
| 12 | L31 | Metadata waktu hanya aktivitas papan | Wallet financier memposting register (`financier.rs:346`) lalu membayar advance segera; di chain shielded sepi, tx berikutnya kandidat advance | ancaman hilang (rendah) | Jeda acak | |
| 13 | L16 | Pemegang viewing key papan melihat N, komitmen, bucket, tag | Juga jenis entri (0x01 vs 0x03 = buyer memakai riwayat) dan txid. Nilai posting konstan 10 000 zat (baik) | ancaman hilang (rendah) | Tambahkan ke tabel | |
| 14 | `outsider.ts:5-14` | Tabel publik vs tersembunyi | Tidak ada baris "Visible" untuk bucket, flag tepat/telat, jenis entri, waktu blok; baris 10 dilebih-lebihkan (#3); baris 12 gagal terhadap pemegang `identity_pk` (#6) | dilebih-lebihkan | Tambah baris dan catatan | |
| 15 | L17, L19, L20 | Pihak tidak melihat financier/buyer lain | Alamat supplier atau financier dipakai ulang antar-deal: pihak yang berkolusi bisa menautkan deal | ancaman hilang (rendah) | Satu alamat terdiversifikasi per deal | |
| 16 | L40, L46 | Bundel memuat invoice | Bukti tanda tangan ganda juga memuat invoice penuh dan kedua entri (`jitsuin-core/src/proof.rs:32-38`) | benar, kurang lengkap | Tambahkan "dan bukti tanda tangan ganda" | |

Terverifikasi benar: N tidak bisa ditebak orang luar karena byte kanonik memuat key per invoice 32 byte CSPRNG supplier (`jitsuin-core/src/nullifier.rs:20-28`); tanda tangan register hanya bisa dicek dengan key supplier dari invoice (`entry.rs:136-147`); `settled_tag` menyembunyikan N dari yang tidak memegangnya; key buyer per invoice dari master lewat keyed BLAKE2b (`history.rs:45-66`); nilai posting papan konstan; CSP `connect-src 'self'` tanpa origin pihak ketiga; `pay` tidak pernah di-retry; TM L38–L39 (viewing key tidak bisa dicabut, viewing key dana membuka semua nominal) benar.

## Spesifikasi (HNK-12.T3)

| # | Spec | Klaim | Kenyataan | Tingkat | Usul | Keputusan |
|---|---|---|---|---|---|---|
| 1 | L139, L152 | Tidak boleh ada entri dengan tag sesudah sertifikat k; griefer hanya menambah noise | Lihat keputusan 1 ✔ | salah | Batasan di §8 dan Security; atau ubah desain | |
| 2 | L139 vs L75 | Dua entri bertag = equivocation; re-post tidak berbahaya | Re-post identik entri bertag menghasilkan `Equivocation` (`jitsuin-board/src/history.rs:124-131`), padahal `lookup` menerima re-post (`jitsuin-board/src/lib.rs:218-220`) | tidak presisi | Satukan entri dengan komitmen sama, atau larang re-post entri bertag | |
| 3 | L73 | Indeks tx = indeks transaksi dalam blok, dari `GetBlock` | Diurut menurut `CompactTx.index` (`lwd.rs:91-110`), lalu yang disimpan peringkat dalam compact block (`enumerate()`, `lib.rs:372`). Urutan sama, nilai berbeda bila lightwalletd melewatkan tx; posisi JTSP tidak cocok dengan full node | tidak presisi | Pakai `CompactTx.index` atau definisikan sebagai peringkat | |
| 4 | L73 | Indeks output | Nomor `Output N` dari devtool (`jitsuin-wallet/src/lib.rs:387-396`); `Position` tanpa pool; tx belum ditambang dilewati | tidak presisi / hilang | Definisikan; papan satu pool; hanya entri tertambang | |
| 5 | L119 | Flag 0x01 = dibayar sebelum/tepat jatuh tempo | Flag memakai waktu blok pembayaran sebagai hari UTC (`jitsuin-flow/src/settlement.rs:174`, `139-143`), bukan tanggal kuitansi. Catatan: `financierSettle` di wasm (PR#3, untuk landing) memakai tanggal kuitansi | tidak presisi | Nyatakan aturan persis; samakan wasm dengan flow atau jelaskan | |
| 6 | L119, L131 | Countersign setelah pembayaran tertambang menutup nominal | Juga butuh satu kuitansi per output bertanda tangan `buyer_pk` dengan nominal = nilai output (`jitsuin-flow/src/receipts.rs:66-79`), dan seal klaim buyer (`settlement.rs:135-138`) | hilang | Tambahkan prasyarat | |
| 7 | L131 | Pemegang N membangun ulang kedua seal | Butuh dokumen pelunasan (N, nominal, jatuh tempo), `buyer_pk`, `financier_pk` (`jitsuin-core/src/settled.rs:157-212`) | tidak presisi | Sebutkan input | |
| 8 | L121-129 | Tabel entri settled | Panjang total 167 byte tidak disebut (`settled.rs:13`, `38`); tag tidak ditandatangani; flag hanya di seal financier | hilang | Tambahkan | |
| 9 | L99, L109 | Policy seal invoice = (buyer) | Tanda tangan invoice buyer Ed25519 biasa atas byte kanonik (`invoice.rs:109-121`); `DocKind::Invoice` tidak dipakai | tidak presisi | Tandai "reserved" atau hapus | |
| 10 | L104 | `flag` seal | `verify_chain` mengabaikan flag (`seal.rs:261-272`); pelunasan: flag buyer 0, financier 1 atau 2; seal pengalihan menerima flag apa pun | hilang | Definisikan per dokumen dan peran | |
| 11 | L45 | Decoder menolak key tidak valid | Hanya cek titik bisa didekompresi (`invoice.rs:54-56`); key small-order lolos decode, gagal di `verify_strict` | tidak presisi | "bukan titik", atau cek `is_weak` | |
| 12 | L67-69 | Komitmen dan bucket | Salt 32 byte tanpa personalisasi (`entry.rs:204-214`); arti bucket belum didefinisikan (HNK-08) | hilang | Sebutkan ukuran salt; bucket ditentukan aplikasi | |
| 13 | L159 | Orang luar hanya melihat hash dan tanda tangan opak | Bucket dan jenis 0x03 terbaca; pemegang rantai bisa memantau invoice berikutnya | tidak presisi | Tambahkan ke bagian Privacy | |
| 14 | L139 | Cek verifier | Kode juga mewajibkan N berbeda antar-sertifikat (`jitsuin-core/src/history.rs:222`), allowlist financier, dan hasil `Open` | hilang | Dokumentasikan | |
| 15 | L147 | JTSP "dengan posisi papan opsional", diverifikasi offline | Layout tidak dispesifikasikan; `verify` mengabaikan posisi (`proof.rs:56-76`); cek papan butuh `first_at` dan urutan ketat | hilang / tidak presisi | Spesifikasikan; posisi = petunjuk tak terautentikasi | |
| 16 | L147 | Bundel `JTSB` | Layout tidak dispesifikasikan (`bundle.rs:5-15`, `72-115`) | hilang | Tambahkan tabel | |
| 17 | L75, L147 | Komitmen berbeda = pembiayaan ganda | Supplier yang menandatangani ulang untuk financier yang sama dengan salt baru menghasilkan "bukti" valid (`proof.rs:66-69`) | catatan | Satu komitmen per (invoice, financier) | |
| 18 | — | ZIP-321 | Tidak disebut; memo dikirim base64url tanpa padding, ≤ 512 (`jitsuin-wallet/src/lib.rs:260-301`) | hilang | Subbagian "Transport" | |
| 19 | — | Fee / ZIP-317 | Tidak disebut; tiap posting papan 10 000 zat (`financier.rs:26`, `settlement.rs:179`); root kewajiban self-send 10 000 zat; fee diserahkan ke devtool; siapa memegang spending key papan tidak dinyatakan | hilang | Nyatakan | |
| 20 | L12 | Uang hanya bergerak di pool shielded | Tidak ditegakkan; `touches_transparent` tidak dipanggil; alamat hanya dicek alfanumerik | catatan | Asumsi, atau tegakkan | |
| 21 | L143 | Solvabilitas memakai "repayments received for N" | Pelunasan dihitung tanpa cek tanda tangan atau tertambang (`jitsuin-flow/src/fund.rs:109-112`); root terbaru = max(periode, tinggi) | tidak presisi | Nyatakan | |
| 22 | L184 | Diuji di NU7, pool Ironwood | Lihat keputusan 5 | belum pasti | Hans konfirmasi | |
| 23 | L57 | Siapa pun bisa memindai dengan wallet watch-only | Paket browser memercayai posisi dan kelengkapan papan dari JSON backend (`jitsuin-wasm/src/api.rs:265-273`) | catatan | Nyatakan kepercayaan pada backend | |
| 24 | L7, L184 | Daftar crate | Tidak menyebut `jitsuin-wallet` | tidak presisi | Tambahkan | |

Terverifikasi benar: layout invoice kanonik dan aturan decoding (`invoice.rs:40-105`); N = BLAKE2b-256 "JitsuinNullifier" (`nullifier.rs:17-29`); offset entri register 136/168 byte dan cakupan tanda tangan (`entry.rs`); `financier_commitment` dan `settled_tag`; panjang item memo 145/200/48/144, memo terbesar 394 ≤ 512; layout kuitansi dan seal, string "JitsuinDocument_" / "JitsuinSealHash_"; layout surat pengalihan; derivasi key buyer "JitsuinBuyerKey_"; sertifikat riwayat 277 byte, "JitsuinHistory__" / "JitsuinHistTag__"; first valid wins; aturan financier (≥ 1 konfirmasi, cek ulang sebelum bayar, reorg); memo advance Sign-to-Pay; aturan validitas JTSP; keenam test vector diuji di unit test.

## Catatan untuk landing

- Temuan Spec #5: `financierSettle` (PR#3) menentukan tepat waktu dari tanggal kuitansi, sedangkan alur backend memakai waktu blok. Untuk landing (tanpa chain) ini wajar, tetapi perlu disebut di PR atau disamakan.
- Bab 6 landing dan halaman orang luar ikut terdampak kalau TM #3, #5, #6 diterima (klaim "tidak bisa ditautkan").
