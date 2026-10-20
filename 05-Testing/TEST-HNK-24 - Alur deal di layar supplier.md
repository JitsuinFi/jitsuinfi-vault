---
tags: [test, "HNK-24"]
type: test
id: HNK-24
phase: F5
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-24 - Alur deal di layar supplier

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-24 - Alur deal di layar supplier|AC]] · **Test** · [[ES-HNK-24 - Alur deal di layar supplier|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-24.1 | Test vector key per invoice | TODO | — | — |
| U-HNK-24.2 | `invoice_id` kembar ditolak | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-24.1 | Siklus supplier lewat relay dan node testnet | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Invoice baru
- [ ] Kirim ke buyer
- [ ] Tawarkan ke financier
- [ ] Tanda tangani entri
- [ ] Segel surat
- [ ] Lihat advance

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
