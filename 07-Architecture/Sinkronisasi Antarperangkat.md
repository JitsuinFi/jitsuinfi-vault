---
tags: [architecture, security, relay]
status: DIBUAT
updated: 2026-10-27
---

# Sinkronisasi Antarperangkat

**Bagian dari:** [[07 - Architecture]] · Kembali: [[START-HERE]] · Terkait: [[Threat Model]] · [[Format Data]] · [[Arsitektur JitsuinFi]] · [[Rencana Akun Server]]

> Temuan F10 dari E2E "messy" 2026-10-27. Branch frontend `hans/device-sync` (belum di-push). Kode: `src/lib/sync.ts` (format, aturan merge, batas ukuran), `src/lib/device-sync.ts` (kapan sinkron), `src/lib/drafts.ts` + `src/app/kept.ts` (form tahan reload).

## Masalahnya
Invoice, deal, key yang sudah dipakai, dan kontak hanya ada di store terenkripsi perangkat (IndexedDB, `src/lib/store.ts`). Akun yang sama di perangkat kedua (passkey yang sama, disinkron iCloud/Google) melihat ledger kosong, tidak bisa Pay, dan bisa memberikan key buyer yang sudah dipakai di perangkat lain.

## Desainnya
- **Tempat:** state per mailbox yang sudah ada di relay (`PUT/GET /api/mailbox/:id/state`, hanya pemilik yang menulis dan membaca, maks 64 KiB + 48 tersegel). **Tidak ada endpoint baru.** Satu state per peran (supplier, buyer, member), karena tiap peran punya mailbox sendiri.
- **Isi:** seluruh record store peran itu: supplier (deal, ref, key buyer yang masuk, kartu dari surat key, alamat advance terakhir, kontak), buyer (invoice beserta surat, seal, bundle, slip; rantai riwayat; key yang sudah diberikan; kontak), member (wallet: holding, token tarik, payout; kontak).
- **Kapan:** setelah tiap perubahan store (debounce 1,2 detik), saat sign-in, saat tab kembali terlihat atau fokus, saat perangkat online lagi, dan tiap 60 detik selama tab terlihat. Satu putaran: baca state relay → merge dengan record lokal → tulis yang baru ke store lokal → kirim hasil merge bila state relay belum memuatnya.
- **Account menu:** satu baris tenang, "Synced with your other devices · just now", atau "Not synced yet: this device is offline".

## Format (versi 2, "JSY2")
```
sealed box (mailboxSeal ke mailbox key milik sendiri)
  └ "JSY2" | iv (12) | AES-256-GCM( gzip( JSON SyncState ) ), AAD "jitsuinfi-sync-v2:<peran>"

SyncState = { v: 2, role, written_at, records: [{ id, at, doc }], held_back, slimmed }
```
- Kunci dalam = HMAC-SHA-256(output PRF inbox, `jitsuin/<peran>/sync/v1`), WebCrypto non-extractable, hanya ada selama sesi.
- `at` = waktu tulis terakhir record di perangkat yang menulisnya (monoton di perangkat itu: selalu lebih besar dari `at` mana pun yang pernah dilihat store). `doc: null` = tombstone (hapus).
- Versi 1 (salinan riwayat buyer `{v:1, certs}`, HNK-25.T2) tetap terbaca sebagai record `history` dengan `at = 0`.

## Aturan merge
| Record | Aturan |
|---|---|
| Semua | Per record, `at` lebih baru menang; seri → JSON kanonik lebih besar (semua perangkat memilih sama). Record yang tidak ada di state = tidak diketahui, **bukan** dihapus |
| Invoice buyer (`invoice:N`) | Pemenang + semua yang tidak boleh hilang dari sisi lain: tanda tangan, waktu kirim, `reply_to`, bundle, sertifikat riwayat, surat + PDF-nya, ketiga seal (hanya untuk surat yang sama), `terms_checked` (OR), `reminders_seen` (gabungan), `received_at` (paling awal) |
| Deal supplier (`N`) | Pemenang + tanda tangan buyer, sign request, entry request, entry, surat masuk, seal, bundle, advance. Offer dari sisi lain kembali **hanya** bila financier itu belum menolak sejak offer dikirim |
| Key yang diberikan (`keys:given`) | Himpunan (k, penerima); tidak pernah dihapus |
| Wallet member (`fund:wallet`) | Holding digabung per leaf (leaf baru hasil payout menggantikan leaf lama dari deposit yang sama), payout per txid |
| Kontak | Pemenang, `verified_at` dipertahankan |
| Riwayat buyer (`history`) | LWW di state, tetapi **tidak** ditulis otomatis ke store lokal: dipulihkan di layar key setelah dicek ke board (perilaku lama) |

