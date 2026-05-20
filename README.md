# Dicoding Collection Dashboard

Analisis Kualitas Udara Beijing 2013-2017 - Proyek Analisis Data Dicoding

## Setup Environment - Anaconda

```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal

```bash
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run Streamlit Dashboard

```bash
cd dashboard
streamlit run dashboard.py
```

## Struktur Direktori

```
submission/
├───dashboard/
│   ├───main_data.csv
│   └───dashboard.py
├───data/
│   ├───PRSA_Data_Aotizhongxin_20130301-20170228.csv
│   └───... (data files lainnya)
├───notebook.ipynb
├───README.md
└───requirements.txt
```

## Fitur Dashboard

- Overview metrics PM2.5 dan kondisi meteorologi
- Tren PM2.5 sepanjang waktu
- Perbandingan Urban vs Suburban
- Korelasi faktor meteorologi
- Analisis AQI dan seasonal
- Ringkasan statistik per stasiun

## Sumber Data

Dataset: PRSA (Beijing PM2.5 Data) - Periode 2013-2017