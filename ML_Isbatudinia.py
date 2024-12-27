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

# Visualisasi Distribusi Harga Mobil
st.subheader('Distribusi Harga Mobil')
plt.figure(figsize=(10, 6))
sns.histplot(data['AskPrice'], bins=30, kde=True)
plt.xlabel('Harga (Price)')
plt.ylabel('Frekuensi')
st.pyplot(plt)

# Distribusi Harga Berdasarkan Merek
st.subheader('Distribusi Harga Berdasarkan Merek')
if 'Brand' in data.columns:
    top_brands = data['Brand'].value_counts().head(10).index
    filtered_df = data[data['Brand'].isin(top_brands)]
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Brand', y='AskPrice', data=filtered_df, order=top_brands)
    plt.xticks(rotation=45)
    plt.xlabel('Merek Mobil')
    plt.ylabel('Harga (Price)')
    st.pyplot(plt)

    # Distribusi Harga Berdasarkan Jarak Tempuh
    st.subheader('Distribusi Harga Berdasarkan Jarak Tempuh')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='kmDriven', y='AskPrice', data=data)
    plt.xlabel('Jarak Tempuh (KmDriven)')
    plt.ylabel('Harga (Price)')
    st.pyplot(plt)

    # Distribusi Harga Berdasarkan Umur Mobil
    st.subheader('Distribusi Harga Berdasarkan Umur Mobil')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Age', y='AskPrice', data=data)
    plt.xlabel('Umur Mobil (Tahun)')
    plt.ylabel('Harga (Price)')
    st.pyplot(plt)

    # Distribusi Harga Berdasarkan Tahun Produksi
    st.subheader('Distribusi Harga Berdasarkan Tahun Produksi')
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='Year', y='AskPrice', data=data)
    plt.xlabel('Tahun Produksi')
    plt.ylabel('Harga (Price)')
    st.pyplot(plt)

# Filter Data
st.subheader('Filter Data')
st.write("Gunakan filter ini untuk menyaring data berdasarkan rentang harga.")
min_price, max_price = st.slider('Rentang Harga', int(data['AskPrice'].min()), int(data['AskPrice'].max()), (int(data['AskPrice'].min()), int(data['AskPrice'].max())))
filtered_data = data[(data['AskPrice'] >= min_price) & (data['AskPrice'] <= max_price)]
st.write(filtered_data)

# Kesimpulan
st.header('Kesimpulan dan Rekomendasi')
st.header("**Kesimpulan Analisis:**")
st.write("Distribusi Harga Mobil:")
st.write("1. Harga mobil bekas memiliki distribusi yang cenderung condong ke kiri, menunjukkan bahwa sebagian besar mobil berada di kisaran harga yang lebih rendah.")
st.write("2. Ini menandakan pasar mobil bekas lebih didominasi oleh kendaraan dengan harga terjangkau.")
st.write("Harga Berdasarkan Merek:")
st.write("1. Merek mobil memiliki pengaruh signifikan terhadap harga.")
st.write("2. Beberapa merek populer dengan volume penjualan tinggi cenderung memiliki harga yang lebih stabil, sedangkan merek premium menunjukkan variasi harga yang lebih besar.")
st.write("3. Merek tertentu seperti Honda dan Toyota mendominasi pasar dengan rentang harga yang bervariasi.")
st.write("Harga Berdasarkan Jarak Tempuh (KmDriven):")
st.write("1. Terdapat korelasi negatif antara jarak tempuh dan harga mobil.")
st.write("2. Mobil dengan jarak tempuh lebih tinggi cenderung memiliki harga yang lebih rendah, mencerminkan pengaruh pemakaian terhadap nilai jual kembali kendaraan.")
st.write("Harga Berdasarkan Umur Mobil:")
st.write("1. Mobil yang lebih tua cenderung memiliki harga yang lebih rendah.")
st.write("2. Penurunan harga cukup signifikan setelah 5–10 tahun, menunjukkan bahwa umur mobil menjadi faktor penentu dalam penilaian harga.")
st.write("Harga Berdasarkan Tahun Produksi:")
st.write("1. Mobil dengan tahun produksi yang lebih baru memiliki harga yang lebih tinggi.")
st.write("2. Ini menunjukkan bahwa teknologi dan fitur terbaru yang tersedia pada model baru meningkatkan nilai jual mobil.")
st.header("**Rekomendasi:**")
st.write("1. Pembeli yang mencari mobil dengan harga terjangkau bisa mempertimbangkan mobil dengan jarak tempuh dan umur lebih tinggi.")
st.write("2. Penjual dapat menargetkan pasar premium untuk mobil baru dengan jarak tempuh rendah dan merek terkenal guna mendapatkan harga yang lebih baik.")
st.write("3. Merek mobil populer seperti Honda dan Toyota tetap menjadi pilihan utama bagi pembeli dengan preferensi harga yang stabil.")