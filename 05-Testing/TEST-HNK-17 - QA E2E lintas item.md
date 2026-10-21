---
tags: [test, "HNK-17"]
type: test
id: HNK-17
phase: F6
lead: Hans
owners: [Hans]
unit: TODO
integrasi: TODO
e2e: TODO
updated: 2026-10-22
---

# TEST-HNK-17 - QA E2E lintas item

> **Peta link:** [[Testing Hub]] · [[Backlog]] · [[AC-HNK-17 - QA E2E lintas item|AC]] · **Test** · [[ES-HNK-17 - QA E2E lintas item|Exec Summary]]

**Lead:** Hans #hans · **Tim:** Hans #hans 

## 1. Unit
Logika murni, cepat, tanpa DB dan tanpa chain.

| ID | Kasus | Hasil | Tanggal | Bukti |
|---|---|---|---|---|
| U-HNK-17.1 | N/A — item ini logika murni atau dokumen; tidak menyentuh DB/chain (dicatat, bukan dilewati) | TODO | — | — |

## 2. Integrasi
Skrip vs DB/chain sungguhan. Semua artefak memakai prefix `TES-` (invoice, akun, label, order).

| ID | Skenario | Hasil | Tanggal | Bukti (txid/log) |
|---|---|---|---|---|
| I-HNK-17.1 | N/A — item ini adalah eksekusi E2E | TODO | — | — |

**Bukti pembersihan:** sisa artefak off-chain `TES-` = _TODO_ (target **0**). Artefak on-chain tidak bisa dihapus; catat txid-nya di tabel di atas. Data produksi tidak boleh tersentuh.

## 3. E2E

### Runbook E2E testnet (HNK-17.T4, disiapkan 2026-10-22)
Dijalankan begitu Railway pulih. Semua invoice memakai prefix `TES-`. Isi kolom "Hasil aktual" dengan txid atau tangkapan layar.

**Prasyarat** (cek berurutan; berhenti kalau satu gagal):
1. `GET https://financier-node-production.up.railway.app/node/console/mandate` menjawab 401/403, bukan 404. Artinya node = main terbaru: `deals.rs`, riwayat buyer, mandat privat.
2. `GET https://relay-production-27dc.up.railway.app/api/health` → 200.
3. Production Vercel menyajikan main sesudah #42–#44: header app menampilkan "Testnet", konsol punya isian "Grace after due date".
4. Saldo wallet financier node minimal 0,002 ZEC testnet: 2 entri × 10.000 zat, advance uji 50.000 zat, fee, cadangan. Isi dari wallet uji `~/.hanko-tes/testnet/wallet-a` ke alamat di `/node/info`; seed tidak pernah keluar dari folder itu.
5. Konsol financier sudah di-pairing dengan passkey operator. Kalau undangan belum ada, jalankan skrip undangan (`pairing.json` lewat SFTP Railway).
6. Dua profil browser terpisah: supplier dan buyer, masing-masing dengan passkey sendiri. Kalau authenticator tidak punya PRF, pakai "Use test data" dengan dua secret berbeda.
7. Wallet buyer testnet (Zodl atau `zcash-devtool`, wallet-b) berisi ≥ 0,001 ZEC untuk membayar QR.

| Langkah | BF | Aksi | Hasil diharapkan | Hasil aktual | Status |
|---|---|---|---|---|---|
| 1 | BF-01 | Supplier, buyer, financier masuk; tukar kartu kontak, cocokkan sidik jari | Kotak surat "ready" di ketiga layar; kotak masuk terbuka sendiri | — | TODO |
| 2 | BF-02 | Supplier membuat `TES-INV-E2E1` (jatuh tempo +3 hari), kirim ke buyer; buyer cek PDF dan tanda tangan | Supplier menerima tanda tangan lewat kotak surat; status "signed, sent" | — | TODO |
| 3 | BF-03 | Supplier memilih financier di direktori (atau kartu), kirim penawaran dengan alamat buyer | Konsol: penawaran 認, cap 適/外/待 per aturan, sisa hari kedaluwarsa | — | TODO |
| 4 | BF-04 | Set mandat privat "Buyer history 0" + KYC mati, lalu Accept. Ulangi dengan riwayat aktif di deal kedua | Tanpa riwayat: pembuka komitmen langsung. Dengan riwayat: buyer menerima "History request", node menulis hasil cek di 案件 | — | TODO |
| 5 | BF-05 | Supplier "Use this entry request" lalu "Sign entry" | Entri otomatis ke node; 案件: 署 lalu 登; txid entri di papan (`/verify` papan live) | txid entri: — | TODO |
| 6 | BF-06 | Tunggu konfirmasi; supplier "Keep the letter" lalu segel; buyer "Keep the letter", "Keep the seal" lalu segel | Surat PDF di kedua layar; hash PDF = `terms_hash`; 案件 menjadi Pay | — | TODO |
| 7 | BF-07 | Konsol: "Approve with passkey: pay …" | Advance terkirim dengan segel financier; supplier menerima "Advance paid" dan txid; buyer menerima segel s2; 案件 金 lalu 済 | txid advance: — | TODO |
| 8 | BF-08 | Buyer step 5: QR muncul hanya setelah surat lengkap; bayar dari wallet-b | Node: repayment Settled, entri settled diposting; supplier dan buyer menerima bundel; status "settled on time" | txid pelunasan: —, settled: — | TODO |
| 9 | BF-09 | Deal kedua: jatuh tempo lewat tanpa bayar (atau bayar sebagian) | 案件: "Repayment overdue/claimed" dan tombol salin bukti JTSE | — | TODO |
| 10 | BF-10 | Supplier menawarkan `TES-INV-E2E1` ke financier kedua (node demo atau CLI) | Financier kedua: deal berhenti 重, Exhibit A bisa disalin dan lolos di `/verify` | — | TODO |
| 11 | BF-11 | Orang luar membuka `/verify` dan "What outsiders see" dengan bundel dan Exhibit A | Verdict 認/重 tanpa membuka pihak atau nominal | — | TODO |
| 12 | BF-12 | Dana: catat setoran anggota, permintaan tarik, tutup periode dengan passkey | Anggota menerima kuitansi, jalur 認, pembayaran; `jitsuin fund --path` = INCLUDED | — | TODO |

Setelah selesai: audit 32 baris BL berstatus AUDIT (`check-backlogs.py --strict`), lalu catat txid di README zcash (W-09).

- [ ] Jalankan panduan E2E HNK-01 – HNK-07 (putaran 1).
- [ ] Jalankan panduan E2E HNK-08 – HNK-11 (putaran 2).
- [ ] Retest semua bug yang sudah diperbaiki.
