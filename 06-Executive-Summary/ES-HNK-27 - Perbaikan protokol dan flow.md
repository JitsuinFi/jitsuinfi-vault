---
tags: [es, "HNK-27"]
type: es
id: HNK-27
phase: F3
status: PARSIAL
updated: 2026-10-20
---

# ES-HNK-27 - Perbaikan protokol dan flow

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-27 - Perbaikan protokol dan flow|AC]] · [[TEST-HNK-27 - Perbaikan protokol dan flow|Test]] · **Exec Summary**

## Apa diubah
- **Salt komitmen (T1):** `commitment_salt` / `commitment_opening` di `jitsuin-core`, `Financier::commitment_opening`, wasm `financierCommitment`. Diturunkan dari key financier dan N (DEV-14).
- **Kelas (T2):** `Deal` membawa kelas, `deal_classes()` memakai `classes_for` (0/0 bila tidak cocok kelas mana pun), `check_entry` menolak kelas yang berbeda; fungsi entri wasm menerima kelas opsional.
- **`assignmentDecode` (T3)** di wasm, dengan `matches_invoice`.
- **Bukti dengan posisi (T4):** `doubleSignProof` menerima posisi opsional kedua entri.
- **`register()` (T5):** cek papan ulang tepat sebelum posting (`BoardChecked` diterima di `Register`) dan `sent_entry` mencegah posting kedua.
- **Konfirmasi (T6):** state baru `AwaitAdvanceConfirmation`; `Done` hanya setelah advance tertambang; kedaluwarsa (`ADVANCE_EXPIRY_BLOCKS` = 50) kembali ke `Pay` dan dibayar ulang sekali; entri yang ditambang ulang dihitung ulang.
- **Nominal advance (T7):** `verify_sign_to_pay` menerima `agreed_advance_zat`.
- **Entri dari tag (T8):** wasm `supplierRegisterTaggedEntry`.
- **Secret byte (T9):** `with_secret` + 9 export `*Bytes` yang menolkan `Uint8Array` pemanggil; `BuyerIdentity` menolkan master saat di-drop.
- **CLI dana (T10):** `jitsuin fund`; `SolvencyPolicy.grace_days` (tidak pernah dibaca) dihapus.

Kompatibilitas: semua parameter baru di wasm opsional, jadi landing page tetap jalan tanpa perubahan. `Event::AdvanceSent` sekarang membawa `tip_height` dan `verify_sign_to_pay` punya parameter baru (pemanggil hanya test).

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Temuan FD-00 §6 yang tertutup | semua kecuali P-14 | 8 dari 14 baris ditutup di kode (lihat audit di file `-backlogs`); sisanya milik item lain (HNK-21, HNK-24 – HNK-26, HNK-28) |
| `scripts/check.sh` | hijau | All checks passed (`9826b09`) |
| Tes unit baru | — | 11 kasus (U-HNK-27.1 – .11) |

## Status
**PARSIAL.** Semua 10 task selesai di kode dan lulus unit test; AC-HNK-27.2 menunggu uji integrasi dengan ≥ 5 deal berkelas, dan uji crash testnet (I-HNK-27.2) menunggu persistensi `Flow` (HNK-26.T10).

## Risiko tersisa
- `ADVANCE_EXPIRY_BLOCKS` mengasumsikan delta kedaluwarsa default 40 blok dari `zcash-devtool`; bila wallet memakai delta lain, angka ini perlu disesuaikan.
- Penolkan secret bersifat upaya terbaik: salinan di dalam derivasi tetap ada sampai memori dipakai ulang (tanpa crate `zeroize`).
- Kelas tetap 0/0 sampai layar supplier (HNK-24.T6) dan node (HNK-26) mengisinya.

## Bukti
- Commit: `748d451`, `d5f98d0`, `59cd762`, `948133a`, `14803af`, `fef1d15`, `b6f33d5`, `a10185f`, `8897517`, `1ac7057`, `9826b09` (branch `hans/hnk-27-protocol-fixes` jitsuinfi-zcash, belum di-push)
- ID tes: U-HNK-27.1 – U-HNK-27.11 PASS; I-HNK-27.1 – .3 TODO
- Persetujuan user untuk push/deploy: _belum_
