---
tags: [architecture, design]
---

# Desain Jitsuin Seal

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Arsitektur JitsuinFi]] · [[Format Data]] · [[Decision Log]] · [[Threat Model]] · [[AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|AC-HNK-19]] · [[AC-HNK-20 - Riwayat pembayaran buyer standar minimal|AC-HNK-20]]

> Desain untuk HNK-19 (Jitsuin Seal, Sign-to-Pay) dan HNK-20 (riwayat buyer), 2026-10-17. Keputusan user: D-19 – D-22. Bagian bertanda **usulan** masih menunggu konfirmasi user. Format byte final ditulis di [[Format Data]] setelah diimplementasikan.

## 1. Inti
Jitsuin Seal mengadopsi **konsep** SignBaliola: dokumen ditandatangani beberapa pihak secara berurutan, dan dokumen tertahan sampai set tanda tangannya lengkap. Konsep ini diterapkan ke seluruh siklus factoring. Ada tiga hal yang tidak dimiliki SignBaliola:

1. **Privat.** Seal tidak dipublikasikan. Hanya pihak yang memegang dokumen yang bisa memverifikasinya; orang luar hanya melihat entri papan tanpa identitas.
2. **Sign-to-Pay.** Tanda tangan terakhir dan uangnya berpindah dalam **satu transaksi shielded**, jadi keduanya tidak bisa terpisah.
3. **Riwayat buyer** yang bisa dibuktikan tanpa membuka relasi dagang (HNK-20).

Hanya konsep yang diadopsi. Tidak ada kode SignBaliola yang dipakai: kodenya milik Baliola, dan aturan Originality ZECATHON mewajibkan kode ditulis selama build window.

## 2. Pemetaan SignBaliola ke Jitsuin Seal

| SignBaliola | Jitsuin Seal |
|---|---|
| PDF di-hash di browser; file tidak pernah dikirim | `terms_hash` = SHA-256 dokumen, dihitung di klien (`document_hash`) |
| `documentMetadata` mengelompokkan N stamp satu dokumen | N (nullifier, DEV-04) menjadi id dokumen; semua entri, kuitansi, dan seal merujuk N |
| Approver berurutan per role (SPV, Chief, HR), tidak boleh loncat | Policy per jenis dokumen: urutan role tetap; tiap seal mengikat hash seal sebelumnya (rantai) |
| Tidak boleh self-approve atau approve dua kali | Satu role satu seal; satu key tidak boleh memegang dua role |
| Threshold tercapai, status `stamped` | Semua role di policy lengkap, status `Sealed` |
| Stamp publik di Mandala Chain, alamat signer terlihat | Seal privat (memo shielded atau bundel); papan publik tanpa identitas |
| Link verifikasi publik | Bundel verifikasi untuk pihak yang diberi; `jitsuin verify` (HNK-09) |
| Meta-transaksi gasless | Fee Zcash ZIP-317, sekitar 10.000 zat per transaksi |
| Approval tercatat, dana di luar sistem | Sign-to-Pay: approval terakhir dan uang dalam satu transaksi |

## 3. Dokumen dan policy seal

| Dokumen | Id | Urutan seal | Gerbang |
|---|---|---|---|
| Invoice | N | Buyer (tanda tangan invoice, HNK-01) | Syarat financier mendaftarkan N |
| Surat pengalihan (cessie) | N | Supplier, lalu Buyer, lalu Financier | Advance hanya bisa dibayar setelah seal Supplier dan Buyer valid. Seal Financier ikut di transaksi advance |
| Pelunasan | N (di papan: `settled_tag`) | Buyer, lalu Financier | Entri `settled` sah hanya dengan dua tanda tangan |

Aturan rantai: langkah 0 tanpa seal sebelumnya; langkah k mengikat hash seal k−1. Seal dengan urutan salah, role ganda, key yang sama untuk dua role, atau isi yang diubah ditolak.

