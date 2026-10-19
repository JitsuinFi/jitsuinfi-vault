---
tags: [flow, sequence, auth]
status: DRAF
updated: 2026-10-19
---

# SEQ-00 - Autentikasi dan Onboarding

**Bagian dari:** [[08 - FlowDiagrams]] · Legenda dan usulan: [[FD-00 - Arsitektur Target dan Legenda]] · Dipakai oleh: [[SEQ-01 - Supplier]] · [[SEQ-02 - Buyer]] · [[SEQ-03 - Financier]] · [[SEQ-05 - Anggota Dana]] · DFD: [[DFD-2.1 - Identitas dan Sesi]]

Alur bersama semua peran yang memegang key: **daftar**, **masuk**, **pilih peran**, **sesi dan stempel**, dan **masuk ke node financier**. Verifier dan orang luar tidak perlu akun ([[SEQ-04 - Verifier dan Orang Luar]]).

Dasar: pola Mera / WebAuthn PRF ([[Desain Jitsuin Seal]] §9). Yang sudah ada di kode: `src/lib/passkey.ts` (salt `jitsuin/buyer/master/v1`, `createPasskey`, `masterFromPasskey`) dan `buyerKeys` di `jitsuin-wasm`. Sisanya usulan P-01, P-02, P-04, P-05, P-07 di [[FD-00 - Arsitektur Target dan Legenda]].

![SEQ-00](assets/seq-00-auth.svg)

```plantuml
@startuml seq-00-auth
!include seq-style.iuml
title SEQ-00 Autentikasi dan onboarding (semua peran yang memegang key)
actor "Pengguna" as U
box "Perangkat pengguna" #FAFBFE
  participant "Web app\n(browser)" as W
  participant "jitsuin-wasm" as X
  participant "Authenticator\npasskey (PRF)" as A
  database "Penyimpanan lokal\n(non-rahasia)" as L
end box
box "Server" #FFFDF5
  participant "Relay dokumen\n(USULAN P-04)" as R
  participant "Node financier\n(PARSIAL)" as NF
end box

== Daftar (P-01, P-02) ==
U -> W : buka /app.html, klik **Daftar**
W -> W : cek PublicKeyCredential + isSecureContext
alt browser tanpa WebAuthn atau bukan HTTPS
  W --> U : "Perangkat tidak mendukung passkey"\n(mode demo: test secret 64 hex, hanya data uji)
end
U -> W : pilih peran: Supplier / Buyer / Financier / Anggota dana
W -> A : navigator.credentials.create()\nrp = jitsuinfi.vercel.app, user.id acak 16 byte,\nresidentKey required, userVerification required,\nextensions.prf = {}
A -> U : minta Face ID / sidik jari / PIN
U -> A : verifikasi
A --> W : credential baru (passkey tersinkron)\n+ prf.enabled
alt prf.enabled = false
  W --> U : "Authenticator tanpa PRF"\n(tidak bisa menurunkan key)
end
note over W #E7F3EA
ADA untuk buyer: createPasskey()
di src/lib/passkey.ts
end note
W -> A : navigator.credentials.get()\nprf.eval.first = SHA-256("jitsuin/<peran>/master/v1")\nprf.eval.second = SHA-256("jitsuin/<peran>/inbox/v1")
A -> U : verifikasi lagi
U -> A : verifikasi
A --> W : PRF first (32 byte) + PRF second (32 byte)
W -> X : turunkan key peran dari PRF first
alt peran = Buyer (ADA)
  X --> W : buyerKeys(master, k):\nidentity_pk + invoice_pk(k)\n(keyed BLAKE2b "JitsuinBuyerKey_")
else peran = Supplier (USULAN P-03)
  X --> W : master supplier; key per invoice nanti =\nBLAKE2b(key = master, invoice_id)
else peran = Financier (USULAN P-05)
  X --> W : tidak ada key tanda tangan di browser;\nkey financier tinggal di node financier
end
W -> X : key kotak surat X25519 dari PRF second
X --> W : mailbox_pk
W -> R : POST /api/mailbox {mailbox_pk, bukti kepemilikan}\n(same-origin, P-11)
note over R #FFF6D6
USULAN P-04: server hanya menyimpan
mailbox_pk, id kotak surat, dan
ciphertext; tanpa nama, email, IP log
end note
R --> W : mailbox_id
W -> L : simpan profil non-rahasia:\nperan, credential id, label\n(try/catch; boleh hilang)
W --> U : kartu kontak: peran, mailbox_id, key publik peran\n(buyer: tanpa identity_pk; invoice_pk diberikan per invoice)
note right of W #FFF6D6
QR dipindai di luar browser atau ditempel:
Permissions-Policy camera=() memblokir kamera
end note

== Masuk (uji stateless) ==
U -> W : klik **Masuk** (perangkat apa pun)
W -> A : credentials.get() discoverable\n(allowCredentials kosong) + prf.eval salt peran
A -> U : verifikasi
U -> A : verifikasi
A --> W : PRF yang sama untuk salt yang sama
W -> X : turunkan ulang key peran
X --> W : key identik dengan saat daftar
note over W, L #E7F3EA
Tidak ada yang dibaca dari server atau localStorage
untuk membangun identitas: localStorage boleh kosong
(perangkat baru, mode private). Profil hanya memudahkan.
end note
W -> R : GET /api/mailbox/<id> (ciphertext baru)
R --> W : daftar ciphertext
W -> X : dekripsi dengan key kotak surat
X --> W : dokumen deal masuk\n(invoice, tanda tangan, surat, seal, ...)

== Pilih peran ==
U -> W : ganti peran (satu orang boleh banyak peran)
W -> A : credentials.get() dengan salt peran lain
A --> W : PRF peran itu
note over W #FFF6D6
USULAN P-02: key tiap peran terisolasi.
SelfApproval di jitsuin-core hanya membandingkan key,
jadi satu orang yang memegang dua peran dengan key
berbeda tidak tertangkap; larangan itu kebijakan
end note

== Sesi dan stempel (P-07) ==
W -> W : simpan key hanya di memori tab
loop setiap tindakan menandatangani (stempel)
  U -> W : klik "Tanda tangani" / "Segel"
  W -> A : credentials.get() userVerification required
  A -> U : verifikasi (satu sentuhan = satu stempel)
  U -> A : verifikasi
  A --> W : PRF
  W -> X : tanda tangani dengan key turunan
  X --> W : tanda tangan / seal
  W -> W : hapus salinan key sementara
end
W -> W : kunci otomatis setelah 15 menit idle\natau tab ditutup: key dihapus dari memori

== Pairing node financier (P-05, sekali saat setup) ==
U -> NF : siapkan node: zcash-devtool init (seed dibuat dan disimpan di node),\nkey financier, init-fvk UFVK papan (watch-only)
note right of NF #FFF6D6 : USULAN; sekarang dijalankan manual lewat CLI (scratchpad cycle-it)
U -> W : buka konsol node, "Pasangkan passkey"
W -> NF : GET /node/pairing/challenge (kode pairing sekali pakai dari layar node)
NF --> W : challenge + kode
W -> A : credentials.create() untuk rp konsol, userVerification required
A -> U : verifikasi
U -> A : verifikasi
A --> W : attestation (public key credential)
W -> NF : POST /node/pairing {attestation, kode}
NF -> NF : simpan public key credential (D9)

== Masuk ke konsol node financier (P-05) ==
U -> W : buka konsol financier
W -> NF : GET /node/session/challenge\n(same-origin, P-11)
NF --> W : challenge acak
W -> A : credentials.get({challenge, allowCredentials = credential financier})
A -> U : verifikasi
U -> A : verifikasi
A --> W : assertion (authenticatorData, clientDataJSON, signature)
W -> NF : POST /node/session {assertion}
NF -> NF : verifikasi signature dengan public key\ncredential yang didaftarkan saat pairing
NF --> W : cookie sesi httpOnly, SameSite=Strict
note over NF #DDEBFA
PARSIAL: Financier (jitsuin-flow) memegang wallet
dan key; API HNK-05.T3 (Dex) belum ada
end note
@enduml
```

