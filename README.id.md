# Lucky Kit

[![CI](https://github.com/ipassya/Lucky-Kit/actions/workflows/validate.yml/badge.svg?branch=main)](https://github.com/ipassya/Lucky-Kit/actions/workflows/validate.yml)
[![Rilis](https://img.shields.io/github/v/release/ipassya/Lucky-Kit?label=rilis)](https://github.com/ipassya/Lucky-Kit/releases/latest)

**Ubah ide aplikasi, dokumen yang sudah ada, atau codebase menjadi rencana implementasi yang jelas.**

[English](README.md) · [Instalasi](docs/installation.md) · [Unduh v1.0.0 (ZIP)](https://github.com/ipassya/Lucky-Kit/releases/download/v1.0.0/lucky-kit-v1.0.0.zip) · [Kontribusi](CONTRIBUTING.md)

Lucky Kit adalah kumpulan instruksi AI yang dapat digunakan kembali untuk perencanaan produk dan dokumentasi. Skill ini membantu founder, tim produk, dan developer menghubungkan kebutuhan, alur pengguna, desain, data, dan tugas implementasi. Mulai dari informasi yang tersedia; keputusan yang belum selesai tetap dicatat.

## Hasil yang diperoleh

| Titik awal | Hasil yang berguna |
| --- | --- |
| Ide aplikasi | Brief proyek berisi scope, alur utama, batasan, dan keputusan terbuka |
| Dokumen yang sudah ada | Kebutuhan dan desain yang selaras, dengan konflik diidentifikasi dan diselesaikan |
| Codebase yang berjalan | Dokumentasi perilaku yang teramati, beserta bukti dan batas cakupannya |
| Spesifikasi siap | Handoff implementasi berisi tugas, dependensi, dan kriteria penerimaan |

Proyek kecil dimulai dengan satu brief. Dokumen produk, alur, desain, teknis, data, dan rencana pengerjaan dipisahkan sesuai kebutuhan. Review atau dokumentasi aplikasi gak otomatis mengizinkan perubahan kode.

## Mulai menggunakan

1. Salin isi [SKILL.md](skills/lucky-kit/SKILL.md) ke chat AI, atau lampirkan jika platform mendukung pembacaan file.
2. Salin template berikut. Ganti bagian dalam kurung; isi **“belum ditentukan”** jika belum tahu.
3. Kirim bersama materi yang relevan. Berikan file rujukan saat diminta; simpan hasil di workspace aplikasi yang dikerjakan.

### Template siap salin

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
Hasil: [brief, spesifikasi selaras, dokumentasi kondisi aktual, atau handoff]; [chat
  atau lokasi tujuan].
Gunakan keputusan yang sudah ada, tandai kekurangan informasi, dan tanyakan hanya hal
  yang menghambat pekerjaan.
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
Hasil: brief di chat berisi scope, alur, kebutuhan data, kriteria penerimaan, dan
  keputusan terbuka.
Gunakan keputusan yang sudah ada, tandai kekurangan informasi, dan tanyakan hanya hal
  yang menghambat pekerjaan.
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
- [Panduan komunitas](CODE_OF_CONDUCT.md) · [Pelaporan keamanan](SECURITY.md) · [Persiapan rilis](docs/open-source.md).

## Lisensi dan kredit

Dibuat dan dikelola oleh **Ihza Luckyan Passya**. Hak cipta © 2026.

Menggunakan [GPL-3.0-only](LICENSE), dengan [izin hasil generasi](skills/lucky-kit/OUTPUT-LICENSE.md) untuk materi yang tercakup dalam hasil proyek, termasuk penggunaan privat dan komersial. Aplikasi hasil generasi gak wajib memakai branding Lucky Kit. Distribusi ulang skill atau pustaka template tetap mengikuti ketentuan yang berlaku. Lihat [kredit](CREDITS.md).
