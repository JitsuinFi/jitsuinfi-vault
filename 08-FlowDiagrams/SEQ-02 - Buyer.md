---
tags: [flow, sequence, buyer]
status: DRAF
updated: 2026-10-19
---

# SEQ-02 - Buyer

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Auth: [[SEQ-00 - Autentikasi dan Onboarding]] · Pasangan: [[SEQ-01 - Supplier]] · [[SEQ-03 - Financier]] · DFD: [[DFD-2.2 - Penerbitan dan Tanda Tangan Invoice]] · [[DFD-2.4 - Pengalihan dan Advance]] · [[DFD-2.5 - Pelunasan dan Settled]] · [[DFD-2.6 - Riwayat Buyer]]

Buyer adalah attestor: tanda tangannya membuat invoice sah, seal-nya di surat pengalihan adalah pengakuan tertulis atas pengalihan (Pasal 613 KUHPerdata), dan pembayarannya ke financier menutup deal. Semua key buyer diturunkan dari satu passkey: key identitas dan satu key per invoice berdasarkan nomor urut `k`, jadi papan publik tidak bisa menautkan invoice-invoice satu buyer.

Kode yang dipakai: `src/lib/passkey.ts`, `src/pages/buyer.ts`, `jitsuin-wasm` (`buyerKeys`, `invoiceDecode`, `buyerSignInvoice`, `buyerHistoryCert`, `buyerSealAssignment`, `assignmentStatus`, `buyerRepayment`, `verifyHistory`), `jitsuin-flow::buyer` (`repayment_request`, `seal_assignment`, `qr_svg`).

![SEQ-02](assets/seq-02-buyer.svg)

