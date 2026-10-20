---
tags: [es, "HNK-06"]
type: es
id: HNK-06
phase: F3
lead: Hans
owners: [Dex, Hans]
status: PARSIAL
updated: 2026-10-17
---

# ES-HNK-06 - Pengalihan hak tagih dan pelunasan

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-06 - Pengalihan hak tagih dan pelunasan|AC]] · [[TEST-HNK-06 - Pengalihan hak tagih dan pelunasan|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Dex #dex, Hans #hans 

## Apa diubah
- `jitsuin-flow::buyer`: `repayment_request` membuat URI ZIP-321 ke alamat financier dengan memo kuitansi pelunasan `JTR1` bertanda tangan buyer, plus `qr_svg`.
- `jitsuin-wallet`: URI satu pembayaran memakai bentuk `zcash:<alamat>?…` (paling umum dipindai wallet HP); `Devtool::pay_uri` membayar URI apa adanya.
- `jitsuin-flow::settlement`: `repayment` mencocokkan pembayaran ke N dan menghitung status `Unpaid` / `Pending` / `Partial` / `Settled`; `Financier::post_settled` mem-posting entri `settled` hanya setelah lunas, dan memakai entri yang sudah ada kalau dipanggil ulang.
- `jitsuin-core::settled_tag`; `jitsuin-board::settled`; `lookup` kini hanya menghitung entri register.
- 34 unit test workspace lulus; `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Pelunasan terdeteksi | 100% kasus uji | 100% (1/1 kasus testnet; 4 kasus unit termasuk palsu dan nominal beda) |
| Waktu deteksi setelah konfirmasi | dicatat | status `Settled` 60 dtk setelah buyer membayar (polling 10 dtk) |

## Status
**PARSIAL**. Bagian Hans (T2, T3, T4) selesai; T1 surat pengalihan (Dex), T5 layar QR dan T6 mode confidential (Dave) belum.

## Risiko tersisa
- AC-HNK-06.1 (surat pengalihan, Dex) dan AC-HNK-06.4 (mode confidential, Hans, dari Dave, D-35) belum.
- D-18 (penanda tangan entri `settled` = financier) menunggu keputusan user.
- Zodl belum diuji memindai QR ini (SPK-04 opsional); uji memakai `zcash-devtool` sebagai wallet buyer.
- Status `Pending` butuh mempool; `zcash-devtool sync` hanya melihat transaksi yang sudah ditambang, jadi di uji status langsung dari `Unpaid` ke `Settled`.
- Bucket entri `settled` disalin dari entri register; kalau kelasnya jarang, bisa memberi petunjuk tautan.
- N masih placeholder sampai DEV-04.

## Bukti
- Commit: `aff284d` (lokal)
- ID tes: U-HNK-06.2, I-HNK-06.1; pelunasan `b29fd4e1755159e2088777e6f2a31284908db3997722763206ac2efe489f7118`, entri `settled` `a81cd2045664e83a4141278f4878c401d6181344b90d02526fb2b61205e5e858`
- Persetujuan user untuk push/deploy: **disetujui 2026-10-17** ("Gas"); push ke `JitsuinFi/jitsuinfi-zcash` dan `JitsuinFi/jitsuinfi-vault`
