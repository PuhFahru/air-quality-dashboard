Berikut merupakan beberapa poin yang perlu diperhatikan ketika mengirimkan submission.

Berkas submission yang dikirim merupakan folder proyek analisis data dalam format ZIP. Pastikan di dalamnyna terdapat berkas-berkas berikut.
Dataset yang digunakan dalam proses analisis data.
Berkas Jupyter Notebook atau Colab Notebook (.ipynb). Pastikan berkas notebook tersebut sudah dijalankan.
Berkas Python (.py) yang digunakan untuk membuat dashboard dengan streamlit.
Berkas requirements.txt yang berisi berbagai library yang digunakan dalam proses analisis data. 
Berkas Markdown (README.md) yang berisi cara menjalankan dashboard (contoh: dicoding collection dashboard).
Jika Anda menerapkan saran pertama, pastikan Anda memberikan rangkuman berupa insight yang diperoleh dari setiap tahapan analisis yang telah dilakukan, mulai dari Gathering Data hingga Explanatory Analysis.
Jika Anda menerapkan saran kedua, pastikan seluruh visualisasi yang dibuat telah menerapkan prinsip desain dan integritas.
Jika Anda menerapkan saran ketiga, tuliskan tautan untuk dashboard tersebut dalam berkas url.txt.
Jika Anda menerapkan saran keempat, pastikan untuk menulis penjelasan atau tujuan dari teknik analisis yang dilakukan dalam markdown/text cell pada berkas Jupyter Notebook atau Colab Notebook.
Berikut merupakan struktur direktori submission yang kami sarankan.
submission
├───dashboard
| ├───main_data.csv
| └───dashboard.py
├───data
| ├───data_1.csv
| └───data_2.csv
├───notebook.ipynb
├───README.md
└───requirements.txt
└───url.txt