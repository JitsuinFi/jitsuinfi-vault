---
tags: [test, "HNK-23"]
type: test
id: HNK-23
phase: F5
unit: PARSIAL
integrasi: TODO
e2e: TODO
updated: 2026-10-20
---

# TEST-HNK-23 - Relay kotak surat end to end

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-23 - Relay kotak surat end to end|AC]] · **Test** · [[ES-HNK-23 - Relay kotak surat end to end|Exec Summary]]

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-23.1 | Enkripsi dan dekripsi pesan roundtrip | TODO | — | — |
| U-HNK-23.2 | Bukti kepemilikan salah ditolak | TODO | — | — |
| U-HNK-23.3 | Pesan di atas batas ukuran ditolak | PASS | 2026-10-20 | `tests/relay-message.test.ts`: PDF > 2 MiB ditolak dengan pesan, saat encode dan saat header dibaca (`d015312`) |
| U-HNK-23.4 | Skema pesan: framing, jenis, peran, field wajib dan asing, versi, `to`, hash lampiran, tanda tangan Ed25519 (termasuk header atau lampiran yang diubah), cakupan semua aliran D7 | PASS | 2026-10-20 | `tests/relay-message.test.ts` 9 kasus, `npm test` 25/25 (`d015312`) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-23.1 | Supplier mengirim invoice + PDF ke buyer lewat relay di Railway, buyer membalas tanda tangan | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Daftar dua akun
- [ ] Kirim invoice dari supplier
- [ ] Buyer menerima dan membalas

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
