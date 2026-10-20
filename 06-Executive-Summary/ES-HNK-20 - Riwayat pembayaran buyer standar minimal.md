---
tags: [es, "HNK-20"]
type: es
id: HNK-20
phase: F3
lead: Hans
owners: [Hans]
status: SELESAI
updated: 2026-10-17
---

# ES-HNK-20 - Riwayat pembayaran buyer standar minimal

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-20 - Riwayat pembayaran buyer standar minimal|AC]] · [[TEST-HNK-20 - Riwayat pembayaran buyer standar minimal|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans 

## Apa diubah
- **Key dan rantai** (`f03cfb1`): `BuyerIdentity` (key identitas + key per invoice dari master secret/passkey PRF), `HistoryCert` 277 byte berantai, tag penerus, entri register jenis `0x03` bertag (DEV-10).
- **Verifier** (`687f2b4`): `verify_history` (jangkar tunggal bertanda tangan supplier, equivocation, penerus tersembunyi, allowlist) dan status per invoice (tepat waktu, terlambat, gagal bayar, berjalan); `MinimumStandard`.
- **Alur** (`e53ce12`): `check_buyer` sebelum registrasi; `Deal::history_tag` mewajibkan entri bertag.
- Wallet: retry `sync`/`enhance` setelah transport error sesaat (`8128d63`).
- 70 unit test workspace lulus; `fmt`, `clippy -D warnings`, `build` hijau.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Bukti riwayat palsu yang lolos | 0 | 0 (cabang, ekor tersembunyi, buyer "baru", tag palsu: semua tertangkap) |
| Tautan publik antar invoice satu buyer | 0 | 0 tanpa sertifikat (pengecualian: invoice pertama bisa ditemukan oleh pemegang `identity_pk`) |

## Status
**SELESAI** (bagian inti; layar FE dan derivasi passkey PRF di HNK-10).

## Risiko tersisa
- Griefing ekor rantai oleh pihak yang pernah melihat sertifikat terakhir buyer (lihat [[Desain Jitsuin Seal]] bagian 7).
- Identitas baru untuk mulai bersih: diredam KYC dan plafon buyer baru; penegakannya di luar protokol.
- Financier yang lalai mem-posting `settled` membuat buyer tampak gagal bayar.
- Derivasi key dari passkey (WebAuthn PRF) belum dibuat di FE; uji memakai master secret tetap.
- Uji mainnet menunggu ZEC (DEV-03).

## Bukti
- Commit: `f03cfb1`, `687f2b4`, `e53ce12` (lokal)
- ID tes: U-HNK-20.1–3, I-HNK-20.1; entri `89af294e09372d137cb9eae95b7b1ba8c7710bb9d14fe2584b4b8951f8cba4bf`, advance `2c33b0b0104014ff75d0a1e9d644c953724534feba16f96daa98895fc922cd08`, pelunasan `1d9f54ca37c4dcf74e65f79d00102c209d912d0889086376f4078b67190a875e`, `settled` `c60c777ec90cde166324df723ff7695149301f24db0f4d421f68c78dd62845fa`, entri deal 1 `fe7136876222e31921b7dd14ecf8b7a5efdeaf8a0c12179badc15389dd1db608`
- Persetujuan user untuk push/deploy: **disetujui 2026-10-17** ("Gas push"); push ke `JitsuinFi/jitsuinfi-zcash` dan `JitsuinFi/jitsuinfi-vault`
