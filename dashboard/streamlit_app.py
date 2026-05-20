"""
Air Quality Dashboard - Beijing PM2.5 Analysis
Streamlit Dashboard for Air Quality Data Analysis Project
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Beijing Air Quality Dashboard",
    page_icon="🌬️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #2C3E50;
        text-align: center;
        padding: 1rem 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #7F8C8D;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #ECF0F1;
        border-radius: 10px;
        padding: 1.5rem;
        text-align: center;
    }
    .stMetric {
        background-color: #ECF0F1;
        border-radius: 10px;
        padding: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load and prepare the cleaned air quality data"""
    try:
        df = pd.read_csv('main_data.csv')
        df['datetime'] = pd.to_datetime(df['datetime'])
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please run the Jupyter notebook first to generate the cleaned data.")
        return None

# Load data
df = load_data()

if df is not None:
    # Main header
    st.markdown('<p class="main-header">🌬️ Beijing Air Quality Dashboard</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Analisis Kualitas Udara Beijing 2013-2017</p>', unsafe_allow_html=True)

    # Sidebar filters
    st.sidebar.header("🔍 Filter Data")

    # Year filter
    years = sorted(df['year'].unique())
    selected_years = st.sidebar.multiselect(
        "Pilih Tahun",
        options=years,
        default=[2016]
    )

    # Station filter
    stations = sorted(df['station'].unique())
    selected_stations = st.sidebar.multiselect(
        "Pilih Stasiun",
        options=stations,
        default=['Aotizhongxin', 'Changping']
    )

    # Location type filter
    location_types = ['All', 'Urban', 'Suburban']
    selected_location = st.sidebar.selectbox(
        "Tipe Lokasi",
        options=location_types
    )

    # Apply filters
    filtered_df = df.copy()

    if selected_years:
        filtered_df = filtered_df[filtered_df['year'].isin(selected_years)]

    if selected_stations:
        filtered_df = filtered_df[filtered_df['station'].isin(selected_stations)]
    else:
        filtered_df = filtered_df[filtered_df['station'].isin(['Aotizhongxin', 'Changping'])]

    if selected_location != 'All':
        filtered_df = filtered_df[filtered_df['location_type'] == selected_location]

    # ========== OVERVIEW METRICS ==========
    st.markdown("---")
    st.subheader("📊 Overview Metrics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        avg_pm25 = filtered_df['PM2.5'].mean()
        st.metric("Rata-rata PM2.5", f"{avg_pm25:.2f} µg/m³")

    with col2:
        max_pm25 = filtered_df['PM2.5'].max()
        st.metric("PM2.5 Tertinggi", f"{max_pm25:.0f} µg/m³")

    with col3:
        avg_temp = filtered_df['TEMP'].mean()
        st.metric("Rata-rata Suhu", f"{avg_temp:.1f}°C")

    with col4:
        records = len(filtered_df)
        st.metric("Total Records", f"{records:,}")

    # ========== VISUALIZATION TABS ==========
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📈 Tren PM2.5",
        "🏙️ Urban vs Suburban",
        "🔗 Korelasi Meteorologi",
        "📊 AQI & Seasonal",
        "📋 Ringkasan per Stasiun"
    ])

    with tab1:
        st.subheader("Tren PM2.5 Sepanjang Waktu")

        # Time series chart
        fig, ax = plt.subplots(figsize=(12, 5))

        monthly_avg = filtered_df.groupby([filtered_df['datetime'].dt.to_period('M')])['PM2.5'].mean()
        monthly_avg.index = monthly_avg.index.to_timestamp()

        ax.plot(monthly_avg.index, monthly_avg.values, color='#E74C3C', linewidth=2)
        ax.fill_between(monthly_avg.index, monthly_avg.values, alpha=0.3, color='#E74C3C')
        ax.set_xlabel('Waktu', fontsize=11)
        ax.set_ylabel('PM2.5 (µg/m³)', fontsize=11)
        ax.set_title('Tren Rata-rata PM2.5 Bulanan', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)

        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(fig)

        # Daily pattern
        st.markdown("#### Pola Harian PM2.5")
        fig2, ax2 = plt.subplots(figsize=(10, 4))

        hourly_avg = filtered_df.groupby('hour')['PM2.5'].mean()
        bars = ax2.bar(hourly_avg.index, hourly_avg.values, color='#3498DB', edgecolor='navy')
        ax2.set_xlabel('Jam', fontsize=11)
        ax2.set_ylabel('PM2.5 (µg/m³)', fontsize=11)
        ax2.set_title('Rata-rata PM2.5 per Jam', fontsize=14, fontweight='bold')
        ax2.set_xticks(range(0, 24, 2))
        ax2.grid(True, alpha=0.3, axis='y')

        plt.tight_layout()
        st.pyplot(fig2)

    with tab2:
        st.subheader("Perbandingan Urban vs Suburban")

        col_left, col_right = st.columns(2)

        with col_left:
            # Bar chart comparison
            fig3, ax3 = plt.subplots(figsize=(6, 5))

            location_avg = filtered_df.groupby('location_type')['PM2.5'].mean()
            colors = ['#E74C3C', '#3498DB']
            bars = ax3.bar(location_avg.index, location_avg.values, color=colors, edgecolor='black')

            for bar, val in zip(bars, location_avg.values):
                ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                        f'{val:.1f}', ha='center', va='bottom', fontweight='bold')

            ax3.set_ylabel('Rata-rata PM2.5 (µg/m³)', fontsize=11)
            ax3.set_title('PM2.5: Urban vs Suburban', fontsize=13, fontweight='bold')
            ax3.set_ylim(0, location_avg.max() * 1.2)

            plt.tight_layout()
            st.pyplot(fig3)

        with col_right:
            # Box plot
            fig4, ax4 = plt.subplots(figsize=(6, 5))

            urban_data = filtered_df[filtered_df['location_type'] == 'Urban']['PM2.5']
            suburban_data = filtered_df[filtered_df['location_type'] == 'Suburban']['PM2.5']

            bp = ax4.boxplot([urban_data, suburban_data],
                           labels=['Urban', 'Suburban'],
                           patch_artist=True)
            bp['boxes'][0].set_facecolor('#E74C3C')
            bp['boxes'][1].set_facecolor('#3498DB')

            ax4.set_ylabel('PM2.5 (µg/m³)', fontsize=11)
            ax4.set_title('Distribusi PM2.5', fontsize=13, fontweight='bold')

            plt.tight_layout()
            st.pyplot(fig4)

        # Station breakdown
        st.markdown("#### Breakdown per Stasiun")
        station_avg = filtered_df.groupby(['station', 'location_type'])['PM2.5'].mean().reset_index()
        station_avg = station_avg.sort_values('PM2.5', ascending=False)

        fig5, ax5 = plt.subplots(figsize=(10, 5))
        colors = ['#E74C3C' if loc == 'Urban' else '#3498DB' for loc in station_avg['location_type']]
        bars = ax5.barh(station_avg['station'], station_avg['PM2.5'], color=colors, edgecolor='black')
        ax5.set_xlabel('Rata-rata PM2.5 (µg/m³)', fontsize=11)
        ax5.set_title('Rata-rata PM2.5 per Stasiun', fontsize=13, fontweight='bold')

        from matplotlib.patches import Patch
        legend_elements = [Patch(facecolor='#E74C3C', label='Urban'),
                         Patch(facecolor='#3498DB', label='Suburban')]
        ax5.legend(handles=legend_elements)

        plt.tight_layout()
        st.pyplot(fig5)

    with tab3:
        st.subheader("Korelasi Faktor Meteorologi")

        # Correlation matrix
        corr_cols = ['PM2.5', 'WSPM', 'RAIN', 'TEMP', 'PRES', 'DEWP']
        corr_matrix = filtered_df[corr_cols].corr()

        fig6, ax6 = plt.subplots(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='RdBu_r',
                   center=0, vmin=-1, vmax=1, square=True,
                   linewidths=0.5, ax=ax6)
        ax6.set_title('Correlation Matrix: PM2.5 & Meteorological Factors',
                     fontsize=13, fontweight='bold')

        plt.tight_layout()
        st.pyplot(fig6)

        # Wind speed categories
        st.markdown("#### PM2.5 Berdasarkan Kecepatan Angin")

        def categorize_wspm(wspm):
            if wspm < 2:
                return 'Calm (<2 m/s)'
            elif wspm < 4:
                return 'Light (2-4 m/s)'
            elif wspm < 6:
                return 'Moderate (4-6 m/s)'
            else:
                return 'Strong (>6 m/s)'

        filtered_df['wspm_category'] = filtered_df['WSPM'].apply(categorize_wspm)

        fig7, ax7 = plt.subplots(figsize=(9, 5))

        wspm_order = ['Calm (<2 m/s)', 'Light (2-4 m/s)', 'Moderate (4-6 m/s)', 'Strong (>6 m/s)']
        wspm_colors = ['#C0392B', '#E74C3C', '#F39C12', '#27AE60']

        wspm_analysis = filtered_df.groupby('wspm_category')['PM2.5'].mean()
        wspm_analysis = wspm_analysis.reindex(wspm_order)

        bars = ax7.bar(range(len(wspm_order)), wspm_analysis.values, color=wspm_colors, edgecolor='black')
        ax7.set_xticks(range(len(wspm_order)))
        ax7.set_xticklabels(wspm_order, rotation=15)
        ax7.set_ylabel('Rata-rata PM2.5 (µg/m³)', fontsize=11)
        ax7.set_title('PM2.5 Berdasarkan Kategori Kecepatan Angin', fontsize=13, fontweight='bold')
        ax7.grid(True, alpha=0.3, axis='y')

        for bar, val in zip(bars, wspm_analysis.values):
            ax7.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                    f'{val:.1f}', ha='center', va='bottom', fontsize=10)

        plt.tight_layout()
        st.pyplot(fig7)

    with tab5:
        st.subheader("Analisis Lanjutan: AQI & Seasonal")

        # AQI Category Distribution
        st.markdown("#### Kategori Kualitas Udara (AQI Binning)")

        # Create AQI categories
        def categorize_pm25_aqi(pm25):
            if pm25 <= 12:
                return 'Good (0-12)'
            elif pm25 <= 35.4:
                return 'Moderate'
            elif pm25 <= 55.4:
                return 'Unhealthy Sensitive'
            elif pm25 <= 150.4:
                return 'Unhealthy'
            elif pm25 <= 250.4:
                return 'Very Unhealthy'
            else:
                return 'Hazardous'

        filtered_df['aqi_category'] = filtered_df['PM2.5'].apply(categorize_pm25_aqi)

        fig_aqi, ax_aqi = plt.subplots(figsize=(10, 5))
        aqi_order = ['Good (0-12)', 'Moderate', 'Unhealthy Sensitive', 'Unhealthy', 'Very Unhealthy', 'Hazardous']
        aqi_colors = ['#27AE60', '#F1C40F', '#E67E22', '#E74C3C', '#8E44AD', '#2C3E50']

        aqi_counts = [filtered_df['aqi_category'].value_counts().get(cat, 0) for cat in aqi_order]
        bars = ax_aqi.bar(range(len(aqi_order)), aqi_counts, color=aqi_colors, edgecolor='black')
        ax_aqi.set_xticks(range(len(aqi_order)))
        ax_aqi.set_xticklabels(aqi_order, rotation=20, fontsize=9)
        ax_aqi.set_ylabel('Jumlah Record', fontsize=10)
        ax_aqi.set_title('Distribusi Kategori Kualitas Udara (AQI)', fontsize=13, fontweight='bold')
        ax_aqi.grid(True, alpha=0.3, axis='y')

        # Add percentage labels
        total = len(filtered_df)
        for bar, cnt in zip(bars, aqi_counts):
            pct = cnt / total * 100
            ax_aqi.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 50,
                       f'{pct:.1f}%', ha='center', va='bottom', fontsize=9)

        plt.tight_layout()
        st.pyplot(fig_aqi)

        # Seasonal Analysis
        st.markdown("#### Analisis Musiman")

        def get_season(month):
            if month in [12, 1, 2]:
                return 'Winter'
            elif month in [3, 4, 5]:
                return 'Spring'
            elif month in [6, 7, 8]:
                return 'Summer'
            else:
                return 'Autumn'

        filtered_df['season'] = filtered_df['month'].apply(get_season)

        col_seas1, col_seas2 = st.columns(2)

        with col_seas1:
            # Seasonal bar chart
            fig_seas, ax_seas = plt.subplots(figsize=(6, 4))
            seasonal_avg = filtered_df.groupby('season')['PM2.5'].mean()
            seasonal_avg = seasonal_avg.reindex(['Spring', 'Summer', 'Autumn', 'Winter'])
            season_colors = ['#2ECC71', '#F39C12', '#E67E22', '#3498DB']
            bars_seas = ax_seas.bar(seasonal_avg.index, seasonal_avg.values, color=season_colors, edgecolor='black')

            for bar, val in zip(bars_seas, seasonal_avg.values):
                ax_seas.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 2,
                           f'{val:.1f}', ha='center', fontsize=10)

            ax_seas.set_ylabel('Rata-rata PM2.5', fontsize=10)
            ax_seas.set_title('PM2.5 per Musim', fontsize=12, fontweight='bold')
            ax_seas.set_ylim(0, seasonal_avg.max() * 1.2)
            ax_seas.grid(True, alpha=0.3, axis='y')

            plt.tight_layout()
            st.pyplot(fig_seas)

        with col_seas2:
            # Seasonal summary table
            seasonal_summary = filtered_df.groupby('season')['PM2.5'].agg(['mean', 'median', 'std']).round(2)
            seasonal_summary = seasonal_summary.reindex(['Spring', 'Summer', 'Autumn', 'Winter'])
            seasonal_summary.columns = ['Mean', 'Median', 'Std']

            st.dataframe(seasonal_summary, use_container_width=True)

        # Temperature Binned Analysis
        st.markdown("#### PM2.5 Berdasarkan Kategori Suhu")

        def categorize_temp(temp):
            if pd.isna(temp):
                return 'Unknown'
            elif temp < 0:
                return 'Freezing'
            elif temp < 10:
                return 'Cold'
            elif temp < 20:
                return 'Cool'
            elif temp < 25:
                return 'Comfortable'
            elif temp < 30:
                return 'Warm'
            else:
                return 'Hot'

        filtered_df['temp_category'] = filtered_df['TEMP'].apply(categorize_temp)

        fig_temp, ax_temp = plt.subplots(figsize=(9, 5))
        temp_avg = filtered_df.groupby('temp_category')['PM2.5'].mean()
        temp_order = ['Freezing', 'Cold', 'Cool', 'Comfortable', 'Warm', 'Hot']
        temp_avg = temp_avg.reindex(temp_order)
        temp_colors = plt.cm.coolwarm(np.linspace(0, 1, len(temp_avg)))

        bars_temp = ax_temp.barh(range(len(temp_avg)), temp_avg.values, color=temp_colors, edgecolor='black')
        ax_temp.set_yticks(range(len(temp_avg)))
        ax_temp.set_yticklabels(temp_avg.index, fontsize=10)
        ax_temp.set_xlabel('Rata-rata PM2.5', fontsize=10)
        ax_temp.set_title('PM2.5 Berdasarkan Kategori Suhu (Binned)', fontsize=12, fontweight='bold')
        ax_temp.grid(True, alpha=0.3, axis='x')

        plt.tight_layout()
        st.pyplot(fig_temp)

    with tab4:
        st.subheader("Ringkasan Statistik per Stasiun")

        # Summary table
        station_summary = filtered_df.groupby('station').agg({
            'PM2.5': ['mean', 'median', 'std', 'max'],
            'PM10': 'mean',
            'TEMP': 'mean',
            'WSPM': 'mean',
            'RAIN': 'sum'
        }).round(2)

        station_summary.columns = ['PM2.5 Mean', 'PM2.5 Median', 'PM2.5 Std', 'PM2.5 Max',
                                   'PM10 Mean', 'Temp Mean', 'Wind Speed Mean', 'Total Rain']

        st.dataframe(station_summary, use_container_width=True)

        # Download button
        csv = station_summary.to_csv()
        st.download_button(
            label="📥 Download Summary (CSV)",
            data=csv,
            file_name="station_summary.csv",
            mime="text/csv"
        )

    # ========== CONCLUSIONS SECTION ==========
    st.markdown("---")
    st.subheader("📌 Kesimpulan & Findings")

    conclusion_col1, conclusion_col2 = st.columns(2)

    with conclusion_col1:
        st.markdown("""
        ### Finding #1: Urban vs Suburban
        - Stations di area **Urban** memiliki rata-rata PM2.5 lebih tinggi
        - Perbedaan signifikan antara stasiun perkotaan dan suburban
        - **Insight**: Perlu kebijakan pengendalian berbeda untuk area urban
        """)

    with conclusion_col2:
        st.markdown("""
        ### Finding #2: Meteorological Factors
        - **Kecepatan angin** berkorelasi negatif dengan PM2.5
        - Kondisi **angin tenang** meningkatkan konsentrasi PM2.5
        - **Insight**: Prediksi PM2.5 bisa memanfaatkan data meteorological
        """)

    # Advanced Analysis Conclusions
    st.markdown("""
    ---
    ### Advanced Analysis Findings
    """)

    adv_col1, adv_col2, adv_col3 = st.columns(3)

    with adv_col1:
        # AQI summary
        aqi_counts = filtered_df['aqi_category'].value_counts()
        total = len(filtered_df)
        unhealthy_pct = ((aqi_counts.get('Unhealthy', 0) + aqi_counts.get('Very Unhealthy', 0) +
                        aqi_counts.get('Hazardous', 0)) / total * 100)
        st.metric("Unhealthy+ Days", f"{unhealthy_pct:.1f}%")

    with adv_col2:
        # Seasonal insight
        if 'season' in filtered_df.columns:
            winter_avg = filtered_df[filtered_df['season'] == 'Winter']['PM2.5'].mean()
            summer_avg = filtered_df[filtered_df['season'] == 'Summer']['PM2.5'].mean()
            seasonal_diff = winter_avg - summer_avg
            st.metric("Winter vs Summer Diff", f"{seasonal_diff:.1f} µg/m³")

    with adv_col3:
        # Good days
        good_pct = aqi_counts.get('Good (0-12)', 0) / total * 100
        st.metric("Good Air Days", f"{good_pct:.1f}%")

    st.markdown("""
    **Key Insights dari Advanced Analysis:**

    1. **AQI Distribution**: majority of days falls in "Moderate" to "Unhealthy" categories
    2. **Seasonal Pattern**: Winter memiliki PM2.5 tertinggi, Summer terendah
    3. **Binning Analysis**: Temperature dan wind speed categories memberikan insight tambahan
    """)
    st.markdown("---")
    st.markdown(
        """
        <div style="text-align: center; color: #7F8C8D; padding: 1rem;">
            <p>📊 Beijing Air Quality Dashboard | Proyek Analisis Data Dicoding</p>
            <p style="font-size: 0.8rem;">Data Source: PRSA (Beijing PM2.5 Data) | Period: 2013-2017</p>
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.warning("⚠️ Mohon jalankan Jupyter notebook terlebih dahulu untuk menghasilkan file data yang diperlukan.")