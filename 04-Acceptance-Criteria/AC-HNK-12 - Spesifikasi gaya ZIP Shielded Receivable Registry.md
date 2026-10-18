---
tags: [ac, "HNK-12"]
type: ac
id: HNK-12
phase: F4
lead: Dave
owners: [Dave, Dex, Hans]
status: TODO
updated: 2026-10-16
---

# AC-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|Test]] · [[ES-HNK-12 - Spesifikasi gaya ZIP Shielded Receivable Registry|Exec Summary]]

**Item:** HNK-12 · **Fase:** F4 · **Dependency:** HNK-02, HNK-07

**Lead:** Dave #dave · **Tim:** Dave #dave, Dex #dex, Hans #hans

## Deskripsi
Dokumen spesifikasi bergaya ZIP: motivasi, spesifikasi format dan algoritma, pertimbangan keamanan, dan test vector.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-12.1 | Struktur ZIP: Abstract, Motivation, Specification, Security Considerations, Test Vectors. | PASS | 2026-10-18 | `jitsuinfi-zcash/docs/zip-shielded-receivable-registry.md` (`c42af3e`): Abstract, Motivation, Conventions, Specification (10 bagian), Security Considerations, Privacy Considerations, Test Vectors, Reference Implementation |
| AC-HNK-12.2 | Test vector cocok dengan implementasi (dijalankan otomatis). | PASS | 2026-10-18 | Semua vector di dokumen diuji `cargo test --workspace` (core: `canonical_and_signature_vectors`, `nullifier_vector`, `document_hash_is_sha256`, `financier_commitment_vector`, `settled_tag_vector`, `key_derivation_vector_and_unlinkable_invoice_keys`). HNK-12.T2 (Dex: membaca vector langsung dari dokumen) tetap terbuka |
| AC-HNK-12.3 | Ditautkan dari README dan deskripsi submission. | TODO | 2026-10-18 | Ditautkan dari README `jitsuinfi-zcash`; deskripsi submission (HNK-14.T2) belum |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
