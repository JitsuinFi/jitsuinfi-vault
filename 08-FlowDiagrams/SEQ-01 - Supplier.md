---
tags: [flow, sequence, supplier]
status: DRAF
updated: 2026-10-19
---

# SEQ-01 - Supplier

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Auth: [[SEQ-00 - Autentikasi dan Onboarding]] · Pasangan: [[SEQ-02 - Buyer]] · [[SEQ-03 - Financier]] · DFD: [[DFD-2.2 - Penerbitan dan Tanda Tangan Invoice]] · [[DFD-2.3 - Registrasi Papan]] · [[DFD-2.4 - Pengalihan dan Advance]]

Supplier menerbitkan invoice, meminta tanda tangan buyer, menawarkannya ke satu financier, menandatangani entri papan untuk financier itu, menyegel surat pengalihan, lalu menerima advance bersama seal terakhir financier (Sign-to-Pay). Jalur "supplier nakal" (menawarkan invoice yang sama ke financier kedua) ada di bagian akhir.

Kode yang dipakai: `src/pages/supplier.ts` (layar simulasi), `jitsuin-wasm` (`publicKey`, `documentHash`, `invoiceEncode`, `invoiceDecode`, `supplierRegisterEntry`, `supplierRegisterHistoryEntry`, `supplierSealAssignment`, `assignmentStatus`), `jitsuin-flow::supplier` (`sign_register_entry`, `received_advances`, `verify_sign_to_pay`).

![SEQ-01](assets/seq-01-supplier.svg)

```plantuml
@startuml seq-01-supplier
!include seq-style.iuml
title SEQ-01 Supplier: dari invoice sampai advance (Sign-to-Pay)
actor "Supplier" as S
box "Perangkat supplier" #FAFBFE
  participant "Web app\n(layar Supplier)" as W
  participant "jitsuin-wasm" as X
  participant "Authenticator\npasskey" as A
  participant "Wallet Zodl\nsupplier" as ZW
end box
box "Server" #FFFDF5
  participant "Relay dokumen\n(USULAN P-04)" as R
end box
participant "Buyer\n(SEQ-02)" as B
participant "Node financier A\n(SEQ-03)" as FA
participant "Financier B" as FB
database "Papan registry\n(memo di chain)" as P
participant "Jaringan Zcash\n(lightwalletd)" as Z

== Masuk ==
S -> W : masuk sebagai Supplier (SEQ-00)
note over W #E7F3EA : ADA: layar Supplier; belum ada login (simulasi)

== 1. Siapkan invoice ==
S -> W : "Invoice baru"
alt saat ini (ADA)
  W -> X : 32 byte acak (crypto.getRandomValues) = secret per invoice
  W --> S : tombol "Download secret backup" (JSON plaintext)
  note right of W #FDECEC : temuan pra-review TM #10
else target (USULAN P-03)
  W -> A : PRF salt "jitsuin/supplier/master/v1"
  A --> W : master supplier
  W -> X : key per invoice = BLAKE2b(key = master, invoice_id)
end
X --> W : supplier_ephemeral_pk = publicKey(secret)
B -> R : invoice_pk(k) buyer (kartu kontak / pesan)
R --> W : invoice_pk(k)
S -> W : invoice_id (TES-INV-...), nominal (zat), tanggal terbit, jatuh tempo, file syarat (PDF)
W -> X : documentHash(file)
X --> W : terms_hash = SHA-256(file)
note right of W #E7F3EA : file tidak pernah diunggah
W -> X : invoiceEncode({invoice_id, supplier_pk, buyer_pk,\namount_zat, issue_date, due_date, terms_hash})
X --> W : invoice kanonik JTSI (base64url)
W -> X : invoiceDecode(invoice)
X --> W : field + N = BLAKE2b-256("JitsuinNullifier", byte kanonik)

== 2. Tanda tangan buyer ==
W -> R : ciphertext(invoice) ke kotak surat buyer
note right of W #FFF6D6 : USULAN P-04; sekarang: salin kode invoice
R -> B : invoice
B -> B : cek isi, tanda tangani (SEQ-02 langkah 2)
B -> R : sig_buyer (64 byte)
R --> W : sig_buyer
W -> X : bundleBuild({invoice, sig_buyer}) lalu verifyBundle
X --> W : tanda tangan buyer valid (verify_strict), N
note right of W #DDEBFA : PARSIAL: belum ada fungsi verifikasi tunggal

== 3. Tawarkan ke satu financier ==
S -> W : pilih financier A (kartu kontak), isi advance yang diminta,\nalamat Zodl untuk advance
ZW --> S : alamat shielded supplier (u1... / utest1...)
W -> R : penawaran {invoice, sig_buyer, alamat supplier, advance}
R -> FA : penawaran
FA -> P : cek papan untuk N (SEQ-03 langkah 3)
P --> FA : N belum ada
FA -> R : pembuka komitmen {financier_pk, salt 32 byte},\nbucket diskon dan tenor, history_tag (bila buyer memakai riwayat)
note right of FA #FFF6D6 : USULAN P-08: salt dibuat library (CSPRNG)
R --> W : pembuka komitmen + syarat deal

== 4. Tanda tangani entri papan untuk financier A ==
W --> S : tampilkan: N, financier, advance, bucket, tag riwayat
S -> W : "Tanda tangani entri"
W -> A : verifikasi pengguna (P-07)
A --> W : PRF / izin
alt buyer tanpa riwayat
  W -> X : supplierRegisterEntry(secret, invoice, financier_pk, salt)
else buyer dengan riwayat (HNK-20)
  W -> X : supplierRegisterHistoryEntry(secret, invoice, financier_pk, salt, sertifikat)
end
X --> W : {memo entri JTS1 136/168 byte, commitment}
note right of W #DDEBFA
PARSIAL: fungsi wasm ADA; kartu di layar supplier belum.
Bucket di wasm saat ini selalu 0/0
end note
W -> R : entri bertanda tangan
R -> FA : entri
FA -> Z : posting entri ke papan (10 000 zat + memo)
Z -> P : entri tertambang
FA -> FA : tunggu >= 1 konfirmasi

== 5. Segel surat pengalihan ==
FA -> R : surat pengalihan JTSA (N, nominal, jatuh tempo,\nfinancier_pk, alamat bayar financier, terms_hash surat)
R --> W : surat
W -> X : assignmentStatus(invoice, surat, [])
X --> W : surat cocok dengan invoice; langkah berikut = Supplier
S -> W : baca surat (PDF dicek dengan SHA-256), "Segel sebagai supplier"
W -> A : verifikasi pengguna (satu sentuhan = satu stempel)
A --> W : izin
W -> X : supplierSealAssignment(secret, invoice, surat)
X --> W : seal s0 (JTL1, 200 byte, langkah 0, role Supplier)
W -> R : s0 ke buyer dan financier A
R -> B : s0
R -> FA : s0
B -> R : s1 (seal buyer, SEQ-02 langkah 4)
R -> FA : s1

== 6. Terima advance (Sign-to-Pay) ==
FA -> Z : advance shielded ke alamat supplier;\nmemo = kuitansi advance + seal s2 financier + catatan piutang
Z -> ZW : note shielded masuk
FA -> R : txid advance + memo
note right of FA #FFF6D6 : USULAN: supplier menerima memo lewat relay
R --> W : txid + memo
W -> X : decode memo: kuitansi JTR1 (advance, N, nominal, signer)
W -> X : assignmentStatus(invoice, surat, [s0, s1, s2])
X --> W : Sealed
note right of X #E7F3EA
ADA di jitsuin-flow: received_advances + verify_sign_to_pay
(signer = financier_pk, nominal = nilai output, rantai Sealed)
end note
ZW --> S : saldo masuk; supplier mencocokkan nominal
W --> S : "Advance diterima, surat tersegel lengkap"

== 7. Pantau pelunasan (opsional) ==
W -> R : GET snapshot papan (USULAN P-06)
R --> W : memo papan
W -> X : bundleOnBoard(bundle dengan dokumen pelunasan, snapshot)
X --> W : register = Registered, settled = {on_time}

== Jalur supplier nakal ==
group menawarkan invoice yang sama ke financier B
  S -> R : penawaran yang sama ke financier B
  R -> FB : invoice + sig_buyer
  FB -> R : pembuka komitmen B
  S -> R : entri bertanda tangan untuk komitmen B
  R -> FB : entri B
  FB -> P : cek papan dengan key supplier dari invoice
  P --> FB : entri A sudah lebih dulu, tanda tangan valid
  FB -> FB : berhenti sebelum membayar (AlreadyFinanced)
  FB -> FB : doubleSignProof(invoice, sig_buyer, entri A, entri B)
  FB --> S : bukti tanda tangan ganda (JTSP), bisa diverifikasi siapa pun yang diberi
end
@enduml
```

