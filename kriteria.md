## Sejauh ini, Anda telah mempelajari berbagai topik mengenai proses analisis data seperti berikut.

1. Dasar-Dasar Analisis Data
2. Penerapan Dasar-Dasar Descriptive Statistics
3. Petimbangan dalam Pengolahan Data
4. Data Wrangling
5. Exploratory Data Analysis
6. Data Visualization
7. Pengembangan Dashboard

## Kriteria 1: Menggunakan Salah Satu dari Dataset yang Telah Disediakan

1. Penggunaan dataset ada di folder @Air-quality-dataset

## Kriteria 2: Melakukan Seluruh Proses Analisis Data

Mirip seperti berbagai materi latihan yang telah dibahas sebelumnya, Anda harus melakukan seluruh proses analisis data mulai dari mendefinisikan pertanyaan hingga membuat rekomendasi action item dari hasil analisis.

Proyek analisis data yang Anda buat harus memenuhi ketentuan berikut.

1. Menentukan Pertanyaan Bisnis

- Minimal terdapat 2 buah pertanyaan bisnis (pertanyaan analisis) yang ingin dijawab melalui proses analisis data.
- Pertanyaan tersebut haruslah menerapkan metode SMART Question.

a. Spesific (Spesifik)
Pertanyaan Anda harus jelas, fokus pada sebuah topik tertentu, dan tidak bermakna ganda. Hindari pertanyaan yang terlalu luas.

- Salah: Bagaimana cara meningkatkan penjualan?
- Benar: Faktor apa saja yang memengaruhi penurunan penjualan produk kategori elektronik di wilayah Jakarta selama kuartal terakhir?

b. Measurable (Terukur)
Pertanyaan Anda harus bisa dijawab dengan angka atau matrix yang konkret. Anda harus tahu apa yang akan dihitung.

- Salah: Apakah pelanggan senang dengan layanan kita?
- Benar: Berapa skor rata-rata Customer Satisfaction untuk layanan purna jual bulan ini dibandingkan bulan lalu?

c. Action-Oriented (Berorientasi Aksi)
Hasil dari pertanyaan Anda harus bisa memberikan arahan untuk melakukan tindakan nyata. Jika pertanyaan terjawab, stakeholder harus tahu apa langkah selanjutnya.

- Salah: Mengapa orang suka berbelanja?
- Benar: Fitur apa pada aplikasi yang paling sering digunakan sebelum pengguna memutuskan untuk melakukan checkout?

c. Relevant (Relevan)
Hasil dari pertanyaan Anda harus sejalan dengan tujuan utama bisnis atau masalah yang sedang dihadapi.

- Salah: Menanyakan tentang stok gudang saat masalah utamanya adalah efektivitas kampanye media sosial.
- Benar: Apakah kampanye iklan di Instagram memberikan Return on Ad Spend (ROAS) yang lebih tinggi dibandingkan iklan di TikTok?

d. Time-bound (Terikat Waktu)
Pertanyaan Anda harus ada batasan waktu yang jelas agar analisis memiliki konteks yang tepat.

- Salah: Berapa banyak pengguna baru kita?
- Benar: Berapa tingkat pertumbuhan pengguna baru secara bulanan (Month-over-Month) sepanjang tahun 2025?

## Contoh pertanyaan bisnis yang memenuhi seluruh elemen SMART

"Faktor apa saja yang memengaruhi penurunan conversion rate pada pengguna aplikasi Android di wilayah Jabodetabek sebesar 5% selama periode Flash Sale Maret 2026?"

## Keterangan:

- Specific: Fokus pada "penurunan conversion rate" untuk "aplikasi Android" di "Jabodetabek". Bukan sekadar penjualan turun.
- Measurable: Ada angka konkret yang ingin dianalisis, yaitu penurunan sebesar "5%".
- Action-Oriented: Dengan mengetahui faktor penyebabnya misalnya bug pada versi Android tertentu atau kendala logistik di Jabodetabek, tim bisa langsung melakukan perbaikan teknis atau operasional.
- Relevant: Penurunan konversi saat Flash Sale adalah masalah kritis bagi bisnis retail/e-commerce.
- Time-bound: Dibatasi pada periode spesifik "Flash Sale Maret 2026".

2. Data Wrangling

- Gathering Data
  Pada tahap ini, Anda harus mengumpulkan dan memuat semua data yang dibutuhkan ke dalam format DataFrame.
- Assessing Data
  Pada tahap ini, Anda harus menilai kualitas dari data yang akan digunakan.
  a. Minimal Anda mampu mengidentifikasi 2 dari beberapa permasalahan yang dapat muncul dalam data, seperti:
  - Missing value
  - Invalid value
  - Duplicate data
  - Inaccurate value
  - Inconsistent value
  - Outlier, dan lain sebagainya.
    b. Anda dapat menggunakan berbagai method dan function dalam library Python untuk menemukan permasalahan tersebut.
    c. Setelah itu, Anda perlu menyebutkan solusi atau tindakan yang harus dilakukan di tahap selanjutnya, yakni

