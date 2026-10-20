---
tags: [ac, "HNK-23"]
type: ac
id: HNK-23
phase: F5
lead: Hans
owners: [Hans]
status: TODO
updated: 2026-10-20
---

# AC-HNK-23 - Relay kotak surat end to end

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-23 - Relay kotak surat end to end|Test]] · [[ES-HNK-23 - Relay kotak surat end to end|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans · Dibuat 2026-10-20 dari [[FD-01 - Keputusan Usulan dan Gelombang Kerja]] dan [[FD-02 - Penelusuran Business Flow ke Backlog]] (D-30)

**Item:** HNK-23 · **Fase:** F5 · **Dependency:** HNK-22

## Deskripsi
Relay dokumen (`jitsuinfi-backend`, Railway) sebagai kotak surat terenkripsi end to end: `mailbox_id` turunan, baca dengan bukti kepemilikan, skema pesan, pesan financier bertanda tangan node, rewrite same-origin. Menyerap HNK-10.T4 dan HNK-10.T5 (DEV-13). Desain: P-04, P-11 di [[FD-00 - Arsitektur Target dan Legenda]], [[DFD-1 - Proses Utama-backlogs]] (D7).

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-23.1 | Relay hidup di URL same-origin web app; CSP tetap `connect-src 'self'`. | TODO | — | — |
| AC-HNK-23.2 | `mailbox_id` yang disimpan relay sama dengan hitungan klien; pendaftaran tanpa bukti kepemilikan ditolak. | TODO | — | — |
| AC-HNK-23.3 | Pihak yang hanya tahu `mailbox_id` tidak bisa membaca daftar pesan. | TODO | — | — |
| AC-HNK-23.4 | Relay hanya menyimpan `mailbox_pk`, `mailbox_id`, ciphertext, dan masa simpan; isi tidak terbaca di server. | TODO | — | — |
| AC-HNK-23.5 | Pesan financier dengan tanda tangan salah ditolak di layar penerima. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
