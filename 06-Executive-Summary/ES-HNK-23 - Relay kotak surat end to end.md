---
tags: [es, "HNK-23"]
type: es
id: HNK-23
phase: F5
status: PARSIAL
updated: 2026-10-20
---

# ES-HNK-23 - Relay kotak surat end to end

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-23 - Relay kotak surat end to end|AC]] · [[TEST-HNK-23 - Relay kotak surat end to end|Test]] · **Exec Summary**

## Apa diubah
- **T1 (Hans), lokal:** skema pesan relay di `src/lib/relay-message.ts`: framing `JTSM`, header (jenis, versi, `to`, pengirim, N, `body` bertipe, lampiran ber-hash), 15 jenis pesan untuk semua aliran D7 + penawaran, PDF ≤ 2 MiB, tanda tangan Ed25519 untuk pesan node, dana, dan permintaan supplier. Spesifikasi di [[Format Data]] "Pesan relay". Baris relay di [[Threat Model]] ditinjau terhadap skema.
- Belum: T2 – T8.

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Data terbaca server | 0 (hanya ciphertext + metadata) | — |

## Status
**PARSIAL.** T1 DONE (lokal); relay, enkripsi, dan API belum.

## Risiko tersisa
_TODO_

## Bukti
- Commit: _TODO_
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
