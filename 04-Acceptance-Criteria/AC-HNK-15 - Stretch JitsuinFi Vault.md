---
tags: [ac, "HNK-15"]
type: ac
id: HNK-15
phase: F7
lead: Hans
owners: [Dex, Hans, Dave]
status: TODO
updated: 2026-10-16
---

# AC-HNK-15 - Stretch JitsuinFi Vault

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-15 - Stretch JitsuinFi Vault|Test]] · [[ES-HNK-15 - Stretch JitsuinFi Vault|Exec Summary]]

**Item:** HNK-15 · **Fase:** F7 · **Dependency:** HNK-07, SPK-05

**Lead:** Hans #hans · **Tim:** Dex #dex, Hans #hans, Dave #dave

## Deskripsi
Dana bersama: setoran anggota → Merkle sum tree kewajiban → uji solvabilitas lewat FVK akun operasional. Hanya dikerjakan kalau F3 lulus paling lambat 23 Okt dan user setuju.

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-15.1 | Keputusan go/no-go user tercatat di [[Decision Log]]. | TODO | — | — |
| AC-HNK-15.2 | Root Merkle sum tree dicatat lewat memo per periode; anggota memverifikasi inklusi simpanannya. | TODO | — | — |
| AC-HNK-15.3 | Uji solvabilitas aset ≥ kewajiban dihitung dari data chain. | TODO | — | — |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
