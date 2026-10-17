---
tags: [es, "HNK-15"]
type: es
id: HNK-15
phase: F7
lead: Hans
owners: [Dex, Hans, Dave]
status: PARSIAL
updated: 2026-10-17
---

# ES-HNK-15 - Stretch JitsuinFi Vault

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-15 - Stretch JitsuinFi Vault|AC]] · [[TEST-HNK-15 - Stretch JitsuinFi Vault|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Dex #dex, Hans #hans, Dave #dave

## Apa diubah
- `jitsuin-core::fund`: catatan piutang `JTN1` dan root kewajiban `JTLR` bertanda tangan manajer; container memo menerima keduanya (`e54ea36`).
- Memo advance kini membawa kuitansi + seal Financier + catatan piutang (394 byte).
- `jitsuin-flow::fund`: `fund_view` (kas, piutang, root terbaru dari data viewing key), `solvency`, `member_view`, `Financier::post_liability_root` (kirim ke akun sendiri).
- `Devtool::balance_zat` untuk wallet watch-only.
- 82 unit test workspace lulus; `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Verifikasi inklusi | 100% anggota uji | — (T1, Dex) |
| Solvabilitas dihitung anggota dari chain | ya | ya: aset 99567000 vs kewajiban 49786000 zat (testnet) |
| Root palsu yang diterima | 0 | 0 (1 diabaikan) |

## Status
**PARSIAL**. Bagian Hans (T2) selesai; T1 Merkle sum tree + inklusi simpanan (Dex) dan T3 halaman anggota (Dave) belum.

## Risiko tersisa
- Total kewajiban di root hanya sebaik Merkle sum tree-nya: tanpa T1 (Dex), anggota belum bisa mengecek simpanannya ikut terhitung.
- Viewing key akun operasional membuka nominal setiap setoran dan advance (tanpa identitas). Pisahkan akun setoran (viewing key hanya untuk auditor) kalau itu tidak diinginkan.
- Manajer bisa membiayai invoice fiktif bersama kaki tangannya; di chain terlihat sebagai gagal bayar, tapi tidak bisa dibuktikan sebagai penipuan. Audit sampel mengurangi risiko.
- Pelunasan dihitung dari nilai yang masuk dengan kuitansi untuk N itu; tanda tangan buyer tidak bisa dicek anggota (tidak memegang `buyer_pk`).
- Hukum: menghimpun dana anggota masuk ranah koperasi/investasi kolektif; diposisikan sebagai demo.

## Bukti
- Commit: `e54ea36` (lokal)
- ID tes: U-HNK-15.2, I-HNK-15.1; entri `72d0e3ed66c757cdb44e570f25ed77191b3e0f8aa111f4757ef65cc29f999083`, advance `7b5687991a8df84cdb334d910f5d08850b98d5d02c7df09cd1bff4f2c167dbd9`, root `d8c207554d7975a28213a7cac45405ecc7bc4ed536929683481ae630d642a03c`, root palsu `4692b8f092dcc0379d881bba1318a237ffd97aee9c8abf12318a70435498a815`
- Persetujuan user untuk push/deploy: _belum_
