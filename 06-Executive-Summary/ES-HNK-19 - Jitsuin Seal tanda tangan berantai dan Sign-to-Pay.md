---
tags: [es, "HNK-19"]
type: es
id: HNK-19
phase: F3
lead: Hans
owners: [Hans]
status: SELESAI
updated: 2026-10-17
---

# ES-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|AC]] · [[TEST-HNK-19 - Jitsuin Seal tanda tangan berantai dan Sign-to-Pay|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans

## Apa diubah
- **Seal berantai** (`b007a26`): seal 200 byte per langkah, policy per dokumen, verifikasi rantai (urutan, role, signer, tanpa self-approval).
- **Surat pengalihan** (`fdc399e`, DEV-06): dokumen kanonik `JTSA`, disegel Supplier → Buyer → Financier.
- **Sign-to-Pay** (`f9fee3e`, DEV-07): state `AwaitAssignment`, cek papan terakhir sebelum bayar, memo advance berisi kuitansi + seal Financier.
- **Pelunasan dua pihak** (`f07787b`, DEV-08): dokumen pelunasan privat, klaim buyer di QR, tanda tangan financier dengan flag tepat waktu/terlambat, entri `settled` 167 byte tanpa N, status watchdog `Claimed`/`Disputed`/`Overdue`.
- **Bundel verifikasi** (`dd23864`): paket offline untuk auditor/juri + pengecekan papan.
- 58 unit test workspace lulus; `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Advance tanpa surat pengalihan tersegel | 0 | 0 (ditolak di testnet dan unit) |
| Klaim buyer tanpa pembayaran yang menjadi `Settled` | 0 | 0 (unit: `Claimed` → `Disputed`) |
| Waktu siklus penuh testnet | dicatat | 302 dtk (4 transaksi) |

## Status
**SELESAI** (bagian inti; FE dan CLI memakai API ini di HNK-10, HNK-09).

## Risiko tersisa
- Sign-to-Pay ditegakkan software financier, bukan chain (tanpa smart contract; FROST multisig di luar cakupan).
- Pembuktian pembayaran shielded ke pihak ketiga (ZIP-311) masih draft: kalau financier menyangkal pembayaran yang benar, buyer hanya punya txid.
- Uji mainnet menunggu ZEC (DEV-03). Di testnet, wallet-b membiayai peran supplier dan buyer (key Ed25519 berbeda).
- Dasar hukum (Pasal 613 KUHPerdata, UU ITE) perlu review ahli hukum.
- Peran AI agent menunggu keputusan user (lihat [[Desain Jitsuin Seal]]).

## Bukti
- Commit: `b007a26`, `fdc399e`, `f9fee3e`, `f07787b`, `dd23864` (lokal)
- ID tes: U-HNK-19.1–5, I-HNK-19.1; entri `33b8f3b0aa754e790e9c7fac0ae7dc08ce8612a8c26620d551d790e1ea390a56`, advance `501e40dafff4d2b7bcedf1adb9535522dc8977b6c6c8f8d3da55e00574335ccb`, pelunasan `d59014b726554404fc5729c8699d0d029fab7a3900485241d632c50bf4aadaf0`, `settled` `dcba74c63a701057d0e6e5f2cee4391b509d393c792801449c772c9552b7cad3`
- Persetujuan user untuk push/deploy: **disetujui 2026-10-17** ("Gas"); push ke `JitsuinFi/jitsuinfi-zcash` dan `JitsuinFi/jitsuinfi-vault`
