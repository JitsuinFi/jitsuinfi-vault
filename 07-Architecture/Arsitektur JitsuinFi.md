---
tags: [architecture]
---

# Arsitektur JitsuinFi

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Format Data]] · [[Threat Model]] · [[Decision Log]]

> Draf. Diperbarui di langkah 2 workflow setiap kali implementasi mengubah desain.

## Aktor
| Aktor | Peran |
|---|---|
| Supplier | Menerbitkan invoice, menjual hak tagih |
| Buyer | Menandatangani invoice (attestor), membayar saat jatuh tempo |
| Financier | Membayar di muka, menagih saat jatuh tempo |
| Papan registry | Alamat Zcash penerima entri; viewing key-nya dipublikasikan; tidak ada operator |
| Juri / auditor | Memverifikasi papan dan bukti lewat `jitsuin verify` |

## Komponen
| Komponen | Isi | Item |
|---|---|---|
| `jitsuin-core` (Rust lib) | Format invoice kanonik, tanda tangan, nullifier, encode/decode entri, commitment financier, kuitansi, bundel bukti, bucket indeks | HNK-01, HNK-02, HNK-07, HNK-08 |
| `jitsuin-wallet` | Sync, kirim shielded + memo, dekode memo; crate stabil atau wrapper `zcash-devtool`/Zally | HNK-03 |
| `jitsuin-board` | Scanner watch-only papan, urutan entri, deteksi N ganda | HNK-04 |
| `jitsuin-flow` | Alur per peran: state machine financier (cek → tunggu tanda tangan supplier → daftar → tunggu konfirmasi → bayar), verifikasi kuitansi di sisi supplier, permintaan pelunasan buyer (URI + QR ZIP-321), deteksi pelunasan dan entri `settled` | HNK-05, HNK-06 |
| `jitsuin` CLI | Perintah per peran + `jitsuin verify` untuk juri | HNK-05 – HNK-07, HNK-09 |
| Web app | UI supplier, buyer, financier; halaman indeks dan halaman orang luar | HNK-08, HNK-10, HNK-11 |
| Spesifikasi | *Shielded Receivable Registry* bergaya ZIP | HNK-12 |

## Infrastruktur
- **Chain:** Zcash mainnet, pool Ironwood, nominal kecil. Bukan testnet NU7.
- **Indexer:** lightwalletd/Zaino publik (SPK-02).
- **Hosting:** Railway (paket berbayar user) untuk backend dan frontend statis. Railway bukan TEE.
- **Wallet user:** Zodl via URI/QR ZIP-321 (SPK-04).
- **Tanpa:** smart contract, ZSA, TEE, cross-chain, CDN pihak ketiga.

## Desain lanjutan
- [[Desain Jitsuin Seal]]: tanda tangan berantai (adopsi konsep SignBaliola), Sign-to-Pay, pelunasan dua pihak, riwayat buyer.

## Alur utama
1. Supplier membuat invoice kanonik (dengan public key sementara supplier) → buyer menandatangani.
2. Financier A menghitung N, memindai papan → N belum ada.
3. Financier A mendapat tanda tangan supplier atas entri, mengirim entri ke papan, menunggu 1 konfirmasi.
4. Financier A membayar di muka secara shielded ke supplier dengan memo kuitansi.
5. Supplier dan buyer menandatangani surat pengalihan (alamat bayar financier).
6. Jatuh tempo: buyer membayar shielded ke financier dengan memo N → lunas.
7. Supplier mencoba ke financier B → B menemukan N → bundel bukti tanda tangan ganda.

## Terbuka (diputuskan lewat spike)
- Crate langsung vs wrapper CLI (SPK-01, SPK-03).
- Jenis viewing key papan yang dipublikasikan: UIVK atau UFVK akun papan (SPK-05).
- Memo biner vs teks dari Zodl (SPK-04).
- Aturan tie-break urutan entri (SPK-08).
