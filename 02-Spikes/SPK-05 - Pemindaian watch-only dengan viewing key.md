---
tags: [spike, "SPK-05"]
type: spike
id: SPK-05
area: Zcash
owner: Hans
status: PASS
updated: 2026-10-16
---

# SPK-05 - Pemindaian watch-only dengan viewing key

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Zcash · **Dipakai oleh:** HNK-04, HNK-09, HNK-15

## Tujuan
Pastikan tooling bisa mengimpor viewing key papan registry dan membaca memo entri, tanpa kemampuan mengirim.

## Hipotesis
`zcash-devtool` atau `zcash_client_backend` mendukung impor UFVK/UIVK watch-only dan mendekode memo masuk.

## Langkah
1. Buat akun papan uji `TES-board` (akun yang hanya menerima, tidak pernah mengirim).
2. Impor viewing key-nya ke wallet watch-only terpisah.
3. Kirim 2 entri uji; scan; baca memo.
4. Uji perbedaan UIVK vs UFVK: output keluar dan change tidak terbaca dengan UIVK.

## Kriteria lulus
- [x] Entri uji terbaca via viewing key.
- [x] Wallet watch-only tidak bisa mengirim.
- [x] Perilaku UIVK vs UFVK sesuai dokumentasi (dicatat).

## Fallback kalau gagal
- Publikasikan UFVK akun papan: aman karena akun papan tidak pernah mengirim dana. Catat sebagai keputusan di [[Decision Log]].

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Wallet watch-only `TES-board-watch` (UFVK) membaca entri tx `b6e9a61bd50c…` dan dua entri tx `d759bbf2605a…`; ketiganya ter-decode dengan signature valid. **Memo hanya terbaca setelah `wallet enhance`** (compact block tidak membawa memo; transaksi penuh harus diambil). | Implikasi HNK-04: scanner wajib mengambil transaksi penuh (`GetTransaction`/enhance) untuk setiap note yang masuk ke papan. |
| BLOCKED | 2026-10-16 | Run 3 (testnet): akun papan `TES-board` dibuat; UFVK-nya diimpor ke wallet watch-only `TES-board-watch` (`init-fvk`) → `Source: imported`, UIVK sama; `wallet send` dari watch-only ditolak: `Error: Cannot spend from view-only accounts`. Catatan: `init-fvk` hanya menerima UFVK (atau Sapling FVK), **tidak menerima UIVK**. | Kriteria 1 (membaca memo entri uji) menunggu TAZ untuk mengirim entri. Usulan D-11: publikasikan UFVK akun papan (aman karena akun papan hanya menerima). |
| BLOCKED | 2026-10-16 | Belum bisa dijalankan. | Butuh Rust (SPK-01) dan entri uji dari SPK-03. |

## Catatan
Papan registry = alamat yang viewing key-nya dipublikasikan. Lihat [[Viewing Key]].