## Ringkasan langkah dan status

| Bagian | Langkah | Status | Kode |
|---|---|---|---|
| 1 | Key per invoice acak + unduh backup | ADA (akan diganti) | `src/pages/supplier.ts` `downloadSecret` |
| 1 | Key per invoice dari master supplier | USULAN P-03 | — |
| 1 | Hash file syarat di browser | ADA | wasm `documentHash` |
| 1 | Invoice kanonik dan N | ADA | wasm `invoiceEncode`, `invoiceDecode` |
| 2 | Kirim invoice dan terima tanda tangan lewat relay | USULAN P-04 | sekarang salin-tempel |
| 2 | Cek tanda tangan buyer | PARSIAL | wasm `bundleBuild` + `verifyBundle` |
| 3 | Penawaran ke financier dan pembuka komitmen | USULAN P-04, P-08 | — |
| 4 | Tanda tangani entri register (dengan atau tanpa tag riwayat) | PARSIAL | wasm `supplierRegisterEntry`, `supplierRegisterHistoryEntry` |
| 5 | Segel surat pengalihan | ADA | wasm `supplierSealAssignment`, `assignmentStatus` |
| 6 | Verifikasi Sign-to-Pay | ADA di flow, USULAN di web | `jitsuin-flow::supplier::verify_sign_to_pay` |
| 7 | Status pelunasan dari papan | PARSIAL | wasm `bundleOnBoard` (butuh snapshot papan, P-06) |
| Nakal | Bukti tanda tangan ganda | ADA | wasm `doubleSignProof`, `jitsuin-core::proof` |
