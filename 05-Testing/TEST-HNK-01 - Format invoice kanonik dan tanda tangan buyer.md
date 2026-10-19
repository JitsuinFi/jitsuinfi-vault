---
tags: [test, "HNK-01"]
type: test
id: HNK-01
phase: F1
lead: Hans
owners: [Hans, Dex, Dave]
unit: PASS
integrasi: TODO
e2e: TODO
updated: 2026-10-19
---

# TEST-HNK-01 - Format invoice kanonik dan tanda tangan buyer

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-01 - Format invoice kanonik dan tanda tangan buyer|AC]] · **Test** · [[ES-HNK-01 - Format invoice kanonik dan tanda tangan buyer|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans, Dex #dex, Dave #dave

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

> **Verifikasi sementara (2026-10-16, Hans):** verifikasi sementara Hans: program di scratchpad memakai `jitsuin-core` lewat path dependency, 21/21 pemeriksaan lulus (bukan unit test resmi). Hasil: encoding deterministik dan roundtrip, sign 2× identik, verify OK, amount diubah ditolak, key salah ditolak, id kosong/amount 0/tanggal salah ditolak, trailing dan truncated ditolak. Unit test resmi tetap task Dex; tabel di bawah diisi saat test resmi ada.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-01.1 | Encode lalu decode menghasilkan invoice yang sama | PASS | 2026-10-19 | `crates/jitsuin-core/tests/invoice_vectors.rs::roundtrip` (jitsuinfi-zcash PR #2) |
| U-HNK-01.2 | Dua kali encode menghasilkan byte identik | PASS | 2026-10-19 | `canonical_bytes_are_deterministic_and_match_vector` — sama byte demi byte dengan `tests/vectors/invoice_v1.txt` (generator Python independen) |
| U-HNK-01.3 | Dua kali sign menghasilkan tanda tangan identik | PASS | 2026-10-19 | `signature_is_deterministic_and_matches_vector` + `vector_signature_verifies` (RFC 8032) |
| U-HNK-01.4 | Ubah satu field → verifikasi gagal | PASS | 2026-10-19 | `any_field_change_breaks_the_signature`: 6 field + buyer key lain → `BadSignature` |
| U-HNK-01.5 | Field kosong atau tidak valid ditolak | PASS | 2026-10-19 | `invalid_fields_are_rejected` (8 kasus) + `decoder_is_strict` (magic, versi, terpotong, trailing, amount 0) |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-01.1 | N/A — item ini logika murni atau dokumen; tidak menyentuh DB/chain (dicatat, bukan dilewati) | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E
Panduan langkah demi langkah untuk user.

- [ ] Jalankan `jitsuin invoice new` dengan data contoh `TES-INV-0001`.
- [ ] Buyer menandatangani; tampilkan byte hex dan tanda tangan.
- [ ] Ulangi → hasilnya sama persis.

| Langkah | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|
| 1 | _TODO_ | — | TODO |