- cleaning data.
  Cleaning Data
  Pada tahap ini, Anda harus melakukan pembersihan data dari masalah yang Anda temukan di tahap Assessing Data.

3. Exploratory Data Analysis (EDA)

Anda harus melakukan eksplorasi data guna menjawab pertanyaan bisnis.

- Minimal terdapat 2 pertanyaan bisnis yang ingin diselesaikan melalui proses EDA.
- Anda dapat menggunakan berbagai method dan function dalam library Python untuk memahami data, seperti melihat rangkuman statistik, melakukan grouping dan agregasi untuk mendapatkan informasi tertentu, dan sebagainya.

Tahap selanjutnya ditujukan untuk melengkapi dan memperkuat proses eksplorasi Anda, yaitu melalui visualisasi data.

4. Visualization & Explanatory Analysis

- Minimal terdapat 2 buah visualisasi data untuk menjawab pertanyaan bisnis yang telah dibuat.
- Pastikan setiap pertanyaan bisnis terjawab oleh minimal 1 visualisasi.

5. Conclusion & Recommendation

- Minimal terdapat 2 buah kesimpulan dari hasil visualisasi data yang sekaligus menjawab pertanyaan bisnis yang telah dibuat.
- Pastikan ada kesimpulan untuk setiap pertanyaan bisnis.
- Buat minimal 1 rekomendasi akhir berupa action item dari kesimpulan yang telah didapatkan.

## Kriteria 3: Proses Analisis Dibuat dalam Notebook yang Rapi

Pada submission ini, Anda harus mengerjakan proyek analisis data menggunakan templat proyek yang telah disediakan. Tujuannya supaya proyek yang dibuat terdokumentasi dengan rapi. Templat yang dimaksud dapat diakses pada tautan berikut: templat notebook.

## Kriteria 4: Membuat Dashboard Sederhana Menggunakan Streamlit

Setelah melakukan proses analisis, selanjutnya Anda wajib membuat dashboard sebagai media untuk menyampaikan hasil analisis data secara interaktif. Pada proyek ini, Anda dapat membuat dashboard dengan streamlit mirip seperti materi latihan sebelumnya. Selain itu, pastikan bahwa dashboard Anda buat dapat berjalan dengan lancar di local.

## Submission Anda akan dinilai oleh Reviewer dengan penilaian bintang berskala 1-5. Untuk mendapatkan nilai tinggi, Anda bisa menerapkan beberapa saran berikut:

1. Memberikan dokumentasi menggunakan markdown/text cell pada notebook (.ipynb) untuk menjelaskan setiap tahapan analisis data.
2. Membuat visualisasi data yang baik dan efektif dengan menerapkan prinsip desain dan integritas.
3. Deploy dashboard ke dalam streamlit cloud.
4. Menerapkan teknik analisis lanjutan seperti RFM analysis, geospatial analysis, clustering, dll. (Tanpa menggunakan algoritma machine learning).
   Catatan: Pastikan teknik analisis lanjutan yang dilakukan relevan dengan dataset yang digunakan.

- RFM Analysis, bertujuan mengelompokkan pelanggan berdasarkan perilaku pembelian mereka dengan memperhatikan tiga faktor utama:
  a. Recency: Menghitung jumlah hari sejak terakhir kali pelanggan melakukan pembelian.
  b. Frequency: Menghitung jumlah total transaksi yang dilakukan oleh pelanggan dalam periode tertentu.
  c. Monetary: Menghitung total pengeluaran pelanggan dalam periode tersebut.
  d. Anda dapat melihat contoh implementasi kodenya pada submodul Latihan Membuat Visualisasi Data.

- Geospatial Analysis, bertujuan menganalisis data berdasarkan lokasi geografis untuk mengidentifikasi tren atau pola tertentu di suatu wilayah. Anda bisa menggunakan package seperti GeoPandas atau folium untuk membuat peta yang menampilkan distribusi data berdasarkan lokasi.

- Clustering, bertujuan mengelompokkan data ke dalam grup berdasarkan karakteristik tertentu tanpa menggunakan algoritma machine learning. Berikut adalah beberapa metode clustering yang bisa diterapkan:
  a. Manual Grouping: Menentukan kriteria pengelompokan berdasarkan aturan bisnis atau pemahaman domain, seperti mengelompokkan pelanggan berdasarkan rentang usia, pendapatan, atau jumlah transaksi.
  b. Binning: Menggunakan teknik binning untuk membagi data ke dalam interval atau kategori tertentu.
