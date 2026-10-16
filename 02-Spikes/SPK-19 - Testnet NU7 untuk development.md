---
tags: [spike, "SPK-19"]
type: spike
id: SPK-19
area: Zcash
owner: Hans
status: PASS
updated: 2026-10-16
---

# SPK-19 - Testnet NU7 untuk development

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Zcash · **Dipakai oleh:** HNK-03 – HNK-07 (opsional)

## Tujuan
Menilai apakah development dan uji integrasi bisa memakai testnet (TAZ gratis) supaya hemat ZEC dan artefak uji tidak menumpuk di mainnet.

## Hipotesis
Testnet hidup dan bisa dipakai, tapi karena sudah NU7, butuh crate pre-release.

## Langkah
1. Cek endpoint testnet lightwalletd.
2. Cek apakah crate stabil mengenal NU7 di testnet.
3. Cari faucet TAZ yang aktif.
4. Kalau user memilih opsi hybrid: build dengan crate pre-release dan kirim 1 transaksi testnet.

## Kriteria lulus
- [x] Endpoint testnet hidup.
- [x] Diketahui crate mana yang bisa bertransaksi di testnet.
- [x] Faucet TAZ aktif ditemukan dan dicoba.
- [x] Satu transaksi testnet dengan memo berhasil (hanya kalau opsi hybrid dipilih).

## Fallback kalau gagal
- Mainnet saja dengan nominal kecil (rencana awal, D-04).

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Kriteria 4 terpenuhi: transaksi testnet dengan memo `b6e9a61bd50c…` dan `d759bbf2605a…` berhasil memakai `zcash-devtool` (crate pre-release). | Semua kriteria terpenuhi. |
| PASS | 2026-10-16 | Run 3: build crate pre-release (`zcash_client_backend =0.25.0-pre.2`, `zcash_client_sqlite =0.23.0-pre.2`, `pczt =0.10.0-pre.2`, `zcash_protocol =0.11.0-pre.1`, `ed25519-dalek` 2.2.0, `blake2b_simd =1.0.5`) hijau dalam 29 dtk; `Nu7` testnet = blok 4.465.026, mainnet `None`; test vector SPK-06 identik. Faucet testnet **`fauzec.com`** (dicek user): 1 TAZ per alamat per 24 jam, menerima UA `utest1…` dan Sapling, verifikasi Cloudflare Turnstile. `zecfaucet.com` menurut ZecHub adalah faucet **mainnet** (perlu dicek di browser). Wallet testnet `TES-wallet-a`, `TES-wallet-b`, `TES-board` dibuat di `~/.hanko-tes/` (izin 700/600, di luar repo dan vault). | Kriteria 4 (satu transaksi testnet dengan memo) menunggu TAZ dari faucet; diklaim user lewat browser karena ada Turnstile. |
| TODO | 2026-10-16 | Endpoint `testnet.zec.rocks:443` hidup: chain `test`, tinggi 4.508.756, branch `77190ad9`, node Zebra v7.0.0-rc.0, lightwalletd v0.5.4. NU7 aktif di testnet sejak blok 4.465.026 (4 Okt). Crate stabil (`zcash_protocol` 0.10.6) mencatat `Nu7 => None` untuk testnet → **tidak bisa membuat transaksi valid di testnet**; butuh crate pre-release (0.25.0-pre.2 dkk, rilis 2–14 Okt). Faucet: ZecHub menyebut `testnet.zecaucet.com` (belum diverifikasi); dokumentasi Zcash menyarankan minta TAZ di Discord. Satu sumber menyebut belum ada wallet konsumen yang terkonfirmasi mendukung NU7 testnet. | Butuh keputusan user: (A) mainnet saja, (B) hybrid testnet untuk dev + mainnet untuk demo, atau (C) testnet saja. |

## Catatan
_TODO_
