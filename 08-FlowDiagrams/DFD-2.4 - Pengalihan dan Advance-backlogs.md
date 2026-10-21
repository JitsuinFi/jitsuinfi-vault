---
tags: [flow, backlog]
status: DITETAPKAN
progress: 6/14 SELESAI
updated: 2026-10-20
---

# DFD-2.4 - Pengalihan dan Advance-backlogs

**Diagram:** [[DFD-2.4 - Pengalihan dan Advance]] · Rencana: [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] · [[FD-02 - Penelusuran Business Flow ke Backlog]] · Backlog: [[Backlog]]

Task untuk proses 4.1 – 4.8. Aturan kolom sama dengan [[DFD-2.1 - Identitas dan Sesi-backlogs]].

Kolom Status mengikuti langkah 6 "Audit flow diagram" di [[Workflow Development]]: `TODO` → `DIKERJAKAN` → `AUDIT` (semua task backlog-nya DONE) → `SELESAI (tanggal, bukti)` atau `GAGAL AUDIT (tanggal, alasan)`; `DITUNDA` hanya dengan keputusan user. Antrean audit tampil di setiap `python3 scripts/sync-vault.py` (lewat `scripts/check-backlogs.py`). Backlog ini ditetapkan 2026-10-20 (D-32).

## Task

| ID | Elemen | Task | Selesai bila | Ref | Task backlog | Owner | Status |
|---|---|---|---|---|---|---|---|
| BL-D24-01 | 4.1, F4.03 | Alamat bayar shielded diversified baru per deal dari wallet node | Dua deal berturut-turut memakai alamat bayar yang berbeda | K-11 | HNK-26.T17 | Hans | TODO |
| BL-D24-02 | 4.1, F4.01 – F4.06 | Kartu surat di konsol: unggah PDF surat, alamat dari node, teks urutan diperbaiki ("sebelum `Flow::new`") | Surat dibuat sebelum deal dimulai; teks kartu tidak lagi menyuruh menunggu entri terkonfirmasi | HNK-21.T4 | HNK-21.T4 | Dex | TODO |
| BL-D24-03 | 4.1, F4.06 | Surat + PDF surat dikirim ke supplier dan buyer lewat relay, pesan ditandatangani node dengan `financier_pk` | Supplier dan buyer menerima surat; pesan dengan tanda tangan salah ditolak | P-04 | HNK-23.T8 | Hans | TODO |
| BL-D24-04 | 4.2 – 4.3 | `assignmentDecode` di `jitsuin-wasm`: N, nominal, jatuh tempo, `financier_pk`, alamat bayar, `terms_hash` | Fungsi mengembalikan semua field; test roundtrip dengan `assignmentEncode` | P-13 | HNK-27.T3 | Hans | SELESAI (2026-10-20, `948133a`, U-HNK-27.3) |
| BL-D24-05 | 4.2, F4.07 – F4.13 | Layar supplier "Segel surat": tampilkan isi surat, cek PDF surat dengan `terms_hash`, segel s0, kirim ke buyer dan financier | PDF salah memunculkan peringatan sebelum tombol segel aktif | P-13 | HNK-24.T7 | Hans | SELESAI (2026-10-20, `17a01ea`: PDF salah dan financier lain ditolak sebelum tombol segel muncul, I-HNK-24.3) |
| BL-D24-06 | 4.3, F4.14 – F4.19 | Layar buyer "Segel surat": isi surat dan cek PDF yang sama, segel s1, kirim ke financier dan supplier | Sama dengan BL-D24-05 untuk buyer | P-13 | HNK-25.T3 | Hans | TODO |
| BL-D24-07 | 4.4, F4.20 – F4.23 | API `POST /node/deals/N/seals`; seal salah (`InvalidDeal`, `UnexpectedSigner`) tampil terbaca | Seal salah tidak mengubah state dan alasannya tampil | HNK-05.T3, C-13 | HNK-21.T9 | Hans | TODO |
| BL-D24-08 | 4.5, F4.24 – F4.28 | Hitung ulang konfirmasi bila entri ditambang ulang di tinggi lain | Advance tidak dibayar dengan konfirmasi di bawah minimum setelah reorg | K-7 | HNK-27.T6 | Hans | SELESAI (2026-10-20, `b6f33d5`, U-HNK-27.6) |
| BL-D24-09 | 4.5 – 4.7 | Persetujuan operator per deal (assertion passkey) sebelum `Pay` | Tanpa assertion operator untuk deal itu, advance tidak terkirim | P-07, P-05 | HNK-26.T15 | Hans | DIKERJAKAN (gerbang dan approval ada, `0f99c30`; audit saat deal API HNK-26.T5+ membayar advance lewat gerbang ini) |
| BL-D24-10 | 4.7, F4.36 – F4.38 | `Done` baru setelah tx advance terkonfirmasi; tx kedaluwarsa dicoba ulang | Retry setelah tx kedaluwarsa membayar lagi tepat satu kali | K-7 | HNK-27.T6 | Hans | SELESAI (2026-10-20, `b6f33d5`, U-HNK-27.6) |
| BL-D24-11 | 4.7, F4.40 | Teruskan txid advance ke supplier dan s2 ke buyer lewat relay | Supplier menerima txid; buyer menerima s2 | P-04 | HNK-23.T8 | Hans | TODO |
| BL-D24-12 | 4.8, F4.43 | Bandingkan advance yang diterima dengan advance yang disepakati | Advance kurang dari yang disepakati menjadi gagal di verifikasi | K-6 | HNK-27.T7 | Hans | SELESAI (2026-10-20, `a10185f`, U-HNK-27.7) |
| BL-D24-13 | 4.8, F4.42 – F4.45 | Status advance di layar supplier (txid, nominal, kecocokan) | Supplier melihat "Advance diterima" atau alasannya gagal | C-17 | HNK-24.T8 | Hans | SELESAI (2026-10-20, `17a01ea`: advance kurang ditandai, yang cocok menutup deal, I-HNK-24.3) |
| BL-D24-14 | Uji | E2E BF-06 dan BF-07 di testnet lewat relay dan API (siklus `TES-`) | Satu siklus lulus di HNK-17 | HNK-17 | HNK-17.T4 | Hans | TODO |

## Sudah ada (tanpa task baru)

- 4.4 verifikasi rantai seal (`Assignment::verify`), 4.5 cek terakhir dan idempotensi (`pay_advance`, `sent_advance`), 4.6 memo Sign-to-Pay, 4.7 kirim advance: diuji testnet.

## Roadmap

- F4.41 verifikasi kuat dari wallet supplier sendiri lewat CLI lokal: fungsi ada, perintah CLI menyusul setelah BL-D24-12.
