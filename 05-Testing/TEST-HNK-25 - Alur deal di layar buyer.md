---
tags: [test, "HNK-25"]
type: test
id: HNK-25
phase: F5
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-25 - Alur deal di layar buyer

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-25 - Alur deal di layar buyer|AC]] · **Test** · [[ES-HNK-25 - Alur deal di layar buyer|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-25.1 | `k` dihitung dari rantai tertambat | TODO | — | — |
| U-HNK-25.2 | QR ditolak untuk surat belum `Sealed` | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-25.1 | Pembayaran QR testnet sampai `Settled` | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Tanda tangani invoice
- [ ] Setujui permintaan riwayat
- [ ] Segel surat
- [ ] Bayar QR
- [ ] Lihat riwayat saya

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
