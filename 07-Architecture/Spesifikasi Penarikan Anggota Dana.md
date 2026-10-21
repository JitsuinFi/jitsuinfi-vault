---
tags: [spec, "HNK-30.T23", "D-47", "HNK-29"]
type: spec
status: DIIMPLEMENTASIKAN
updated: 2026-10-21
---

# Spesifikasi Penarikan dan Bagi Hasil Anggota Dana

> **Peta link:** [[Decision Log]] (D-47) · [[Backlog]] (HNK-30.T23, HNK-29) · [[SEQ-05 - Anggota Dana]] · [[DFD-2.9 - Solvabilitas Dana]] · [[Format Data]] · [[Threat Model]]

Celah yang ditutup: alur dana sudah jelas untuk uang **masuk** (setoran, advance, pelunasan buyer ke kas operasional, root kewajiban `JTLR`), tetapi belum ada cara uang **kembali** ke anggota.

## Model: unit, bukan saldo
- Daun Merkle sum tree (HNK-15.T1) memegang **unit**, bukan saldo ZEC: `(id_daun, unit)`. Total unit = jumlah root.
- **Nilai per unit (NAV)** = (kas + piutang berjalan + piutang lewat tempo setelah potongan) ÷ total unit, dihitung anggota sendiri dengan `fund_view` / `solvency` yang sudah ada (`jitsuin fund`). Bagi hasil terjadi otomatis: pelunasan buyer menaikkan kas, sehingga NAV naik; tidak ada pembagian manual yang harus dipercaya.
- Setoran baru: unit = setoran ÷ NAV saat periode berjalan, dicatat di kuitansi setoran.
- `JTLR` tetap: root dan total sekarang berarti total unit. Format tidak berubah (8 byte total), maknanya ditulis di [[Format Data]].
- **Nilai dasar 1 zat per unit.** Unit pertama diterbitkan pada NAV 1; setoran berikutnya pada NAV saat itu. Karena total `JTLR` = total unit, uji `solvency` yang sudah ada (aset ≥ total) tetap berlaku tanpa diubah dan berarti "NAV tidak di bawah nilai dasar". Laba menaikkan NAV di atas 1.
- **Merkle sum tree:** daun = `SHA-256("jitsuin-fund-leaf-v1" ‖ id_daun ‖ unit_le8)`, node = `SHA-256("jitsuin-fund-node-v1" ‖ kiri ‖ jumlah_kiri_le8 ‖ kanan ‖ jumlah_kanan_le8)`, jumlah node = jumlah kedua anak; jalur = saudara (hash, jumlah, sisi). Root dan jumlahnya masuk ke `JTLR`.
- **Pembayaran penarikan** adalah uang keluar dari node, jadi setiap pembayaran butuh persetujuan passkey manajer (D-43, `pay.rs`), sama seperti advance.

## Hak menarik: token di kuitansi setoran
- Anggota tidak punya key tanda tangan (hanya key kotak surat). Kuitansi setoran (`fund.receipt`) membawa `token_tarik` acak 32 byte; daun menyimpan `id_daun = SHA-256("jitsuin-fund-leaf-v1" ‖ token_tarik)`.
- Permintaan tarik membuka `token_tarik`; manajer mencocokkannya dengan daun. Token baru dikirim di kuitansi pembayaran (sekali pakai).

## Alur penarikan
1. Anggota mengirim `fund.withdraw` tersegel ke kotak surat manajer: `{token_tarik, unit | "all", alamat_shielded_baru, periode}`.
2. Manajer mengantre permintaan sampai **akhir periode** (bukan seketika): penarikan dibayar dari **kas** saja, piutang yang belum jatuh tempo tidak dicairkan paksa.
3. Di akhir periode: NAV dihitung, setiap permintaan dibayar `unit × NAV` ke alamat shielded anggota. **Implementasi:** semua pembayaran satu transaksi (output per anggota, tanpa memo); kuitansi `fund.payout` (dengan `leaf_id` yang dibayar dan token baru bila unit tersisa) lewat relay. Pemegang UFVK melihat nominal tiap output, sama seperti transaksi terpisah.
4. Root `JTLR` periode berikutnya mencerminkan unit yang berkurang; anggota memeriksa jalurnya (9.7).
5. **Kas kurang:** semua permintaan periode itu dibayar pro-rata sejauh kas cukup, sisanya diantre ke periode berikut. Tidak ada anggota yang didahulukan.
6. **Tidak solvent** (`solvency` gagal): penarikan ditahan dan dicatat; anggota melihat verdict yang sama di perangkatnya.

## Privasi dan kebocoran
| Pihak | Melihat |
|---|---|
| Publik | Tidak ada (transaksi shielded) |
| Pemegang UFVK operasional (anggota lain, auditor) | Nominal tiap pembayaran keluar, tanpa identitas penerima (alamat baru per pembayaran). Sama dengan kebocoran setoran yang sudah tercatat di SEQ-05 |
| Manajer | Siapa menarik berapa (sudah tahu dari setoran) |

Mitigasi opsional: akun pembayaran terpisah yang viewing key-nya hanya untuk auditor, seperti akun setoran.

## Pesan baru (relay, JTSM)
| Tipe | Dari → ke | Body |
|---|---|---|
| `fund.withdraw` | anggota → dana | `token_tarik` (hex 32), `units` (uint atau `"all"`), `address` (teks), `period` (uint) |
| `fund.payout` | dana → anggota | `period`, `leaf_id`, `units`, `amount_zat`, `nav` {`assets_zat`, `units`}, `txid`, `next_token` (hex 32, hanya bila unit tersisa); signer `fund` |

## Implementasi (D-49, 2026-10-21)
- `jitsuin-core::units` (jitsuinfi-zcash): pohon, jalur, verifikasi; vektor dipakai juga oleh `src/lib/units.ts` di web app.
- jitsuinfi-node `fund.rs` + endpoint konsol: `GET /node/console/fund`, `POST /node/console/fund/deposits` (setoran harus sudah mined di wallet node), `POST /node/console/fund/withdrawals/{relay_id}`, `POST /node/console/fund/plan`, `POST /node/console/fund/close` (persetujuan passkey atas hash rencana; rencana ditolak bila ledger berubah sejak dibuat). Cadangan kas 100.000 zat untuk fee dan self-send root; potongan piutang lewat tempo 50 % saat menilai aset; tenggang 7 hari.
- Urutan tutup periode: bayar, simpan ledger (uang sudah keluar), kirim root `JTLR`, kirim jalur dan kuitansi. Bila root gagal dikirim, konsol menampilkan galatnya; ledger tetap benar.
- Web app: konsol 帳簿 (catat setoran, antre penarikan dari kotak surat, rencana dan tutup periode), halaman anggota (slip unit, cap jalur, permintaan tarik). Token tarik disimpan di store terenkripsi peran anggota.
- **Batas:** anggota hanya bisa membuktikan unitnya ada di root yang dikirim kepadanya; kecocokan dengan `JTLR` on-chain dan uji solvabilitas tetap lewat UFVK di perangkat sendiri. Kuitansi yang gagal terkirim ke relay belum bisa dikirim ulang.

## Task turunan bila disetujui
- HNK-29.T1 diperluas: daun berisi unit dan `id_daun` dari token; kuitansi membawa token.
- Antrean penarikan dan pembayaran akhir periode di node manajer.
- Halaman anggota (HNK-30.T22): tombol tarik, status antrean, NAV dan nilai unit miliknya.