```plantuml
@startuml seq-02-buyer
!include seq-style.iuml
title SEQ-02 Buyer: tanda tangan, pengakuan pengalihan, riwayat, pelunasan
actor "Buyer" as B
box "Perangkat buyer" #FAFBFE
  participant "Web app\n(layar Buyer)" as W
  participant "jitsuin-wasm" as X
  participant "Authenticator\npasskey" as A
  participant "Wallet Zodl\nbuyer" as ZW
end box
box "Server" #FFFDF5
  participant "Relay dokumen\n(USULAN P-04)" as R
end box
participant "Supplier\n(SEQ-01)" as S
participant "Node financier\n(SEQ-03)" as F
participant "Jaringan Zcash" as Z
database "Papan registry" as P

== Masuk ==
B -> W : "Buka key dengan passkey"
W -> A : credentials.get(), prf.eval.first = SHA-256("jitsuin/buyer/master/v1")
A -> B : verifikasi
B -> A : verifikasi
A --> W : master (32 byte, hanya di memori)
note right of W #E7F3EA : ADA: masterFromPasskey() di src/lib/passkey.ts
alt nomor invoice k saat ini (ADA)
  B -> W : ketik nomor invoice di riwayat (0, 1, 2, ...)
else target (USULAN P-09)
  W -> R : ambil rantai sertifikat sendiri (terenkripsi)
  R --> W : ciphertext
  W -> X : dekripsi, k = jumlah sertifikat
end
W -> X : buyerKeys(master, k)
X --> W : identity_pk, invoice_pk(k)

== 1. Bagikan key untuk invoice baru ==
W --> B : kartu kontak: invoice_pk(k) (QR / salin)
B -> R : invoice_pk(k) ke supplier
R -> S : invoice_pk(k)

== 2. Tanda tangani invoice ==
S -> R : invoice kanonik
R --> W : invoice
W -> X : invoiceDecode(invoice)
X --> W : invoice_id, supplier_pk, buyer_pk, nominal, tanggal, terms_hash, N
W -> W : cek buyer_pk = invoice_pk(k)
B -> W : buka file syarat dari supplier
W -> X : documentHash(file)
X --> W : SHA-256 = terms_hash ? cocok : tolak
B -> W : "Tanda tangani invoice"
W -> A : verifikasi pengguna (P-07)
A --> W : izin
W -> X : buyerSignInvoice(master, k, invoice)
X --> W : sig_buyer (Ed25519 atas byte kanonik)
W -> R : sig_buyer ke supplier
R -> S : sig_buyer

== 3. Ungkap riwayat ke financier (HNK-20) ==
F -> R : permintaan riwayat untuk invoice N (financier_pk)
R --> W : permintaan
W --> B : "Financier X meminta riwayat pembayaranmu"
B -> W : setujui (persetujuan eksplisit)
W -> A : verifikasi pengguna
A --> W : izin
W -> X : buyerHistoryCert(master, k, invoice, financier_pk, sertifikat k-1)
X --> W : sertifikat k (JTSH 277 byte, ditandatangani key identitas)
W -> R : sertifikat 0..k + identity_pk ke financier;\nsertifikat k ke supplier (untuk tag entri)
R -> F : rantai sertifikat
R -> S : sertifikat k
note right of R #FFF6D6
USULAN: rantai disimpan terenkripsi di kotak surat buyer (P-09).
Rantai hanya dibuka ke financier yang sedang diminta
end note

== 4. Segel surat pengalihan ==
F -> R : surat pengalihan JTSA
S -> R : seal supplier s0
R --> W : surat + s0
W -> X : assignmentStatus(invoice, surat, [s0])
X --> W : rantai valid, langkah berikut = Buyer
W --> B : tampilkan: bayar ke alamat financier, nominal, jatuh tempo
B -> W : "Segel sebagai buyer"
W -> A : verifikasi pengguna (satu sentuhan = satu stempel)
A --> W : izin
W -> X : buyerSealAssignment(master, k, invoice, surat, s0)
X --> W : seal s1 (role Buyer, mengikat hash s0)
W -> R : s1 ke financier dan supplier
R -> F : s1
note over F : financier membayar advance ke supplier (SEQ-03)

== 5. Bayar saat jatuh tempo ==
W --> B : pengingat jatuh tempo (lokal / relay)
B -> W : "Tampilkan QR pembayaran"
W -> X : buyerRepayment(master, k, invoice, surat, hari ini)
X --> W : {uri ZIP-321, qr_svg, memo}\nmemo = kuitansi pelunasan + seal klaim buyer (346 byte)
note right of X #E7F3EA : ADA: jitsuin-flow::buyer::repayment_request
W --> B : QR (hanya di layar buyer)
B -> ZW : pindai QR
ZW -> Z : transaksi shielded ke alamat financier, nominal tepat, memo utuh
Z -> F : pembayaran masuk wallet financier
F -> F : watchdog: cocokkan kuitansi + klaim, tunggu tertambang
F -> Z : entri settled dua tanda tangan ke papan
Z -> P : entri settled tertambang

== 6. Cek status dan riwayat sendiri ==
W -> R : GET snapshot papan (USULAN P-06)
R --> W : memo papan
W -> X : verifyHistory(sertifikat 0..k, identity_pk, allowlist, papan, hari ini, tenggang)
X --> W : on_time / late / defaults / open per invoice

== Jalur sengketa ==
group buyer mengaku bayar tanpa membayar
  ZW -> Z : tidak ada pembayaran (atau nominal kurang)
  F -> F : status Claimed; lewat jatuh tempo + tenggang menjadi Disputed
  note right of F #E7F3EA
  ADA: settlement::Repayment::status.
  Seal klaim buyer menjadi bukti yang tidak bisa disangkal
  end note
end
@enduml
```

## Ringkasan langkah dan status

| Bagian | Langkah | Status | Kode |
|---|---|---|---|
| Masuk | Master dari passkey PRF | ADA | `src/lib/passkey.ts` |
| Masuk | Nomor invoice `k` otomatis dari rantai sertifikat | USULAN P-09 | sekarang diketik di layar Buyer |
| 1 | Bagikan `invoice_pk(k)` | ADA (salin) / USULAN (relay) | wasm `buyerKeys` |
| 2 | Cek isi dan hash file syarat, tanda tangani | ADA | wasm `invoiceDecode`, `documentHash`, `buyerSignInvoice` |
| 3 | Terbitkan sertifikat riwayat dengan persetujuan | ADA (fungsi) / USULAN (alur persetujuan) | wasm `buyerHistoryCert` |
| 4 | Segel surat pengalihan | ADA | wasm `buyerSealAssignment`, `assignmentStatus` |
| 5 | QR ZIP-321 dengan kuitansi + klaim | ADA | wasm `buyerRepayment`, `jitsuin-flow::buyer` |
| 5 | Bayar dari Zodl | Belum diuji (SPK-04 TODO); fallback: wallet `zcash-devtool` | `jitsuin-wallet::Devtool::pay_uri` |
| 6 | Cek riwayat sendiri terhadap papan | PARSIAL | wasm `verifyHistory` (butuh snapshot papan, P-06) |
| Sengketa | Klaim tanpa pembayaran berakhir `Disputed` | ADA | `jitsuin-flow::settlement` |
