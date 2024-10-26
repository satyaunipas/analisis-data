import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("main_data.csv")
df['datetime'] = pd.to_datetime(df[['year', 'month', 'day', 'hour']])

# Judul Dashboard
st.title("Dashboard Kualitas Udara")

# Pilihan Stasiun untuk Tren PM2.5
st.subheader("Tren Konsentrasi PM2.5 di Berbagai Stasiun")
station = st.selectbox("Pilih Stasiun:", df['station'].unique())
station_data = df[df['station'] == station]

# Plot Tren PM2.5
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=station_data, x='datetime', y='PM2.5', ax=ax)
ax.set_title(f'Tren PM2.5 di Stasiun {station}')
ax.set_xlabel("Tanggal")
ax.set_ylabel("Konsentrasi PM2.5")
st.pyplot(fig)

# Plot Distribusi Polutan
st.subheader("Distribusi Polutan Utama")
pollutant = st.selectbox("Pilih Polutan:", ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3'])

fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(df[pollutant], kde=True, ax=ax)
ax.set_title(f'Distribusi {pollutant}')
ax.set_xlabel(pollutant)
ax.set_ylabel("Frekuensi")
st.pyplot(fig)

# Scatter Plot antara Suhu dan PM2.5
st.subheader("Hubungan antara Suhu dan PM2.5")
fig, ax = plt.subplots(figsize=(8, 5))
sns.scatterplot(data=df, x='TEMP', y='PM2.5', alpha=0.5, ax=ax)
sns.regplot(data=df, x='TEMP', y='PM2.5', scatter=False, color='red', line_kws={"linewidth": 1.5}, ax=ax)
ax.set_title("Hubungan antara Suhu (TEMP) dan PM2.5")
ax.set_xlabel("Suhu (°C)")
ax.set_ylabel("Konsentrasi PM2.5")
st.pyplot(fig)