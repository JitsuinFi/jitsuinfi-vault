---
tags: [test, "HNK-02"]
type: test
id: HNK-02
phase: F1
lead: Hans
owners: [Hans, Dex]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-17
---

# TEST-HNK-02 - Nullifier dan entri papan registry

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-02 - Nullifier dan entri papan registry|AC]] · **Test** · [[ES-HNK-02 - Nullifier dan entri papan registry|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

> **Verifikasi sementara (2026-10-16, Hans):** verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi). Hasil: memo 512/entri 136/marker 0xFF, roundtrip dengan dan tanpa padding, verify OK, key salah dan signature diubah gagal, padding non-nol ditolak, marker bukan 0xFF ditolak, kind tidak dikenal ditolak; nullifier belum diuji (DEV-04). Unit test resmi tetap task Dex; tabel di bawah diisi saat test resmi ada.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-02.1 | N sama untuk input sama | PASS | 2026-10-17 | `nullifier_vector`, `nullifier_depends_on_every_invoice_field_only` (`40d7656`) |
| U-HNK-02.2 | N berbeda bila satu bit input berbeda | PASS | 2026-10-17 | `nullifier_depends_on_every_invoice_field_only`: `invoice_id` dan `supplier_ephemeral_pk` diubah → N berbeda; invoice invalid ditolak |
| U-HNK-02.3 | Encode/decode entri roundtrip | TODO | — | — |
| U-HNK-02.4 | Panjang entri ≤ 512 byte | TODO | — | — |
| U-HNK-02.5 | Tanda tangan supplier salah → ditolak | TODO | — | — |
| U-HNK-02.6 | Magic atau tipe tidak dikenal → ditolak | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-02.1 | N/A — item ini logika murni atau dokumen; tidak menyentuh DB/chain (dicatat, bukan dilewati) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] `jitsuin entry build` dari `TES-INV-0001` → tampilkan ukuran dan hex.
- [ ] `jitsuin entry verify` → valid.
- [ ] Ubah satu byte → invalid.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
