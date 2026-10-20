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
| U-HNK-23.1 | Enkripsi dan dekripsi pesan roundtrip | PASS | 2026-10-20 | jitsuin-core `mailbox::tests` (4) dan jitsuin-wasm `mailbox_keys_proof_and_sealed_messages_through_the_api`: segel lalu buka, kotak surat lain gagal, byte diubah gagal, terpotong gagal, key ephemeral baru = kotak berbeda, pesan kosong, key low-order ditolak, secret ephemeral dihapus; vektor tetap (PRF 0x11, e 0x22, nonce 0x33) sama dengan relay di jitsuinfi-backend `tests/vectors.test.ts` (`370fa2a`, `5143a65`) |
| U-HNK-23.2 | Bukti kepemilikan salah ditolak | PASS | 2026-10-20 | jitsuinfi-backend `tests/relay.test.ts` "registration needs a fresh, matching proof": bukti nol, challenge dipakai ulang, bukti dari secret lain dengan `mailbox_pk` korban, challenge untuk key lain, challenge untuk baca, challenge kedaluwarsa; tak satu pun mendaftarkan kotak surat (`2d987dd`) |
| U-HNK-23.3 | Pesan di atas batas ukuran ditolak | PASS | 2026-10-20 | `tests/relay-message.test.ts`: PDF > 2 MiB ditolak dengan pesan, saat encode dan saat header dibaca (`d015312`) |
| U-HNK-23.4 | Skema pesan: framing, jenis, peran, field wajib dan asing, versi, `to`, hash lampiran, tanda tangan Ed25519 (termasuk header atau lampiran yang diubah), cakupan semua aliran D7 | PASS | 2026-10-20 | `tests/relay-message.test.ts` 9 kasus, `npm test` 25/25 (`d015312`) |
| U-HNK-23.5 | API relay: daftar, kirim, baca hanya pemilik, ambil, hapus, kedaluwarsa | PASS | 2026-10-20 | jitsuinfi-backend `tests/relay.test.ts` 6 tes (memory store): id relay = id klien; kirim 202, kotak surat tak dikenal 404, tipe salah 400, terlalu kecil 400, di atas batas 413, penuh 429; daftar tanpa token / token lain / token kedaluwarsa 401; isi yang diambil byte-identik; pesan kedaluwarsa setelah 30 hari dan dibersihkan; key low-order ditolak; header `no-store`, `nosniff` (`2d987dd`) |
| U-HNK-23.6 | Skenario yang sama di Postgres | PASS | 2026-10-20 | Postgres Supabase (Session pooler, ap-southeast-1): `npm run migrate` membuat `relay_mailboxes`, `relay_messages`, `relay_challenges`, `relay_read_tokens`, RLS aktif di keempatnya; `tests/pg-store.test.ts` lulus (4,1 dtk), baris uji dihapus (0 kotak surat, 0 pesan sesudahnya) |

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
