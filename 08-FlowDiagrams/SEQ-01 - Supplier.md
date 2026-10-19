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
  W -> W : 32 byte acak (crypto.getRandomValues di JS) = secret per invoice
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
S -> W : invoice_id (TES-INV-...), nominal (ZEC, dikonversi ke zat),\ntanggal terbit, jatuh tempo, file syarat (PDF)
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
FA -> R : pembuka komitmen {financier_pk, salt 32 byte},\nkelas diskon dan tenor, history_tag (bila buyer memakai riwayat),\nsurat pengalihan JTSA (Flow::new sudah membutuhkannya)
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
Kelas di wasm saat ini selalu 0/0
(classes_for belum dipanggil)
end note
W -> R : entri bertanda tangan
R -> FA : entri
FA -> Z : posting entri ke papan (10 000 zat + memo)
Z -> P : entri tertambang
FA -> FA : tunggu >= 1 konfirmasi

== 5. Segel surat pengalihan ==
note over W : surat JTSA diterima di bagian 3 (N, nominal, jatuh tempo,\nfinancier_pk, alamat bayar financier, terms_hash surat)
W -> X : assignmentStatus(invoice, surat, [])
X --> W : surat cocok dengan invoice; langkah berikut = Supplier
S -> W : buka PDF surat (SHA-256 dicocokkan dengan terms_hash),\n"Segel sebagai supplier"
note right of W #DDEBFA
PARSIAL: wasm belum punya assignmentDecode, jadi alamat bayar
dan nominal di surat tidak bisa ditampilkan sebelum disegel
end note
W -> A : verifikasi pengguna (satu sentuhan = satu stempel)
A --> W : izin
W -> X : supplierSealAssignment(secret, invoice, surat)
X --> W : seal s0 (JTL1, 200 byte, langkah 0, role Supplier)
W -> R : s0 ke buyer dan financier A
R -> B : s0
R -> FA : s0
B -> R : s1 (seal buyer, SEQ-02 langkah 4)
R -> FA : s1
R -> W : s1 (salinan untuk supplier)

== 6. Terima advance (Sign-to-Pay) ==
FA -> Z : advance shielded ke alamat supplier;\nmemo = kuitansi advance + seal s2 financier + catatan piutang
Z -> ZW : note shielded masuk
FA -> R : txid advance (petunjuk)
R --> W : txid
alt verifikasi kuat (ADA di jitsuin-flow, butuh tx wallet supplier)
  W -> W : baca output + memo dari wallet supplier sendiri\n(watch-only supplier di node / CLI, bukan Zodl)
  W -> W : received_advances: kuitansi JTR1 advance, signer = financier_pk,\nnominal = nilai output; verify_sign_to_pay: [s0, s1] + s2 dari memo = Sealed
else hanya lewat relay (USULAN, lemah)
  W -> X : assignmentStatus(invoice, surat, [s0, s1, s2 dari memo relay])
  X --> W : Sealed
  note right of X #FDECEC
  Memo lewat relay tidak membuktikan uang dan seal
  ada di satu transaksi, atau nominal = nilai output.
  wasm juga belum punya dekoder kuitansi/memo
  end note
end
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
  FB -> R : pembuka komitmen B + minta entri bertanda tangan\nsebelum cek papan (kebijakan B, USULAN P-14)
  S -> R : entri bertanda tangan untuk komitmen B
  R -> FB : entri B
  FB -> P : cek papan dengan key supplier dari invoice
  P --> FB : entri A sudah lebih dulu, tanda tangan valid
  FB -> FB : berhenti sebelum membayar (AlreadyFinanced)
  FB -> FB : susun bukti dengan posisi entri A di papan\n(proof_from_offer di jitsuin-board)
  FB --> S : bukti tanda tangan ganda (JTSP)
  note right of FB #FDECEC
  Tanpa entri B (Flow sekarang meminta entri hanya setelah NotFound),
  B hanya tahu invoice sudah dibiayai, tanpa bukti. wasm doubleSignProof
  tidak mengisi posisi papan, sehingga jitsuin verify menolak buktinya
  end note
end

== Mode confidential (USULAN, roadmap) ==
note over S, FA #FFF6D6
Surat disegel Supplier lalu Financier saja (buyer tidak diberi tahu);
buyer membayar ke supplier, supplier meneruskan ke financier dengan
kuitansi bertanda tangan supplier; settled ditandatangani supplier + financier.
Belum diimplementasikan (Mode Confidential)
end note
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
| 5 | Segel surat pengalihan | PARSIAL: seal ADA; isi surat belum bisa ditampilkan (tanpa `assignmentDecode`) | wasm `supplierSealAssignment`, `assignmentStatus` |
| 6 | Verifikasi Sign-to-Pay | ADA di flow (butuh tx wallet supplier); lewat relay saja lemah | `jitsuin-flow::supplier::verify_sign_to_pay` |
| 7 | Status pelunasan dari papan | PARSIAL | wasm `bundleOnBoard` (butuh snapshot papan, P-06) |
| Nakal | Bukti tanda tangan ganda | PARSIAL: butuh entri B sebelum cek papan (P-14); wasm tanpa posisi papan | `jitsuin_board::proof_from_offer`, wasm `doubleSignProof` |
