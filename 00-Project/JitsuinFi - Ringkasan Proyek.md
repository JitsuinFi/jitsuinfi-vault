---
tags: [project]
---

# JitsuinFi - Ringkasan Proyek

**Bagian dari:** [[00 - Project]] · Kembali: [[START-HERE]]

## Satu kalimat
JitsuinFi adalah **registry privat untuk pembiayaan invoice**: setiap invoice hanya bisa dibiayai satu kali, tanpa isi invoice, nominal, atau pihak-pihaknya terlihat publik.

**Tagline:** "Zcash stops double-spending. JitsuinFi stops double-financing."

**Nama:** *hanko* adalah stempel tanda tangan pribadi di Jepang untuk mengesahkan kontrak dan invoice. Desain JitsuinFi memang bertumpu pada tanda tangan debitur.

## Masalah
- **Pembiayaan ganda:** supplier nakal membiayakan invoice yang sama ke beberapa financier.
- Pencegahannya sekarang lewat registry terpusat (yang ikut melihat detail invoice) atau tokenisasi di chain publik (nominal, pemegang, sering identitas debitur terlihat).
- Detail invoice adalah rahasia dagang: siapa memasok siapa, berapa nilainya. Supplier yang butuh uang cepat juga sedang memberi sinyal kesulitan kas.

## Cara kerja singkat
1. Buyer menandatangani invoice (Ed25519 deterministik).
2. Financier menghitung nullifier `N = H("jitsuin" ‖ tanda tangan buyer)` dan memindai papan registry.
3. Kalau N belum ada: financier mendaftarkan N (entri bertanda tangan key sementara supplier), menunggu satu konfirmasi, lalu membayar di muka secara shielded.
4. Kalau N sudah ada: financier kedua mendapat **bukti kriptografis bahwa supplier menandatangani dua kali**.
5. Saat jatuh tempo, buyer membayar shielded ke financier dengan memo yang merujuk N.

Detail: [[Arsitektur JitsuinFi]] · [[Format Data]] · [[Threat Model]].

## Pengungkit kemenangan
1. **Indeks suku bunga publik:** bucket diskon dan tenor tanpa nominal dan pihak ("harga publik, partisipan gelap").
2. **Spesifikasi gaya ZIP:** *Shielded Receivable Registry*.
3. **Integrasi dengan tools invoice ekosistem:** "Mereka membuat invoice. Kami membuat invoice itu bisa dibiayai."
4. **Verifier CLI untuk juri:** `jitsuin verify` atas txid mainnet nyata.
5. **Pengguna sungguhan:** 1–2 merchant/freelancer komunitas Zcash.

## Scope
- **Dibangun:** invoice dagang saja (HNK-01 sampai HNK-14 di [[Backlog]]).
- **Roadmap di pitch:** promes, purchase order, termin proyek, reverse factoring, sewa, earned wage access; JitsuinFi Vault (dana bersama + bukti solvabilitas).
- **Di luar scope:** surat berharga publik (obligasi, SBN, sukuk, Treasuries), reksa dana, resi gudang, BNPL.

## Track dan kriteria
- Track: **Private Markets** (private credit).
- Kriteria juri berurutan: Privacy (bocor = diskualifikasi), Usefulness, Execution, Originality. Lihat [[ZECATHON - Aturan dan Deadline]].

## Hubungan dengan AVAL
Konsepnya mirip proyek user sebelumnya, **AVAL** (Casper Agentic Buildathon 2026). **Kode AVAL tidak dipakai.** Repo baru, kode baru, dan AVAL diungkapkan di deskripsi submission. Lihat keputusan D-03 di [[Decision Log]].

## Sumber
Catatan lengkap: `../Brainstorm/JitsuinFi.md` (di luar vault, jangan diubah dari sini). Daftar lain: [[Sumber Eksternal]].
