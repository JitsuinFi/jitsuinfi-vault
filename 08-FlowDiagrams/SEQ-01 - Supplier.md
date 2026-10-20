---
tags: [flow, sequence, supplier]
status: DRAF
updated: 2026-10-20
---

# SEQ-01 - Supplier

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda: [[FD-00 - Arsitektur Target dan Legenda]] · Auth: [[SEQ-00 - Autentikasi dan Onboarding]] · Pasangan: [[SEQ-02 - Buyer]] · [[SEQ-03 - Financier]] · DFD: [[DFD-2.2 - Penerbitan dan Tanda Tangan Invoice]] · [[DFD-2.3 - Registrasi Papan]] · [[DFD-2.4 - Pengalihan dan Advance]] · [[DFD-2.7 - Deteksi Pembiayaan Ganda]]

Supplier menerbitkan invoice, meminta tanda tangan buyer, menawarkannya ke satu financier, menandatangani entri papan untuk financier itu, menyegel surat pengalihan, lalu menerima advance bersama seal terakhir financier (Sign-to-Pay). Jalur "supplier nakal" (menawarkan invoice yang sama ke financier kedua) ada di bagian akhir. Urutan dengan financier sama dengan [[SEQ-03 - Financier]]: pembuka komitmen dan surat (SEQ-03 bagian 1b), cek riwayat buyer (bagian 2), cek papan (bagian 3), lalu permintaan entri (bagian 4).

Kode yang dipakai: `src/pages/supplier.ts` (layar simulasi), `jitsuin-wasm` (`publicKey`, `documentHash`, `invoiceEncode`, `invoiceDecode`, `bundleBuild`, `verifyBundle`, `bundleOnBoard`, `supplierRegisterEntry`, `supplierRegisterHistoryEntry`, `supplierSealAssignment`, `assignmentStatus`, `doubleSignProof`), `jitsuin-flow::supplier` (`sign_register_entry`, `received_advances`, `verify_sign_to_pay`), `jitsuin-board::proof_from_offer`.

![SEQ-01](assets/seq-01-supplier.svg)

[Buka diagram ukuran penuh](assets/seq-01-supplier.svg)

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
  participant "jitsuin CLI lokal\n+ watch-only supplier\n(USULAN)" as CL
end box
box "Server" #FFFDF5
  participant "Relay dokumen\n(USULAN P-04)" as R
end box
participant "Buyer\n(SEQ-02)" as B
participant "Node financier A\n(SEQ-03)" as FA
participant "Financier B" as FB
participant "Verifier / pihak\nberwenang (SEQ-04)" as V
database "Papan registry\n(memo di chain)" as P
participant "Jaringan Zcash\n(lightwalletd)" as Z

== Masuk ==
S -> W : masuk sebagai Supplier (SEQ-00)
note over W #E7F3EA : ADA: layar Supplier; belum ada login (simulasi)

== 1. Siapkan invoice ==
S -> W : "Invoice baru", invoice_id (TES-INV-...)
alt saat ini (ADA)
  W -> W : secret per invoice: 32 byte acak\n(crypto.getRandomValues di JS)
  W --> S : tombol "Download secret backup" (JSON plaintext)
  note right of W #FDECEC : temuan pra-review TM #10
else target (USULAN P-01, P-03)
  W -> A : prf.eval.first =\nSHA-256("jitsuin/supplier/master/v1")
  A --> W : master supplier
  W -> X : key per invoice = keyed BLAKE2b(master),\npersonalisasi sendiri, input unik per invoice
  note right of X #FFF6D6
  Bukan invoice_id polos: id yang dipakai ulang
  memberi key sama, dan entri lain supplier jadi
  bisa ditemukan. invoice_id dipakai ulang ditolak
  end note
end
X --> W : supplier_ephemeral_pk = publicKey(secret)
B -> R : invoice_pk(k) buyer (pesan, SEQ-02 bagian 1)
R --> W : invoice_pk(k)
S -> W : nominal (ZEC, dikonversi ke zat), tanggal terbit,\njatuh tempo, file syarat (PDF)
W -> X : documentHash(file)
X --> W : terms_hash = SHA-256(file)
note right of W #E7F3EA : file tidak diunggah ke server
W -> X : invoiceEncode({invoice_id, supplier_pk, buyer_pk,\namount_zat, issue_date, due_date, terms_hash})
X --> W : invoice kanonik JTSI (base64url)
W -> X : invoiceDecode(invoice)
X --> W : field + N = BLAKE2b-256("JitsuinNullifier",\nbyte kanonik)

