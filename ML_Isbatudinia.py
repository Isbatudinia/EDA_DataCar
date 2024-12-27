import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

def load_data():
    data = pd.read_csv('used_car_dataset.csv')
    # Bersihkan kolom harga
    data['AskPrice'] = data['AskPrice'].replace('[^0-9]', '', regex=True).astype(float)
    # Bersihkan kolom km_driven
    data['kmDriven'] = data['kmDriven'].replace('[^0-9]', '', regex=True).astype(float)
    return data

data = load_data()

# Hitung Umur Kendaraan
current_year = 2024
data['Age'] = current_year - data['Year']

# Title
st.title('Analisis Harga Mobil Bekas')

# Data Wrangling
st.header('1. Data Wrangling')
st.write("**Penjelasan**: Bagian ini memuat dan menampilkan data awal yang akan digunakan untuk analisis.")
st.subheader('Assign Dataset')
st.write('Dataset berhasil dimuat!')
st.write(data.head())

# Data Availability Checking
st.subheader('2. Data Availability Checking')
st.write("**Penjelasan**: Mengecek apakah data memiliki nilai kosong atau tipe data yang tidak sesuai.")
st.write('Informasi Dataset:')
st.write(data.info())
st.write('Jumlah Data Kosong:')
st.write(data.isnull().sum())

# Descriptive Statistics (Optional)
st.subheader('3. Descriptive Statistics')
st.write("**Penjelasan**: Memberikan gambaran statistik deskriptif untuk memahami distribusi dan karakteristik data.")
st.write(data.describe())

# Exploratory Data Analysis
st.header('4. Exploratory Data Analysis')
st.write("**Penjelasan**: Menjelajahi hubungan antar variabel untuk menemukan pola dan korelasi penting.")

# Korelasi Antar Fitur
st.subheader('Korelasi Antar Fitur')
st.write("Menampilkan matriks korelasi untuk melihat hubungan antara variabel numerik.")
# Pilih hanya kolom numerik
numeric_data = data[['AskPrice', 'Year', 'Age', 'kmDriven']]
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt='.2f', ax=ax)
st.pyplot(fig)

# Scatter Plot Harga vs Tahun
st.subheader('Harga vs Tahun Produksi')
st.write("Hubungan antara harga mobil dengan tahun produksinya.")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='Year', y='AskPrice', ax=ax)
st.pyplot(fig)

# Scatter Plot Harga vs Umur
st.subheader('Harga vs Umur Kendaraan')
st.write("Hubungan antara harga mobil dengan umur kendaraan.")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='Age', y='AskPrice', ax=ax)
st.pyplot(fig)

# Scatter Plot Harga vs Kilometer Tempuh
st.subheader('Harga vs Kilometer Tempuh')
st.write("Hubungan antara harga mobil dengan kilometer yang telah ditempuh.")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x='kmDriven', y='AskPrice', ax=ax)
st.pyplot(fig)

# Data Visualization
st.header('5. Data Visualization')
st.write("**Penjelasan**: Memvisualisasikan distribusi harga untuk memahami pola umum di data.")

# Visualisasi Distribusi Harga
st.subheader('Distribusi Harga Mobil')
fig, ax = plt.subplots()
sns.histplot(data['AskPrice'], kde=True, ax=ax)
st.pyplot(fig)

# Filter Data
st.subheader('Filter Data')
st.write("Gunakan filter ini untuk menyaring data berdasarkan rentang harga.")
min_price, max_price = st.slider('Rentang Harga', int(data['AskPrice'].min()), int(data['AskPrice'].max()), (int(data['AskPrice'].min()), int(data['AskPrice'].max())))
filtered_data = data[(data['AskPrice'] >= min_price) & (data['AskPrice'] <= max_price)]
st.write(filtered_data)

# Dashboard 
st.header('6. Dashboard')
st.write('Gunakan filter di atas untuk menjelajahi data lebih dalam.')

# Kesimpulan
st.header('7. Kesimpulan')
st.write("**Kesimpulan Analisis:**")
st.write("1. Harga mobil bekas memiliki korelasi negatif dengan umur kendaraan. Semakin tua kendaraan, harganya cenderung lebih murah.")
st.write("2. Kilometer yang telah ditempuh (km_driven) juga mempengaruhi harga, di mana kendaraan dengan jarak tempuh lebih tinggi cenderung memiliki harga lebih rendah.")
st.write("3. Tahun produksi memiliki korelasi positif dengan harga. Mobil yang lebih baru cenderung memiliki harga yang lebih tinggi.")
st.write("4. Distribusi harga menunjukkan adanya variasi besar, sehingga pemilihan harga yang tepat dapat dibantu dengan filter yang disediakan di dashboard.")
st.write("Gunakan dashboard dan visualisasi ini untuk mengeksplorasi lebih lanjut pola harga mobil bekas berdasarkan berbagai variabel.")
