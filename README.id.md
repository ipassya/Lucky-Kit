# Lucky Kit

[![CI](https://github.com/ipassya/Lucky-Kit/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/ipassya/Lucky-Kit/actions/workflows/validate.yml)
[![Rilis](https://img.shields.io/github/v/release/ipassya/Lucky-Kit?label=rilis)](https://github.com/ipassya/Lucky-Kit/releases/latest)

**Ubah ide aplikasi, dokumen yang sudah ada, atau codebase menjadi rencana implementasi yang jelas.**

[English](README.md) · [Instalasi](docs/installation.md) · [Unduh v1.0.0 (ZIP)](https://github.com/ipassya/Lucky-Kit/releases/download/v1.0.0/lucky-kit-v1.0.0.zip) · [Kontribusi](CONTRIBUTING.md)

Lucky Kit adalah kumpulan instruksi AI yang dapat digunakan kembali untuk perencanaan produk dan dokumentasi. Skill ini membantu founder, tim produk, dan developer menghubungkan kebutuhan, alur pengguna, desain, data, dan tugas implementasi. Mulai dari informasi yang tersedia; keputusan yang belum selesai tetap dicatat.

## Hasil yang diperoleh

| Titik awal | Hasil yang berguna |
| --- | --- |
| Ide aplikasi | Spesifikasi yang relevan, milestone berurutan sesuai dependensi, dan tasks untuk versi pertama yang scope-nya jelas, beserta asumsi dan blocker |
| Dokumen yang sudah ada | Kebutuhan dan desain yang selaras, dengan konflik diidentifikasi dan diselesaikan |
| Codebase yang berjalan | Dokumentasi perilaku yang teramati, beserta bukti dan batas cakupannya |
| Spesifikasi siap | Handoff implementasi berisi tugas, dependensi, dan kriteria penerimaan |

Perencanaan aplikasi otomatis membuat dan memperbarui dokumen di workspace aplikasi setelah lokasi dan tujuan dasarnya jelas. Kamu gak perlu meminta penyimpanan secara terpisah. Kalau lokasinya belum jelas, Lucky Kit menanyakannya sambil melanjutkan penggalian kebutuhan. Permintaan khusus diskusi saja atau review saja tetap di chat; tanpa akses file, skill memberikan isi dokumen dan menjelaskan bahwa hasil belum disimpan. Review atau dokumentasi aplikasi gak otomatis mengizinkan perubahan kode.

Satu prompt ide secara default memulai persiapan implementasi. Project brief menjadi draft awal atau spesifikasi lengkap untuk proyek kecil. Lucky Kit melanjutkan dokumentasi yang relevan dan rencana delivery tanpa menunggu prompt terpisah untuk tiap artefak. Setiap milestone punya hasil dan kriteria selesai; setiap task punya ID, hasil, rujukan kebutuhan, dependensi, kriteria penerimaan, metode verifikasi, dan status kesiapan atau blocker. Task berikutnya yang siap dikerjakan mendapat handoff. Permintaan eksplorasi saja, brief saja, review, atau dokumen tertentu tetap mengikuti batasnya.

Lucky Kit punya penggalian kebutuhan terarah seperti grill-me. Skill membahas skenario konkret, menguji asumsi, dan menelusuri konsekuensi pertanyaan yang diperlukan, biasanya satu keputusan per giliran. Jawaban yang sudah ada dipakai kembali, sementara dokumentasi yang gak bergantung pada jawaban dilanjutkan dengan asumsi yang jelas dan bisa diubah. Keputusan penting yang belum selesai memblokir task terkait. Kalau konteks cukup, wawancara gak wajib; usulan yang belum disepakati gak dianggap sudah disetujui atau siap tanpa syarat. Gak perlu skill wawancara terpisah.

Lucky Kit memilih file berdasarkan siapa yang memakainya serta keputusan atau pekerjaan yang dibantu. Dokumen yang masih berguna diperbarui, dan topik substansial dipisahkan ketika membantu implementasi atau pemeliharaan. PRD (Product Requirement Documentation), TRD (Technical Requirement Documentation), AFD (App Flow Documentation), DBD (Design Brief Documentation), BSD (Backend Schema Documentation), dan IPD (Implementation Plan Documentation) adalah pilihan format, bukan paket wajib. Proyek kecil bisa memakai satu spesifikasi lengkap beserta rencana delivery; proyek lebih besar mendapat dokumen terpisah sesuai kebutuhan. Permintaan khusus skema atau handoff gak otomatis menambah dokumen pendamping.

Persiapan implementasi mencakup seluruh versi pertama yang direncanakan, termasuk tasks setelah task awal. Draft perencanaan yang lengkap masih bisa punya blocker; Lucky Kit melaporkannya dan menunjukkan pekerjaan yang bisa dimulai secara independen. Kelengkapan rencana gak membuktikan persetujuan, implementasi, keberhasilan pengujian, atau kesiapan produksi.

Setiap pembuatan atau perubahan mengikuti konvensi workspace, menjaga keputusan yang menjadi acuan, meninjau isi serta dokumen terdampak, dan menjalankan pemeriksaan sesuai perubahan. Dalam repo Git yang sudah tersedia, Lucky Kit otomatis melakukan commit untuk satu pembaruan tugas yang utuh dan sudah divalidasi, kecuali kamu atau aturan workspace meminta sebaliknya. Perubahan lain tetap dijaga; perubahan yang bercampur dilaporkan sebagai hambatan, bukan ikut dimasukkan. Skill gak otomatis menginisialisasi Git atau melakukan push. Tanpa Git, dokumen tetap disimpan dan status tanpa commit dilaporkan.

Perubahan yang bercampur dalam satu file perlu dipisahkan per bagian; memilih seluruh file saja belum cukup. Hook yang gagal tetap diaktifkan, dan permintaan eksplisit jangan commit membuat perubahan tugas tetap belum di-commit maupun di-stage. Commit baru dilaporkan setelah isi aktualnya diperiksa.

## Mulai menggunakan

1. Salin isi [SKILL.md](skills/lucky-kit/SKILL.md) ke chat AI, atau lampirkan jika platform mendukung pembacaan file.
2. Salin template berikut. Ganti bagian dalam kurung; isi **“belum ditentukan”** jika belum tahu.
3. Kirim bersama materi yang relevan dan lokasi workspace aplikasi. Berikan file rujukan saat diminta; dokumen perencanaan disimpan di sana jika akses file tersedia.

### Template siap salin

Ide dan workspace aplikasi sudah cukup untuk mulai. Field lain membantu menjaga keputusanmu; kamu gak perlu menyebut jenis dokumen atau mengisi semua field.

```text
Gunakan Lucky Kit untuk merencanakan [aplikasi] bagi [pengguna], guna menyelesaikan
  [masalah].
Alur utama: [pemicu → tindakan → hasil].
MVP: [fitur wajib versi pertama]. Di luar scope: [pengecualian].
Platform dan desain: [web/mobile/lainnya; kebutuhan visual atau design system yang
  tersedia].
Data dan integrasi: [data yang dicatat, sumber, aturan akses, layanan eksternal].
Batasan: [budget, tenggat, stack, atau kebutuhan lain].
Materi tersedia: [belum ada, dokumen, desain, atau kode; lokasi jika bisa diakses].
Hasil: spesifikasi yang relevan, milestone, dan tasks sampai persiapan implementasi.
  [Ganti hanya kalau menginginkan hasil yang lebih terbatas.]
Workspace aplikasi: [lokasi tujuan; atau minta khusus diskusi di chat saja].
Gunakan keputusan yang sudah ada, gali kekurangan informasi dan trade-off penting,
  serta perbarui dokumen seiring jawaban diperoleh. Lanjutkan dengan asumsi yang jelas
  jika masuk akal; tandai blocker penting dan tuntaskan perencanaan yang independen.
```

### Contoh: aplikasi keuangan pribadi

```text
Gunakan Lucky Kit untuk merencanakan aplikasi keuangan pribadi bagi freelancer yang
  perlu mencatat pemasukan tidak tetap.
Alur utama: tambah pemasukan atau pengeluaran → perbarui saldo dompet → tinjau budget
  bulanan.
MVP: transaksi manual, dompet, kategori, budget bulanan. Di luar scope: sinkronisasi
  bank, pembayaran, investasi.
Platform dan desain: web yang nyaman di ponsel; dashboard sederhana dan pencatatan
  transaksi yang cepat.
Data dan integrasi: catatan pribadi per pengguna dalam Rupiah; login email; tanpa
  koneksi bank.
Batasan: MVP 6 minggu, hosting maksimal Rp500.000/bulan; stack belum ditentukan.
Materi tersedia: baru ide.
Workspace aplikasi: [path workspace aplikasi keuangan pribadi saya].
Hasil: seluruh dokumen perencanaan yang relevan, milestone, dan tasks untuk MVP ini,
  termasuk dependensi, kriteria penerimaan, verifikasi, blocker, dan handoff task berikutnya.
  Pisahkan dokumen khusus sesuai kebutuhan; jangan berhenti di project brief.
Gunakan keputusan yang sudah ada, gali kekurangan informasi dan trade-off penting,
  serta perbarui dokumen seiring jawaban diperoleh. Lanjutkan dengan asumsi yang jelas
  jika masuk akal; tandai blocker penting dan tuntaskan perencanaan yang independen.
```

Ganti bidang, pengguna, dan batasan pada contoh untuk merencanakan ide lain. Permintaan berbahasa Indonesia menghasilkan diskusi dan dokumen Indonesia; bahasa lainnya menghasilkan bahasa Inggris.

## Gunakan dengan tool pilihanmu

| Lingkungan | Cara mulai |
| --- | --- |
| Chat AI | Salin instruksi dan permintaan; berikan potongan sumber yang relevan sesuai kebutuhan. |
| Asisten dengan akses proyek | Berikan instruksi dan lokasi proyek: “Dokumentasikan alur dan model data yang sudah diimplementasikan; pisahkan bukti dari usulan.” |
| Agent yang mendukung skill | Pasang seluruh folder `skills/lucky-kit/` di lokasi yang didukung platform, lalu minta agent menggunakan Lucky Kit. |

Instruksi teks dapat dipindahkan antarplatform; pemuatan skill dan akses file mengikuti kemampuan platform. Menuliskan path lokal saja gak memberi chat akses ke file. Kualitas hasil bergantung pada model dan konteks yang tersedia.

Instalasi cukup dengan menyalin folder secara manual. Installer Python dan PowerShell opsional, pembaruan, dan batas verifikasi dijelaskan dalam [panduan instalasi](docs/installation.md). Skill sendiri gak memerlukan runtime atau akun layanan.

## Referensi

- [Panduan kontribusi](CONTRIBUTING.md): struktur paket, penyuntingan, dan pemeriksaan wajib.
- [Keputusan desain](docs/redesign.md): struktur workflow dan pengukuran konteks.
- [Evaluasi perilaku](docs/behavior-evaluation.md): skenario terisolasi yang bisa diulang, bukti Git, dan review penggalian kebutuhan serta kegunaan dokumen.
- [Panduan komunitas](CODE_OF_CONDUCT.md) · [Pelaporan keamanan](SECURITY.md) · [Persiapan rilis](docs/open-source.md).

## Lisensi dan kredit

Dibuat dan dikelola oleh **Ihza Luckyan Passya**. Hak cipta © 2026.

Menggunakan [GPL-3.0-only](LICENSE), dengan [izin hasil generasi](skills/lucky-kit/OUTPUT-LICENSE.md) untuk materi yang tercakup dalam hasil proyek, termasuk penggunaan privat dan komersial. Aplikasi hasil generasi gak wajib memakai branding Lucky Kit. Distribusi ulang skill atau pustaka template tetap mengikuti ketentuan yang berlaku. Lihat [kredit](CREDITS.md).