== 2. Tanda tangan buyer ==
W -> R : ciphertext(invoice + PDF syarat) ke kotak surat buyer
note right of W #FFF6D6
USULAN P-04; sekarang salin kode invoice,
PDF dikirim di luar sistem
end note
R -> B : invoice + PDF syarat
B -> B : cek isi dan hash PDF, tanda tangani\n(SEQ-02 bagian 2)
B -> R : buyer_signature (64 byte)
R --> W : buyer_signature
W -> X : bundleBuild({invoice, buyer_signature})
X --> W : bundel; gagal bila tanda tangan buyer\ntidak valid (verify_strict)
note right of W #DDEBFA
PARSIAL: fungsi ADA; belum ada kartu
cek tanda tangan buyer di layar Supplier
end note

== 3. Tawarkan ke satu financier ==
S -> W : pilih financier A (kartu kontak), advance yang diminta
ZW --> S : alamat shielded baru untuk deal ini\n(u1... / utest1...)
W -> R : penawaran {invoice, buyer_signature,\nalamat supplier, advance}
R -> FA : penawaran
FA -> R : pembuka komitmen {financier_pk, salt 32 byte},\nkelas diskon/tenor, surat JTSA + PDF surat\n(SEQ-03 bagian 1b, sebelum Flow::new)
note right of FA #E7F3EA
ADA (HNK-27.T1, DEV-14): salt diturunkan dari
key financier dan N, jadi retry memberi
komitmen yang sama; kelas dari deal_classes
end note
R --> W : pembuka komitmen, kelas, surat + PDF surat
opt buyer memakai riwayat (HNK-20)
  FA -> R : minta riwayat (SEQ-03 bagian 2)
  R -> B : permintaan riwayat (SEQ-02 bagian 3)
  B -> R : sertifikat k untuk invoice ini
  R --> W : sertifikat k
  note right of W #FDECEC
  Pemegang sertifikat k bisa menghitung tag
  invoice buyer berikutnya (TM #6)
  end note
end
FA -> P : cek papan untuk N (SEQ-03 bagian 3)
P --> FA : N belum ada
FA -> R : minta entri bertanda tangan\n(+ history_tag yang akan dicocokkan)
R --> W : permintaan entri

== 4. Tanda tangani entri papan untuk financier A ==
W --> S : tampilkan: N, financier, advance, kelas, tag riwayat
S -> W : "Tanda tangani entri"
W -> A : verifikasi pengguna (USULAN P-01, P-03, P-07)
A --> W : PRF (stempel)
alt buyer tanpa riwayat
  W -> X : supplierRegisterEntry(secret, invoice,\nfinancier_pk, salt)
else buyer dengan riwayat (HNK-20)
  W -> X : supplierRegisterHistoryEntry(secret, invoice,\nfinancier_pk, salt, sertifikat k)
end
X --> W : {memo 512 byte (entri JTS1 136/168 byte\n+ padding nol), commitment}
note right of W #DDEBFA
PARSIAL: fungsi wasm ADA, dengan kelas opsional
(HNK-27.T2) dan varian dari history_tag saja
(supplierRegisterTaggedEntry, HNK-27.T8); kartu di
layar supplier belum (HNK-24.T6)
end note
W -> R : entri bertanda tangan
R -> FA : entri
FA -> Z : posting entri ke papan (10 000 zat + fee, memo)
Z -> P : entri tertambang
FA -> FA : tunggu >= min_confirmations

== 5. Segel surat pengalihan ==
note over W : surat JTSA dan PDF surat diterima di bagian 3\n(N, nominal, jatuh tempo, financier_pk,\nalamat bayar financier, terms_hash surat)
W -> X : assignmentStatus(invoice, surat, [])
X --> W : surat cocok dengan invoice (nominal dan\njatuh tempo dipaksa sama); langkah berikut = Supplier
S -> W : buka PDF surat
W -> X : documentHash(PDF surat) = terms_hash surat?
note right of W #DDEBFA
PARSIAL: assignmentDecode ADA di wasm (HNK-27.T3);
layar supplier belum menampilkan alamat bayar,
financier_pk, dan terms_hash, dan belum punya
input PDF (HNK-24.T7)
end note
S -> W : "Segel sebagai supplier"
W -> A : verifikasi pengguna (USULAN P-07)
A --> W : PRF (stempel)
W -> X : supplierSealAssignment(secret, invoice, surat)
X --> W : seal s0 (JTL1, 200 byte, langkah 0, role Supplier)
W -> R : s0 ke buyer dan financier A
R -> B : s0
R -> FA : s0
B -> R : s1 (seal buyer, SEQ-02 bagian 4)
R -> FA : s1
R -> W : s1 (salinan untuk supplier)

== 6. Terima advance (Sign-to-Pay) ==
FA -> Z : advance shielded ke alamat supplier;\nmemo = kuitansi advance + seal s2 + catatan piutang
Z -> ZW : note shielded masuk
FA -> R : txid advance (petunjuk)
R --> W : txid
alt verifikasi kuat (USULAN: jalur supplier; fungsi ADA)
  CL -> Z : sync wallet watch-only supplier sendiri
  Z --> CL : output + memo tx advance
  CL -> CL : received_advances: kuitansi JTR1, signer = financier_pk,\nnominal = nilai output = advance yang disepakati;\nverify_sign_to_pay: [s0, s1] + s2 dari memo = Sealed
  note right of CL #FFF6D6
  Fungsi jitsuin-flow hanya dipanggil unit test:
  belum ada perintah CLI, export wasm, atau API.
  Di luar browser: wasm tanpa jaringan dan
  connect-src 'self'. UFVK supplier tidak ke server
  (P-10). Pembanding advance yang disepakati ADA
  (verify_sign_to_pay, HNK-27.T7)
  end note
else hanya lewat relay (jalur lemah)
  W -> X : assignmentStatus(invoice, surat,\n[s0, s1, s2 dari memo lewat relay])
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
W -> X : bundleOnBoard(bundel JTSB dengan surat +\ndokumen pelunasan dari financier, snapshot)
X --> W : register = Registered, settled = {on_time}

== Jalur supplier nakal ==
group menawarkan invoice yang sama ke financier B
  S -> R : penawaran yang sama ke financier B
  R -> FB : invoice + buyer_signature
  FB -> R : pembuka komitmen B + minta entri bertanda tangan\nsebelum cek papan (kebijakan B, USULAN P-14)
  S -> R : entri bertanda tangan untuk komitmen B
  R -> FB : entri B
  FB -> P : cek papan dengan key supplier dari invoice
  P --> FB : entri A sudah lebih dulu, tanda tangan valid
  FB -> FB : berhenti sebelum membayar (AlreadyFinanced)
  FB -> FB : susun bukti: entri A dengan posisi di papan\n+ entri B (proof_from_offer di jitsuin-board)
  FB -> V : bukti tanda tangan ganda (JTSP)
  FB --> S : penawaran ditolak
  note right of FB #FDECEC
  Tanpa entri B (Flow sekarang meminta entri hanya
  setelah NotFound), B hanya tahu invoice sudah
  dibiayai, tanpa bukti. wasm doubleSignProof kini
  menerima posisi papan (HNK-27.T4).
  JTSP membuktikan dua tanda tangan, bukan niat menipu
  (lihat risiko P-14 di FD-00)
  end note
end

== Mode confidential (USULAN, roadmap) ==
note over S, FA #FFF6D6
Surat disegel Supplier lalu Financier saja (buyer tidak diberi tahu);
buyer membayar ke supplier, supplier meneruskan ke financier dengan
kuitansi bertanda tangan supplier; settled ditandatangani supplier
+ financier. Belum diimplementasikan (Mode Confidential)
end note
@enduml
```

## Ringkasan langkah dan status

| Bagian | Langkah | Status | Kode |
|---|---|---|---|
| 1 | Key per invoice acak + unduh backup | ADA (akan diganti) | `src/pages/supplier.ts` `downloadSecret` |
| 1 | Key per invoice dari master supplier (passkey supplier) | USULAN P-01, P-03 | — |
| 1 | Hash file syarat di browser | ADA | wasm `documentHash` |
| 1 | Invoice kanonik dan N | ADA | wasm `invoiceEncode`, `invoiceDecode` |
| 2 | Kirim invoice + PDF syarat dan terima tanda tangan lewat relay | USULAN P-04 | sekarang salin-tempel; PDF di luar sistem |
| 2 | Cek tanda tangan buyer | PARSIAL: `bundleBuild` sudah memeriksa; kartu di layar Supplier belum ada | wasm `bundleBuild` |
| 3 | Penawaran, pembuka komitmen, surat + PDF surat, sertifikat k | USULAN P-04, P-08 | — |
| 4 | Tanda tangani entri register (dengan atau tanpa tag riwayat) | PARSIAL: wasm ADA (kelas opsional, varian tag saja; HNK-27), layar dan passkey supplier USULAN P-01, P-03, P-07 | wasm `supplierRegisterEntry`, `supplierRegisterHistoryEntry` |
| 5 | Segel surat pengalihan | PARSIAL: seal ADA; isi surat dan cek PDF surat USULAN P-13; passkey supplier USULAN P-07 | wasm `supplierSealAssignment`, `assignmentStatus` |
| 6 | Verifikasi Sign-to-Pay | PARSIAL: fungsi ADA (hanya unit test); jalur kuat lewat CLI lokal USULAN; lewat relay saja lemah | `jitsuin-flow::supplier::received_advances`, `verify_sign_to_pay` |
| 7 | Status pelunasan dari papan | PARSIAL | wasm `bundleOnBoard` (butuh bundel lengkap dan snapshot papan, P-06) |
| Nakal | Bukti tanda tangan ganda ke pihak berwenang | PARSIAL: butuh entri B sebelum cek papan (P-14); wasm dengan posisi papan ADA (HNK-27.T4) | `jitsuin_board::proof_from_offer`, wasm `doubleSignProof` |