## 4. Surat pengalihan (usulan isi)
Dokumen kanonik berisi: N, nominal yang wajib dibayar buyer, tanggal jatuh tempo, `financier_pk`, alamat bayar financier, dan `terms_hash` (SHA-256 PDF surat).

**Dasar hukum (perlu review ahli hukum):**
- Pasal 613 KUHPerdata: pengalihan piutang (cessie) baru berlaku terhadap debitur setelah diberitahukan kepadanya, atau disetujui dan diakui secara tertulis. Seal buyer di surat pengalihan adalah pengakuan tertulis itu.
- UU ITE dan PP 71/2019: tanda tangan elektronik tidak tersertifikasi tetap alat bukti. Versi komersial bisa memakai tanda tangan tersertifikasi dari PSrE.

## 5. Sign-to-Pay
- **Advance:** satu memo (512 byte) membawa dua item: kuitansi advance (146 byte) dan seal Financier atas surat pengalihan. Uang dan tanda tangan penerimaan financier tiba bersamaan di supplier.
- **Pelunasan:** satu memo membawa kuitansi pelunasan dan tanda tangan buyer atas entri `settled`.
- **State machine financier (DEV-07):** `AwaitConfirmation` → `AwaitAssignment` (menunggu seal Supplier dan Buyer) → `Pay`. Advance tidak bisa dikirim tanpa surat pengalihan yang tersegel.

## 6. Pelunasan dua pihak dan sengketa

| Status | Kapan |
|---|---|
| `Unpaid` | Belum ada pembayaran valid |
| `Claimed` | Buyer menandatangani klaim lunas, tapi pembayaran yang cocok belum terlihat di wallet financier |
| `Settled` | Pembayaran valid sudah ditambang dan financier menambahkan tanda tangannya; entri `settled` dua tanda tangan di papan |
| `Disputed` | Klaim buyer lewat batas tenggang tanpa pembayaran yang cocok |
| `Overdue` | Jatuh tempo lewat tanpa pembayaran dan tanpa klaim |

**Skenario buyer berbohong:** buyer menandatangani "sudah bayar" padahal tidak membayar. Tanda tangan financier hanya dibuat otomatis kalau pembayaran yang cocok benar-benar diterima, jadi status berhenti di `Claimed` lalu `Disputed`, bukan `Settled`. Klaim palsu yang ditandatangani buyer menjadi bukti yang tidak bisa disangkal. Supplier memegang N, jadi bisa melihat status ini.

**Skenario sebaliknya (financier berbohong):** buyer memegang txid pembayarannya. Pembuktian pembayaran shielded ke pihak ketiga (payment disclosure, ZIP-311) masih draft, jadi ini dicatat sebagai risiko tersisa dan roadmap.

**Watchdog (bukan AI):** proses deterministik dengan akses baca saja (viewing key wallet financier + viewing key papan). Tugasnya mencocokkan pembayaran, menambahkan tanda tangan financier, menghitung status, dan memberi tahu pihak terkait. Watchdog tidak bisa membelanjakan dana. Pola ini setara "agent wallet + delegated access", tapi di Zcash delegasinya native lewat viewing key.

**AI agent (D-23, diputuskan 2026-10-17):** AI tidak menjadi hakim, karena kebenaran pelunasan sudah ditentukan tanda tangan dan chain. Kalau dipakai, AI hanya asisten lokal yang menjelaskan status dan menyusun draf surat sengketa dari data yang sudah dimiliki pengguna. AI tidak pernah menerima seed, spending key, atau viewing key, dan tidak mengirim data ke provider cloud (kebocoran mendiskualifikasi).

## 7. Riwayat buyer berantai sebagai standar minimal (HNK-20, D-20, DEV-10)
Keputusan user 2026-10-17: riwayat harus lengkap, termasuk yang buruk. Bukti yang hanya positif tidak cukup.

