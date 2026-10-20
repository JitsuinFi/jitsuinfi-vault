---
tags: [test, "HNK-26"]
type: test
id: HNK-26
phase: F5
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-26 - Konsol dan API node financier

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-26 - Konsol dan API node financier|AC]] · **Test** · [[ES-HNK-26 - Konsol dan API node financier|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-26.1 | Verifikasi assertion: challenge kedaluwarsa dan origin salah ditolak | TODO | — | — |
| U-HNK-26.2 | Serialisasi `Flow` roundtrip | TODO | — | — |
| U-HNK-26.3 | Penjadwal tidak memposting ulang txid tersimpan | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-26.1 | Deal testnet lewat API dan konsol | TODO | — | — |
| I-HNK-26.2 | Restart node di state `AwaitConfirmation` | TODO | — | — |
| I-HNK-26.3 | Kasus `AlreadyFinanced` dan `DoubleFinanced` | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Pairing passkey
- [ ] Terima penawaran
- [ ] Cek riwayat
- [ ] Posting entri
- [ ] Kumpulkan seal
- [ ] Setujui advance
- [ ] Settled otomatis

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
