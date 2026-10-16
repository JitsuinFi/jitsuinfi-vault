---
tags: [spike, "SPK-06"]
type: spike
id: SPK-06
area: Kripto
owner: Hans
status: PASS
updated: 2026-10-16
---

# SPK-06 - Kripto inti Ed25519 hash dan layout memo

> **Peta link:** [[Spikes Hub]] · [[Backlog]] · [[Rencana Fase]]

**Owner:** Hans #hans · **Area:** Kripto · **Dipakai oleh:** HNK-01, HNK-02, HNK-07

## Tujuan
Konfirmasi library memberi tanda tangan deterministik dan hash konsisten, entri muat 512 byte, dan encoding memo sesuai ZIP-302.

## Hipotesis
`ed25519-dalek` deterministik (RFC 8032); BLAKE2b-256 dengan personalisasi cukup untuk nullifier; entri sekitar 136 byte.

## Langkah
1. Tanda tangani byte yang sama dua kali → bandingkan.
2. Hitung N dengan BLAKE2b-256 personalisasi `Hanko_Nullifier`.
3. Encode entri sesuai [[Format Data]]; ukur panjang.
4. Baca ZIP-302: aturan byte pertama memo untuk data arbitrer (`0xFF`).
5. Simpan test vector.

## Kriteria lulus
- [x] Tanda tangan identik.
- [x] Test vector tercatat.
- [x] Ukuran entri ≤ 512 byte.
- [x] Aturan ZIP-302 terkonfirmasi.

## Fallback kalau gagal
- Kalau tanda tangan tidak deterministik: N = H(invoice kanonik ‖ pubkey buyer), tanda tangan buyer hanya sebagai otorisasi (catat DEV di [[Backlog]]).

## Hasil
| Status | Tanggal | Bukti | Catatan |
|---|---|---|---|
| PASS | 2026-10-16 | Lintas implementasi: Rust `ed25519-dalek` 2.2.0 + `blake2b_simd` 1.0.5 menghasilkan pk, sig, dan N **identik** dengan Node/Python (test vector run 1). Deterministik dan verifikasi OK. | Test vector siap dipakai di unit test HNK-01 dan HNK-02. |
| PASS | 2026-10-16 | Validasi desain dengan Node `crypto` (Ed25519) + Python `hashlib.blake2b` (person `Hanko_Nullifier`). Test vector: seed 32×`0x07`, pesan hex `01` + ASCII `TES-INV-0001`; pk `ea4a6c63e29c520abef5507b132ec5f9954776aebebe7b92421eea691446d22c`; sig `8d611668ca96505907dde4c3c65d44299a26fa538dcea32813287a9b65bcfef4b646a5198a8f10f48a66f17c665d23aa7907c249d4daa0363f0f336dfd13a800`; N `976189cf46c2169a14530b0d635dff7464764c9b9a9b222e1796b2ba57c1bcde`. Sign 2× identik; verifikasi setelah 1 byte diubah = false; 1 bit beda → N beda; entri 136 byte; ZIP-302: data arbitrer memakai byte pertama `0xFF`. | Implementasi Rust (`ed25519-dalek`) di HNK-01 wajib menghasilkan sig yang sama (RFC 8032 deterministik) — dipakai sebagai test vector lintas implementasi. |

## Catatan
Fondasi keamanan: N harus tidak bisa ditebak tanpa invoice bertanda tangan.
