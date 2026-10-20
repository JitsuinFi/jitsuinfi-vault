---
tags: [design-ref, "DS-07"]
type: design-ref
id: DS-07
source_file: 9a7830b313c0c7b0d4eb3323a2052503.jpg
kind: timeline-app
mode: operate
creator: RON Design (logo di gambar)
updated: 2026-10-20
---

# DS-07 - Cardiology Timeline Tree

> **Peta link:** [[DS-00 - Peta Visual Design|Peta visual]] · [[09 - Design|Hub modul]] · [[DS-PAL - Palet Utama JitsuinFi|Palet utama]]

![DS-07](9a7830b313c0c7b0d4eb3323a2052503.jpg)

## 1. Identitas
| | |
|---|---|
| File | `09-Design/9a7830b313c0c7b0d4eb3323a2052503.jpg`, 1200×1200 |
| Jenis | Shot konsep aplikasi riwayat pasien kardiologi, dalam bingkai tablet abu-abu tua |
| Pembuat | Logo "RON DESIGN" di kanan atas (kemungkinan studio yang sama dengan [[DS-06 - Automatic Payment Moss]]) |
| Mode | **Operate** (membaca riwayat dan sebab-akibat) |

## 2. Yang terlihat (apa adanya)
- **Kepala berbentuk tab map dokumen:** label "Cardiology" berada di tonjolan tab yang menyatu dengan bingkai, tombol tutup bulat di kiri.
- **Tab pill:** Treatment Dynamics (aktif putih, ikon kaca pembesar), Visits, Medications, Labs, Allergies, Genetics.
- **Kartu pasien:** foto, "Female, 24", "Tiffany Woodward".
- **Diagnosis "Hypertension"** dan tanda vital: Heart Rate `89 bpm`, Pressure `100/67`, Oxygen `98 %`, Temperature `36.8 °C`.
- **Chip penyaring:** Office Visits, Medications, Labs (aktif putih), Procedures, Hospitalizations, Imaging (nonaktif abu-abu); tombol pengaturan.
- **Garis waktu horizontal** bergradasi (merah ke hijau) dengan **simpul kuning neon** (ikon dokumen) di Aug dan Sep; tombol "+" hitam di ujung kanan.
- **Pohon cabang** dari tiap simpul (garis tipis bersudut membulat) ke:
  - pill obat abu-abu: "Aspirin x2"; "bisoprolol x3", "Aspirin x2";
  - kartu **Blood Pressure**: grafik gelombang dengan pita kuning, penanda gelap `180 / 120` (Friday), Average `160 / 110`, `+10` merah; bulan berikutnya `135 / 92` (Thursday), Average `130 / 90`, `-20`;
  - kartu **Symptoms** (Headache, siluet tubuh dengan titik merah) dan **ECG** (garis jantung).
- **Sumbu minggu vertikal** ("I Week", "II Week") dengan tombol naik/turun.
- **Scrubber waktu bawah:** Jan 2022 → Sep, ikon kunjungan, obat, lab dengan lencana jumlah (6, 2, 3 …); **jendela gelap** memilih rentang Aug – Sep.

## 3. Style
- **Klinis tetapi hangat:** abu-abu kehangatan kertas `#DFDFD7` + putih + abu tua, **satu aksen kuning neon** untuk peristiwa.
- **Diagram alir sebagai UI:** garis penghubung bersudut membulat, cabang dari garis waktu.
- **Siluet map berkas** pada bingkai: aplikasi = map dokumen.
- Kartu radius besar dengan ikon timbangan di sudut; pill obat dengan ikon di lingkaran putih.

## 4. POV dan komposisi
- **Kamera:** tablet tampak depan lurus, latar gradasi abu terang.
- **Sumbu:** waktu mengalir kiri → kanan (garis atas) dan diperbesar ke bawah (minggu). Dua dimensi waktu dalam satu kanvas.
- **Fokus dan konteks:** kanvas besar = rentang yang dipilih; scrubber bawah = seluruh tahun dengan jendela pilihan.
- Kanvas terpotong di kiri dan kanan: tersirat **kanvas tak berujung** yang digeser.