## Langkah penting

| No | Langkah | Status | Sumber |
|---|---|---|---|
| Daftar | `create()` dengan ekstensi PRF, cek `prf.enabled` | ADA (buyer) | `src/lib/passkey.ts` `createPasskey` |
| Daftar | `get()` dengan `prf.eval.first = SHA-256("jitsuin/buyer/master/v1")` | ADA (buyer) | `masterFromPasskey` |
| Daftar | Salt untuk supplier, financier, inbox | USULAN P-02 | — |
| Daftar | Turunan key buyer `identity_pk`, `invoice_pk(k)` | ADA | `jitsuin-core::history::BuyerIdentity`, wasm `buyerKeys` |
| Daftar | Key per invoice supplier dari master | USULAN P-03 | menggantikan `downloadSecret` di `src/pages/supplier.ts` |
| Daftar | Kotak surat dan kartu kontak | USULAN P-04 | — |
| Masuk | Key identik di perangkat baru (credential tersinkron yang sama) | Belum diuji | sifat PRF; belum ada kasus di TEST-HNK-10 |
| Sesi | Key hanya di memori modul | ADA (buyer) | U-HNK-10.3 di TEST-HNK-10 |
| Sesi | Satu sentuhan per stempel, kunci 15 menit | USULAN P-07 | — |
| Pairing node | Seed dan key dibuat di node, UFVK papan diimpor, public key credential disimpan | USULAN P-05 | sekarang manual lewat CLI |
| Konsol financier | Assertion passkey ke node, same-origin | USULAN P-05, P-11 | API HNK-05.T3 |

## Catatan keamanan

- Output PRF tidak pernah keluar dari browser dan tidak pernah disimpan. Yang disimpan lokal hanya profil non-rahasia (peran, id credential).
- WebAuthn mengikat passkey ke domain (`rp.id`). Ganti domain = passkey baru = key baru. Domain final harus dipilih sebelum ada pengguna sungguhan.
- Perangkat tanpa PRF (sebagian authenticator lama) tidak bisa memakai alur ini; mode demo memakai test secret 64 karakter hex, hanya untuk data uji berawalan `TES-`, tidak untuk dana sungguhan.
- CSP `connect-src 'self'` memblokir panggilan ke origin lain. Relay dan node harus dijangkau lewat path same-origin (misalnya rewrite Vercel `/api/*` ke relay) atau konsol disajikan oleh node itu sendiri (P-11). Cookie `SameSite=Strict` hanya bekerja di origin yang sama.
- Kartu kontak buyer tidak memuat `identity_pk`: siapa pun yang memegangnya bisa menghitung tag riwayat pertama buyer ([[Threat Model]]).
