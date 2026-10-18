---
tags: [ac, "HNK-11"]
type: ac
id: HNK-11
phase: F5
lead: Dave
owners: [Dave, Hans]
status: PASS
updated: 2026-10-18
---

# AC-HNK-11 - Threat model dan halaman orang luar

> **Peta link:** [[AC Hub]] · [[Backlog]] · **AC** · [[TEST-HNK-11 - Threat model dan halaman orang luar|Test]] · [[ES-HNK-11 - Threat model dan halaman orang luar|Exec Summary]]

**Item:** HNK-11 · **Fase:** F5 · **Dependency:** HNK-07

**Lead:** Dave #dave · **Tim:** Dave #dave, Hans #hans

## Deskripsi
Threat model per aktor dan halaman "apa yang bisa dilihat orang luar". Draf awal: [[Threat Model]].

## Acceptance criteria
Status per kriteria: `TODO` / `PASS` / `FAIL` / `BLOCKED`, wajib dengan tanggal dan bukti (commit, txid, log, id tes).

| ID | Kriteria | Status | Tanggal | Bukti |
|---|---|---|---|---|
| AC-HNK-11.1 | Threat model mencakup metadata waktu dan jumlah entri, QR ZIP-321 di tempat umum, IP ke lightwalletd, invoice fiktif, hilangnya penegakan smart contract, dan pengalihan confidential. | PASS | 2026-10-18 | [[Threat Model]] final: metadata waktu/jumlah entri, QR ZIP-321, IP ke lightwalletd (opsi `--connection tor`), invoice fiktif, tanpa smart contract, pengalihan confidential ([[Mode Confidential]]), plus serangan baru (riwayat, dana, griefing ekor, operator web) |
| AC-HNK-11.2 | Setiap kebocoran punya mitigasi atau dinyatakan sebagai risiko tersisa. | PASS | 2026-10-18 | Setiap baris tabel kebocoran dan serangan punya kolom mitigasi dan sisa risiko |
| AC-HNK-11.3 | Halaman orang luar menampilkan tampilan explorer yang kosong. | PASS | 2026-10-18 | Halaman "What outsiders see" (`cdcba0d`, `98466b2` (`jitsuinfi-frontend`, lokal)): kartu explorer untuk advance testnet `7b568799…` (input/output transparan: tidak ada; nominal, pihak, memo: terenkripsi) dan pembaca entri papan yang hanya menampilkan hash |
| AC-HNK-11.4 | Ditinjau ulang setelah HNK-05 – HNK-07 selesai. | PASS | 2026-10-18 | Ditinjau ulang 2026-10-18 setelah HNK-05 – HNK-07, HNK-19, HNK-20, HNK-15.T2 diuji di testnet |

## Deviasi
_Kosong._ Kalau implementasi menyimpang dari keputusan, tulis di sini **dan** di [[Backlog]] bagian Log Deviasi. Tidak ada perubahan diam-diam.
