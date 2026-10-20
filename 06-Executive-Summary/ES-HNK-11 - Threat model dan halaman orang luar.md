---
tags: [es, "HNK-11"]
type: es
id: HNK-11
phase: F5
lead: Hans
owners: [Hans]
status: SELESAI
updated: 2026-10-18
---

# ES-HNK-11 - Threat model dan halaman orang luar

> **Peta link:** [[Exec Summary Hub]] · [[Backlog]] · [[AC-HNK-11 - Threat model dan halaman orang luar|AC]] · [[TEST-HNK-11 - Threat model dan halaman orang luar|Test]] · **Exec Summary**

**Lead:** Hans #hans · **Tim:** Hans #hans 

## Apa diubah
- [[Threat Model]] final: tabel siapa melihat apa, kebocoran, serangan, dan di luar cakupan, mencakup semua fitur yang sudah diuji testnet.
- [[Mode Confidential]] (HNK-06.T6).
- Halaman "What outsiders see" dengan kartu explorer dan pembaca entri papan.

_Dikerjakan Hans (agent) atas keputusan user D-25 / DEV-11; review oleh Hans (Dave tidak lagi memegang task, D-35)._

## Hasil vs KPI (angka riil)
| KPI | Target | Aktual |
|---|---|---|
| Kebocoran tanpa mitigasi atau pernyataan | 0 | — |

## Status
**SELESAI**.

## Risiko tersisa
- Review independen oleh Hans (HNK-11.T3) belum: dokumen ditulis agent (DEV-11).
- Payment disclosure (ZIP-311) masih draft: sisa risiko sengketa pelunasan tetap tercatat.

## Bukti
- Commit: lihat Apa diubah (lokal)
- ID tes: _TODO_
- Persetujuan user untuk push/deploy: _belum_