- **Key.** Buyer punya satu master secret (di web app: output passkey WebAuthn PRF). Dari situ diturunkan key identitas dan satu key per invoice berdasarkan nomor urut. Invoice memakai key per invoice sebagai `buyer_pk`, jadi papan publik tidak bisa menautkan invoice-invoice satu buyer.
- **Rantai.** Untuk setiap invoice yang dibiayai, key identitas menandatangani sertifikat riwayat: nomor urut, key invoice, key supplier, N, nominal, jatuh tempo, key financier, dan hash sertifikat sebelumnya.
- **Jangkar di papan.** Entri register invoice itu membawa *tag penerus* `BLAKE2b-256("JitsuinHistTag__", identity_pk ‖ hash sertifikat sebelumnya)`, dan tag-nya ikut ditandatangani supplier (entri jenis `0x03`). Akibatnya:
  - rantai yang dinomori ulang atau dicabangkan tidak cocok dengan tag di papan;
  - dua entri asli dengan tag yang sama = buyer mencabangkan rantai (equivocation);
  - invoice yang disembunyikan di ujung terdeteksi, karena tag penerus dari sertifikat terakhir sudah ada di papan;
  - buyer yang mengaku baru terdeteksi, karena tag pertama identitasnya sudah ada di papan.
- **Status per invoice dari papan.** Entri `settled` dua tanda tangan menunjukkan lunas, tepat waktu atau terlambat. Kalau tidak ada `settled` setelah jatuh tempo ditambah masa tenggang, statusnya gagal bayar. Selain itu, statusnya masih berjalan.
- **Standar minimal (policy financier).** Contoh: tidak ada gagal bayar, minimal 80% tepat waktu, dan buyer yang belum punya 2 pelunasan dianggap baru dengan plafon kecil. Financier hanya menghitung pelunasan dari financier di allowlist.
- **Privasi.** Rantai hanya dibuka buyer ke financier yang sedang diminta, mirip laporan kredit yang dipegang buyer sendiri. Orang luar tidak bisa menghitung tag. Pengecualiannya tag pertama: siapa pun yang tahu `identity_pk` bisa menemukan invoice pertama buyer itu.

**Batas yang jujur:**
- **Mulai bersih dengan identitas baru.** Diredam dengan mengikat key identitas ke KYC dan memberi plafon kecil untuk buyer baru.
- **Financier lalai mem-posting `settled`.** Buyer akan tampak gagal bayar. Buyer membantah dengan kuitansi dan klaimnya, dan kewajiban posting menjadi syarat masuk allowlist.
- **Griefing ekor rantai.** Pihak yang pernah melihat sertifikat terakhir buyer bisa mem-posting entri palsu dengan tag penerusnya untuk menghambat pembiayaan berikutnya. Entri palsu untuk posisi yang sudah diungkap tetap diabaikan, karena harus ditandatangani key supplier di sertifikat.

## 8. Yang tidak diambil
- **Commitment fee buyer (D-20):** deposit tidak bisa dikunci di pool shielded tanpa smart contract, dan versi transparan membocorkan nominal. Komitmen buyer diganti seal surat pengalihan dan riwayat pembayaran.
- **Escrow trustless (FROST multisig):** tooling masih tahap demo; terlalu berat untuk sisa waktu. Penegakan Sign-to-Pay ada di state machine financier.

## 9. Sumber ide tambahan
- **Mera / WebAuthn PRF** (bounty Monad, konteks tools saja): satu passkey menghasilkan banyak key terpisah lewat salt namespace. Dipakai untuk key per invoice tanpa seed.
- **Dynamic agent wallets + delegated access** (konteks): sama dengan watchdog berbasis viewing key.
- **Obscura Labs:** operator infrastruktur Zcash (Zebra, lightwalletd, DNS seeder) dan ZECFiat (gateway ZEC ke fiat untuk pasar Afrika). Relevan untuk roadmap: supplier bisa mencairkan advance ke mata uang lokal.
