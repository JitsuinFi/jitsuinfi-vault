---
tags: [es, "HNK-07"]
type: es
id: HNK-07
phase: F3
lead: Hans
owners: [Hans, Dave, Dex]
status: PARSIAL
updated: 2026-10-17
---

# ES-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|AC]] · [[TEST-HNK-07 - Deteksi pembiayaan ganda dan bukti tanda tangan ganda|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans, Dave #dave, Dex #dex

## Apa diubah
- `jitsuin-core::DoubleSignProof` (`JTSP`, `8e523f0`): invoice bertanda tangan buyer + dua entri register untuk N yang sama, ditandatangani key supplier dari invoice, dengan commitment berbeda; posisi papan opsional per entri; verifikasi offline.
- `jitsuin-board`: `proof_from_offer` (tanpa transaksi: tawaran supplier ke financier B saat A sudah terdaftar), `proof_from_lookup` (setelah balapan), `verify_proof_on_board`.
- 74 unit test workspace lulus; `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Deteksi pembiayaan ganda | 100% kasus uji | 100% (2/2 skenario testnet: tawaran dan balapan; unit: semua kasus) |
| False positive | 0 | 0 (re-post dengan commitment sama dan entri griefing tidak dihitung) |

## Status
**PARSIAL**. Bagian core Hans (T1) selesai; T2 (Hans, FE, menunggu scaffold Dave), T3 dan T5 (Dave), T4 uji mainnet (Dex) belum.

## Risiko tersisa
- Orang luar bisa melihat N yang sama muncul dua kali di papan (tanpa tahu invoice atau pihaknya, dan tidak bisa membedakannya dari griefing).
- Bundel bukti berisi invoice: hanya diberikan ke pihak berwenang (pengadilan, asosiasi, financier terkait).
- Kekuatan hukum bukti tanda tangan elektronik perlu review ahli hukum (UU ITE).
- Uji mainnet menunggu ZEC (DEV-03).

## Bukti
- Commit: `8e523f0` (lokal)
- ID tes: U-HNK-07.1–2, I-HNK-07.1; entri B `05d5aa7a02a33c14d460922468745fb4d6d814daa83989eed22b21c0540c79eb`
- Persetujuan user untuk push/deploy: **disetujui 2026-10-17** ("Gas push"); push ke `JitsuinFi/jitsuinfi-zcash` dan `JitsuinFi/jitsuinfi-vault`