## Key buyer lintas perangkat
- Layar "Your next invoice key" membaca record tersinkron sebelum menawarkan key: invoice yang sudah menyebut key #k memberi peringatan yang sama seperti di perangkat asal; key yang sudah diberikan (dikirim atau disalin) disebut penerimanya dan tanggalnya.
- Sertifikat riwayat yang diterbitkan perangkat lain menaikkan key yang ditawarkan (`keyAfterOtherDevices`), juga bila board tidak terbaca, karena state ditandatangani kunci akun ini. E2E: perangkat 2 menawarkan key **#1**, bukan #0.
- Key tetap tidak maju sebelum invoicenya dibiayai (indeks key = indeks sertifikat), jadi "key #0 sudah dipakai, belum dibiayai" tetap #0 dengan peringatan, sama di semua perangkat.

## Batas ukuran (64 KiB)
1. JSON di-gzip (`CompressionStream`). Satu invoice tanpa PDF sekitar 1–2 KB.
2. Masih terlalu besar → byte PDF dikeluarkan dulu; nama, SHA-256, dan ukurannya tetap. Perangkat tanpa PDF menulis "PDF on your other device" dan meminta file dipilih untuk dicek (PDF dummy 127 KB selalu dikeluarkan; surat kecil ikut).
3. Masih terlalu besar → record selesai paling lama (punya bundle) dikeluarkan dulu, lalu yang paling lama lainnya; jumlahnya di `held_back`. Riwayat dan `keys:given` tidak pernah dikeluarkan. Record yang ditahan tetap di perangkat yang memilikinya.
- **Belum ada:** meminta PDF dari perangkat lain lewat relay. Sekarang pengguna memilih file lagi (dicek dengan hash) atau bertindak di perangkat asal.

## Form tahan reload
Write an invoice, kode "by hand" buyer, form stasiun (offer: financier, advance, alamat; konfirmasi advance), deposit dan permintaan tarik member. Draft disimpan per akun + layar di `sessionStorage` tab ini, **terenkripsi** AES-GCM dengan kunci HMAC(PRF inbox, `jitsuin/<peran>/drafts/v1`), layar sebagai AAD. Setelah reload dan sign-in lagi, form terisi kembali. File yang dipilih tidak bisa bertahan: hanya nama, ukuran, SHA-256; form meminta file dipilih ulang. Draft dihapus saat aksi berhasil, "Start over"/Cancel, Sign out, dan saat tab ditutup.

## Keamanan dan kebocoran
- Semua yang disinkron disegel ke kunci pemilik dan dienkripsi kunci dalam yang hanya bisa diturunkan dari passkey. Relay hanya melihat **ciphertext, ukurannya, dan waktunya**.
- Segel luar saja tidak cukup: mailbox key publik (ada di kartu kontak), jadi siapa pun, termasuk relay, bisa menyegel state palsu. AEAD dalam menolak state yang tidak dibuat pemilik passkey.
- **Bocor:** (1) ukuran state ≈ jumlah record dan apakah PDF ikut; (2) waktu tulis ≈ kapan pemilik bekerja dan berapa perangkat aktif (tulis tiap perubahan, baca tiap menit saat tab terlihat); (3) relay bisa menahan atau mengembalikan state lama (rollback). Merge tidak pernah membiarkan record lama menimpa yang baru, jadi rollback hanya bisa menyembunyikan record dari perangkat baru, tidak menghapus atau membatalkan; menu menulis "the relay handed back an older copy".
- Draft di `sessionStorage` terenkripsi; plaintext hanya di memori.
- Konflik bersamaan: dua perangkat menulis hampir bersamaan → PUT terakhir menang di relay, tetapi perangkat lain menulis ulang hasil merge pada putaran berikutnya (konvergen, diuji).

## Bukti
- `npm test`: 293 lulus (baru: `tests/sync.test.ts` 20, `tests/drafts.test.ts` 6: aturan merge, batas ukuran, key lintas perangkat, restore draft).
- E2E lokal (relay memory store, `vite preview`, passkey bersama disimulasikan dengan shim PRF seperti laporan messy; supplier+financier tiruan di Node untuk sisi buyer). Screenshot: `design-samples/sync/`.