## 5. Makna
- **Riwayat sebagai sebab-akibat:** obat (sebab) bercabang ke tekanan darah (akibat); `+10` lalu `-20` menceritakan perbaikan.
- **Simpul kuning = peristiwa yang tercatat**, garis = waktu yang tidak bisa diulang.
- Map berkas = rekam medis resmi.

## 6. Warna terukur
| Hex | Peran yang terlihat | Calon token |
|---|---|---|
| `#DFDFD7` | Kanvas | `--raw-color-stone-200` → `--background` |
| `#F1F1F0` / putih | Kartu, tab aktif, chip aktif | `--surface-raised` |
| `#5B5C59` | Bingkai, tombol gelap, jendela scrubber | `--raw-color-stone-700` → `--surface-inverse` |
| `#8B8D8C` | Pill obat, chip nonaktif | `--surface-muted` |
| `#F3FE51` | Simpul peristiwa, pita grafik | `--raw-color-neon-yellow-300` → `--state-event` |
| Merah dan hijau tipis | Gradasi garis waktu, delta | `--delta-up`, `--delta-down` |

Kontras: kuning `#F3FE51` hanya sebagai latar ikon gelap (baik); teks abu kecil di atas `#DFDFD7` lemah.

## 7. Tipografi
- Sans geometris bersih (mirip "Gilroy" atau "Urbanist"; tidak terverifikasi). Judul "Cardiology" ±28 px, diagnosis ±20 px, angka vital ±20 px dengan satuan kecil, label ±9 px.

## 8. Komponen terdeteksi
| Komponen | Fungsi | Catatan |
|---|---|---|
| Kepala tab map | Identitas dokumen | Bentuk tab menyatu dengan bingkai |
| Deret tanda vital | Ringkasan keadaan sekarang | Label kecil di atas angka |
| Chip penyaring on/off | Lapisan data yang tampil | Putih = tampil |
| **Garis waktu bercabang** | Peristiwa dan akibatnya | Simpul neon, konektor bersudut membulat |
| Kartu grafik dengan penanda | Satu metrik per periode | Rata-rata + delta |
| Pill entitas | Obat dan dosis | Ikon di lingkaran putih |
| **Scrubber rentang** | Navigasi seluruh tahun | Jendela gelap, lencana jumlah per bulan |

## 9. Gerak yang tersirat
- `Handle`: kanvas digeser horizontal; jendela scrubber diseret mengubah rentang.
- `Inview`: cabang tergambar dari simpul ke kartu; grafik gelombang mengalir.
- `SpringTrigger`: memilih bulan memusatkan kanvas pada simpulnya.
- `Hover`: simpul membesar, tooltip tanggal.

## 10. Relevansi untuk JitsuinFi
| Bisa diambil | Ke mana |
|---|---|
| **Garis waktu bercabang** | Riwayat buyer: rantai sertifikat 0..k yang tertambat di papan, tiap simpul = invoice, cabang = tepat waktu/terlambat/gagal (HNK-20, HNK-25.T6, bab 5 landing "Paid and remembered") |
| Simpul peristiwa di garis waktu deal | Timeline per N: ditandatangani, ditawarkan, terdaftar, disegel, advance, lunas (HNK-24.T9) |
| Scrubber rentang dengan lencana jumlah | Menelusuri papan publik per tinggi blok atau per bulan (Verify, Indeks) |
| Kepala berbentuk tab map | Metafora dokumen berkas, cocok dengan "lembar" dan surat pengalihan di `MASTER.md` |
| Chip lapisan data on/off | Verify: tampilkan atau sembunyikan lapisan bukti |

| Bertentangan | Alasan |
|---|---|
| Foto dan nama pasien | Identitas; data sensitif |
| Kuning neon `#F3FE51` | Tidak ada di [[DS-PAL - Palet Utama JitsuinFi]]; padanan peristiwa: segel Dark Raspberry di kertas, Button Blue di dalam "air" |
| Kartu grafik sebagai wadah | Landing melarang kartu |

## 11. Pertanyaan terbuka
- Pola pohon garis waktu ini dipakai untuk riwayat buyer di app atau di landing bab 5?
