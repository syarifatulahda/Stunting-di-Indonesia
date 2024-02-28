import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import altair as alt

st.set_page_config(
    page_title = 'Stunting di Indonesia'
    ,layout='wide'
)

# Membaca file CSV ke dalam sebuah DataFrame
file1 ='Data.csv'
df1 = pd.read_csv(file1)
#st.write(df1)
#df1.info()

# helper function

def format_big_number(num):
    if num >= 1e6:
        return f"{num / 1e6:.2f} Mio"
    elif num >= 1e3:
        return f"{num / 1e3:.2f} K"
    else:
        return f"{num:.2f}"
    
#Fungsi untuk menambahkan gaya CSS ke teks
def style_text(text, color="green", font_size="24px", font_weight="bold"):
    return f'<span style="color:{color}; font-size:{font_size}; font-weight:{font_weight}">{text}</span>'

# Mengatur warna latar belakang sidebar
st.markdown(
    """
    <style>
    .sidebar .sidebar-content {
        background-color: #f4f4f4;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Tampilkan judul di sidebar
st.sidebar.title('Stunting')

# Membuat menu navigasi
page = st.sidebar.radio("Pilih Halaman", ["Stunting di Indonesia", "Faktor yang Diduga Mempengaruhi Stunting", "Bagaimana Hubungan Stunting dengan Faktor yang Diduga?"])

# Tampilkan konten berdasarkan pilihan navigasi

if page == "Stunting di Indonesia":
    st.title("Stunting Indonesia 2022")
    st.write("Stunting adalah kondisi gagal tumbuh pada anak di bawah lima tahun sebagai akibat dari kekurangan gizi kronis. "
             "Hal tersebut mengakibatkan anak terlalu pendek untuk usianya. Kekurangan gizi pada anak yang mengalami stunting terjadi sejak bayi dalam kandungan hingga setelah lahir atau biasa disebut 1.000 Hari Pertama Kehidupan (HPK). "
             "Anak yang mengalami stunting hingga berusia lima tahun akan sulit untuk diperbaiki sehingga berlanjut hingga dewasa dan dapat meningkatkan risiko keturunan dengan BBLR)."
    )
    st.write("Penurunan prevalensi stunting pada balita telah menjadi fokus utama, baik di tingkat global maupun di Indonesia. Dalam Rencana Pembangunan Jangka Menengah Nasional (RPJMN) 2020-2024, penurunan angka stunting pada anak usia dini telah ditetapkan sebagai salah satu proyek utama dengan target mencapai 14,00 persen pada tahun 2024. Untuk mencapai tujuan ini, kerja keras dari pemerintah dan berbagai pihak terlibat sangat diperlukan.")
    st.write("Dapat dilihat dibawah ini bahwa prevelensi stunting di Indonesia pada tahun 2022 sudah mengalami penurunan dibandingkan dengan tahun 2021")
    # Menampilkan 2 kolom
    col1, col2 = st.columns(2)
    # Menghitung rata-rata stunting untuk tahun 2021 dan 2022
    ts2021 = df1['Stunting 2021'].mean()
    ts2022 = df1['Stunting 2022'].mean()
    ts2122 = ts2022-ts2021
    n21=df1.iloc[0]['Stunting 2021']
    # Menampilkan rata-rata stunting untuk tahun 2021 di kolom pertama
    with col1:
        st.metric("2021", value=format_big_number(ts2021)+"%")
    # Menampilkan rata-rata stunting untuk tahun 2022 di kolom kedua
    with col2:
        st.metric("2022", value=f"{format_big_number(ts2022)}%", delta=f"{format_big_number(ts2122)}%")

    st.write("Bagaimana Stunting Tahun 2022 di Provinsi anda jika dibandingkan dengan Tahun 2021?")
    # Membaca file CSV ke dalam sebuah DataFrame
    file1 ='Data.csv'
    df1 = pd.read_csv(file1)

    Provinsi = st.selectbox("Provinsi", ['Pilih Provinsi', 'Nusa Tenggara Timur', 'Sulawesi Barat', 'Papua','Nusa Tenggara Barat','Aceh', 'Papua Barat','Sulawesi Tengah','Kalimantan Barat','Sulawesi Tenggara','Sulawesi Selatan','Kalimantan Tengah','Maluku Utara','Maluku','Sumatera Barat','Kalimantan Selatan','Kalimantan Timur','Gorontalo', 'Kalimantan Utara','Sumatera Utara', 'Jawa Tengah', 'Sulawesi Utara','Jawa Barat','Banten','Bengkulu','Jawa Timur','Sumatera Selatan', 'Kepulauan Bangka Belitung', 'Jambi', 'Riau', 'DI Yogyakarta', 'Kepulauan Riau','Lampung', 'DKI Jakarta', 'Bali'], index=0 if 'Tahun' not in st.session_state else None)
    
    if Provinsi == 'Nusa Tenggara Timur':
        n21=df1.iloc[0]['Stunting 2021']
        n22=df1.iloc[0]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass

        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Nusa Tenggara Timur lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2.5% dari tahun 2021 yaitu sebesar 35.3%."
        )
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Sulawesi Barat' :
        n21=df1.iloc[1]['Stunting 2021']
        n22=df1.iloc[1]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2021 untuk Provinsi Sulawesi Barat lebih besar dibandingkan dengan tahun 2022. "
            "Pada tahun 2022, angka stunting naik 1.2% dari tahun 2021 yaitu sebesar 35%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid green; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Papua' :
        n21=df1.iloc[2]['Stunting 2021']
        n22=df1.iloc[2]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2021 untuk Provinsi Papua lebih kecil dibandingkan dengan tahun 2022. "
            "Pada tahun 2022, angka stunting naik 5.10% dari tahun 2021 yaitu sebesar 34.6%." )
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid green; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Nusa Tenggara Barat' :
        n21=df1.iloc[3]['Stunting 2021']
        n22=df1.iloc[3]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2021 untuk Provinsi Nusa Tenggara Barat lebih kecil dibandingkan dengan tahun 2022. "
            "Pada tahun 2022, angka stunting naik 1.3% dari tahun 2021 yaitu sebesar 32.7%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid green; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Aceh' :
        n21=df1.iloc[4]['Stunting 2021']
        n22=df1.iloc[4]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Aceh lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2% dari tahun 2021 yaitu sebesar 31.2%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Papua Barat' :
        n21=df1.iloc[5]['Stunting 2021']
        n22=df1.iloc[5]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
       # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Papua Barat lebih besar dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting naik 3.8% dari tahun 2021 yaitu sebesar 30%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid green; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Sulawesi Tengah' :
        n21=df1.iloc[6]['Stunting 2021']
        n22=df1.iloc[6]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Sulawesi Tengah lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 1.5% dari tahun 2021 yaitu sebesar 28.2%." )
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Kalimantan Barat' :
        n21=df1.iloc[7]['Stunting 2021']
        n22=df1.iloc[7]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Kalimantan Barat lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2% dari tahun 2021 yaitu sebesar 27.8%."  )
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Sulawesi Tenggara' :
        n21=df1.iloc[8]['Stunting 2021']
        n22=df1.iloc[8]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Sulawesi Tenggara lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2.5% dari tahun 2021 yaitu sebesar 27.7%."        )
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Sulawesi Selatan' :
        n21=df1.iloc[9]['Stunting 2021']
        n22=df1.iloc[9]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Sulawesi Selatan lebih kecil dibandingkan dengan tahun 2021. "     
            "Pada tahun 2022, angka stunting turun 0.2% dari tahun 2021 yaitu sebesar 27.2%." )
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
        
    elif Provinsi == 'Kalimantan Tengah' :
        n21=df1.iloc[10]['Stunting 2021']
        n22=df1.iloc[10]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Kalimantan Tengah lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 0.5% dari tahun 2021 yaitu sebesar 26.9%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Maluku Utara' :
        n21=df1.iloc[11]['Stunting 2021']
        n22=df1.iloc[11]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
             st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Maluku Utara lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 1.4% dari tahun 2021 yaitu sebesar 26.1%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Maluku' :
        n21=df1.iloc[12]['Stunting 2021']
        n22=df1.iloc[12]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Maluku lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2.6% dari tahun 2021 yaitu sebesar 26.1%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Sumatera Barat' :
        n21=df1.iloc[13]['Stunting 2021']
        n22=df1.iloc[13]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Sumatera Barat lebih besar dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting naik 1.9% dari tahun 2021 yaitu sebesar 25.2%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Kalimantan Selatan' :
        n21=df1.iloc[14]['Stunting 2021']
        n22=df1.iloc[14]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Kalimantan Selatan lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 5.4% dari tahun 2021 yaitu sebesar 24.6%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Kalimantan Timur' :
        n21=df1.iloc[15]['Stunting 2021']
        n22=df1.iloc[15]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Kalimantan Timur lebih besar dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting naik 1.1% dari tahun 2021 yaitu sebesar 23.9%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Gorontalo' :
        n21=df1.iloc[16]['Stunting 2021']
        n22=df1.iloc[16]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Gorontalo lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 5.2% dari tahun 2021 yaitu sebesar 23.8%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
   
    elif Provinsi == 'Kalimantan Utara' :
        n21=df1.iloc[17]['Stunting 2021']
        n22=df1.iloc[17]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Kalimantan Utara lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 5.4% dari tahun 2021 yaitu sebesar 22,1%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Sumatera Utara' :
        n21=df1.iloc[18]['Stunting 2021']
        n22=df1.iloc[18]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Sumatera Utara lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 4.7% dari tahun 2021 yaitu sebesar 21.1%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Jawa Tengah' :
        n21=df1.iloc[19]['Stunting 2021']
        n22=df1.iloc[19]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Jawa Tengah lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 0.1% dari tahun 2021 yaitu sebesar 20.8%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Sulawesi Utara' :
        n21=df1.iloc[20]['Stunting 2021']
        n22=df1.iloc[20]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Sulawesi Utara lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 1.1% dari tahun 2021 yaitu sebesar 20.5%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
    
    elif Provinsi == 'Jawa Barat' :
        n21=df1.iloc[21]['Stunting 2021']
        n22=df1.iloc[21]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Jawa Barat lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 4.3% dari tahun 2021 yaitu sebesar 20.2%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
   
    elif Provinsi == 'Banten' :
        n21=df1.iloc[22]['Stunting 2021']
        n22=df1.iloc[22]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Banten lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 20.0% dari tahun 2021 yaitu sebesar 20%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Bengkulu' :
        n21=df1.iloc[23]['Stunting 2021']
        n22=df1.iloc[23]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:  
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Bengkulu lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2.3% dari tahun 2021 yaitu sebesar 19.8%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Jawa Timur' :
        n21=df1.iloc[24]['Stunting 2021']
        n22=df1.iloc[24]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Jawa Timur lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 4.3% dari tahun 2021 yaitu sebesar 19.2%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Sumatera Selatan' :
        n21=df1.iloc[25]['Stunting 2021']
        n22=df1.iloc[25]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Sumatera Selatan lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 6.2% dari tahun 2021 yaitu sebesar 18.6%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Kepulauan Bangka Belitung' :
        n21=df1.iloc[26]['Stunting 2021']
        n22=df1.iloc[26]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Kepulauan Bangka Belitung lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 0.1% dari tahun 2021 yaitu sebesar 18.5%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Jambi' :
        n21=df1.iloc[27]['Stunting 2021']
        n22=df1.iloc[27]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Jambi lebih kecil dibandingkan dengan tahun 2021."
            "Pada tahun 2022, angka stunting turun 4.4% dari tahun 2021 yaitu sebesar 18%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Riau' :
        n21=df1.iloc[28]['Stunting 2021']
        n22=df1.iloc[28]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Riau lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 5.30% dari tahun 2021 yaitu sebesar 17.0%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'DI Yogyakarta' :
        n21=df1.iloc[29]['Stunting 2021']
        n22=df1.iloc[29]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021: 
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi DI Yogyakarta lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 0.9% dari tahun 2021 yaitu sebesar 16.4%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Kepulauan Riau' :
        n21=df1.iloc[30]['Stunting 2021']
        n22=df1.iloc[30]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Kepulauan Riau lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2.2% dari tahun 2021 yaitu sebesar 15.4%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Lampung' :
        n21=df1.iloc[31]['Stunting 2021']
        n22=df1.iloc[31]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Lampung lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 3.3% dari tahun 2021 yaitu sebesar 15.2%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'DKI Jakarta' :
        n21=df1.iloc[32]['Stunting 2021']
        n22=df1.iloc[32]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi DKI Jakarta lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2% dari tahun 2021 yaitu sebesar 14.8%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)

    elif Provinsi == 'Bali' :
        n21=df1.iloc[33]['Stunting 2021']
        n22=df1.iloc[33]['Stunting 2022']
        n2122= n22 - n21
        if n22 > ts2022:
            st.markdown('<h2 style="color: red; animation: fadeIn 3s;">Peringatan!</h2>', unsafe_allow_html=True)
            st.write("Provinsi ini berada di atas rata-rata stunting Indonesia 2022")
        else:
            pass
        s2021 , s2022 = st.columns(2)
        with s2021:  
            st.metric("2021", value=f'{n21}%')
        with s2022:
            st.metric("2022", value=f'{n22}%', delta=format_big_number(n2122) + "%")
        # Menampilkan informasi tambahan dalam kotak dengan warna yang berbeda menggunakan HTML
        additional_info = (
            "Angka Stunting pada tahun 2022 untuk Provinsi Bali lebih kecil dibandingkan dengan tahun 2021. "
            "Pada tahun 2022, angka stunting turun 2.9% dari tahun 2021 yaitu sebesar 8%.")
        st.write("Informasi Tambahan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info}</div>', unsafe_allow_html=True)
        # Membuat teks untuk mengenai sumber data
    sumber = """
    Sumber Data: [Stunting 2021-2022](https://ayosehat.kemkes.go.id/pub/files/files46531._MATERI_KABKPK_SOS_SSGI.pdf)        """
    st.markdown(sumber)

elif page == "Faktor yang Diduga Mempengaruhi Stunting":
    st.title("Faktor-faktor yang Mempengaruhi Stunting")
    st.write("Faktor Penyebab stunting juga dipengaruhi oleh pekerjaan ibu, usia ibu ketika hamil, jumlah anggota rumah tangga, pola asuh, dan pemberian ASI eksklusif, selain itu stunting juga disebabkan oleh beberapa faktor lain seperti pendidikan ibu, pengetahuan ibu mengenai gizi, pemberian ASI eksklusif, pemberian imunisasi dasar yang lengkap, tingkat kecukupan zink dan zat besi, riwayat penyakit infeksi serta faktor genetik. Serta faktor luarnya seperti sanitasi yang layak dan air minum yang layak.")
    st.write("Dibawah ini terdapat tiga faktor yang diduga mempengaruhi stunting di Indonesia.")
    st.write("Anda dapat melihat ketiga faktor tersebut berdasarkan provinsi.")
    # Menambahkan pilihan untuk memilih provinsi
    province_options = ['Pilih Provinsi'] + list(df1['Provinsi'].unique())
    selected_province = st.selectbox('Pilih Provinsi:', province_options)
    # Filter data untuk provinsi yang dipilih
    selected_data = df1[df1['Provinsi'] == selected_province]
    # Plot bar chart horizontal jika provinsi A dipilih
    if selected_province != 'Pilih Provinsi':
        selected_data = df1[df1['Provinsi'] == selected_province]
    
        if selected_province == 'Nusa Tenggara Timur':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title=Persentase),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sulawesi Barat':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Papua':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Nusa Tenggara Barat':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Aceh':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Papua Barat':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sulawesi Tengah':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Kalimantan Barat':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sulawesi Tenggara':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sulawesi Selatan':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Kalimantan Tengah':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Maluku Utara':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Maluku':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sumatera Barat':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Kalimantan Selatan':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Kalimantan Timur':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Gorontalo':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Kalimantan Utara':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sumatera Utara':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Jawa Tengah':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sulawesi Utara':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Jawa Barat':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Banten':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Bengkulu':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Jawa Timur':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Sumatera Selatan':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Kep. Bangka Belitung':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Jambi':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Riau':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'DI Yogyakarta':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Kepulauan Riau':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Lampung':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'DKI Jakarta':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
        elif selected_province == 'Bali':
            selected_data = selected_data.drop(columns=['Provinsi','Stunting 2022','Stunting 2021'])  # Menghapus kolom Provinsi
            selected_data = selected_data.T.reset_index()  # Transpose dan reset index
            selected_data.columns = ['Variable', 'Value']  # Mengganti nama kolom

            # Membuat bar chart horizontal dengan Altair
            bars = alt.Chart(selected_data).mark_bar().encode(
                y=alt.Y('Variable:N', title='Variable'),  # Variabel di sumbu y
                x=alt.X('Value:Q', title='Persentase'),  # Nilai di sumbu x
                color='Variable:N'  # Warna berdasarkan variabel
            ).properties(
                width=600,
                height=400,
                title=f'Data Provinsi {selected_province}'
            )
            st.altair_chart(bars, use_container_width=True)
    else:
        ()
    sumber = """
    Sumber Data: [Sanitasi Layak](https://www.bps.go.id/id/statistics-table/2/MTI2NyMy/proporsi-rumah-tangga-yang-memiliki-akses-terhadap-layanan-sanitasi-layak.html) 
                [Imunisasi Dasar Lengkap dan Ibu Melahirkan < 20 Tahun](https://www.bps.go.id/id/publication/2022/12/23/54f24c0520b257b3def481be/profil-kesehatan-ibu-dan-anak-2022.html)     
        """
    st.markdown(sumber)
    
elif page == "Bagaimana Hubungan Stunting dengan Faktor yang Diduga?":
    
    st.title("Bagaimana Hubungan Stunting dengan Faktor yang Diduga?")
    Faktor = st.selectbox("Pilih Faktor :", ['Pilih Faktor', 'Sanitasi Layak', 'Imunisasi Dasar Lengkap', 'Ibu Melahirkan Usia < 20 Tahun'], index=0 if 'Faktor' not in st.session_state else None)
    if Faktor == 'Sanitasi Layak':
        # Ambil satu kolom sebagai variabel x dan satu kolom sebagai variabel y
        y = df1['Stunting 2022']
        x = df1['Sanitasi Layak']  # Ubah kolom sesuai kebutuhan Anda
        # Menghitung regresi linear
        coefficients = np.polyfit(x, y, 1)
        m, b = coefficients
        # Menghitung korelasi antara variabel x dan y
        correlation = np.corrcoef(x, y)[0, 1]
        # Persamaan garis regresi linear
        equation = f'y = {m:.2f}x + {b:.2f}'
        # Membuat dataframe untuk plotting
        df_plot = pd.DataFrame({'x': x, 'y': y})
        # Plot scatter plot dan garis regresi linear menggunakan Altair
        scatter_plot = alt.Chart(df_plot).mark_circle().encode(
            x='x:Q',
            y='y:Q',
            tooltip=['x:Q', 'y:Q']
        )
        regression_line = alt.Chart(df_plot).transform_regression(
            'x', 'y'
        ).mark_line(color='red').encode(
            x='x',
            y='y'
        )
        plot = (scatter_plot + regression_line).properties(
            width= 800,
            height= 400,
            title='Scatter Plot antara Stunting dan Sanitasi Layak dengan Garis Regresi Linear'
        ).interactive()
        # Menampilkan plot menggunakan st.write()
        st.write(plot)
        st.write(f'Nilai Korelasi: {correlation:.2f}')
        st.write(f'Persamaan Regresi: {equation}')
        additional_info = (
            "1. Korelasi antara stunting dengan sanitasi layak adalah -0.58. Ini menunjukkan bahwa hubungan antara stunting dan sanitasi layak cukup kuat. "
            "Meskipun tidak sempurna, korelasi ini cukup signifikan untuk menarik kesimpulan bahwa perubahan dalam satu variabel cenderung diikuti oleh perubahan dalam variabel lainnya.<br>"
            "2. -0.38 adalah koefisien kemiringan garis regresi, yang menunjukkan seberapa banyak stunting (y) berubah untuk setiap satuan perubahan dalam sanitasi layak (x).<br>"
            "3. 54.40 adalah intercept, yang merupakan perkiraan tingkat stunting ketika tingkat sanitasi layak adalah nol.<br>"
        )
        additional_info = '<div style="text-align: justify; text-justify: inter-word; border: 1px solid red; padding: 10px">' + additional_info + '</div>'
        st.write("Informasi Tambahan:")
        st.markdown(additional_info, unsafe_allow_html=True)
        additional_info2 = (
            "Jika tingkat sanitasi layak meningkat (x meningkat), kita dapat memperkirakan penurunan tingkat stunting (y menurun), dan sebaliknya."
        )
        st.write("Kesimpulan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info2}</div>', unsafe_allow_html=True)


    elif Faktor == 'Imunisasi Dasar Lengkap':
        # Ambil satu kolom sebagai variabel x dan satu kolom sebagai variabel y
        y = df1['Stunting 2022']
        x = df1['Imunisasi Dasar Lengkap']  # Ubah kolom sesuai kebutuhan Anda
        # Menghitung regresi linear
        coefficients = np.polyfit(x, y, 1)
        m, b = coefficients
        # Menghitung korelasi antara variabel x dan y
        correlation = np.corrcoef(x, y)[0, 1]
        # Persamaan garis regresi linear
        equation = f'y = {m:.2f}x + {b:.2f}'
        # Membuat dataframe untuk plotting
        df_plot = pd.DataFrame({'x': x, 'y': y})
        # Plot scatter plot dan garis regresi linear menggunakan Altair
        scatter_plot = alt.Chart(df_plot).mark_circle().encode(
            x='x:Q',
            y='y:Q',
            tooltip=['x:Q', 'y:Q']
        )
        regression_line = alt.Chart(df_plot).transform_regression(
            'x', 'y'
        ).mark_line(color='red').encode(
            x='x',
            y='y'
        )
        plot = (scatter_plot + regression_line).properties(
            width= 800,
            height= 400,
            title='Scatter Plot antara Stunting dan Imunisasi Dasar Lengkap dengan Garis Regresi Linear'
        ).interactive()
        # Menampilkan plot menggunakan st.write()
        st.write(plot)
        st.write(f'Nilai Korelasi: {correlation:.2f}')
        st.write(f'Persamaan Regresi: {equation}')
        additional_info = (
            "1. Korelasi antara stunting dan imunisasi dasar lengkap adalah -0.42. Ini  menunjukkan bahwa ada hubungan negatif moderat antara tingkat stunting dan imunisasi dasar lengkap."
            "Dalam kata lain, semakin tinggi tingkat stunting, semakin rendah tingkat imunisasi dasar lengkap, dan sebaliknya.<br>"
            "2. -0.20 adalah koefisien kemiringan garis regresi. Ini menunjukkan bahwa setiap peningkatan satu unit dalam imunisasi dasar lengkap (x) akan diikuti oleh penurunan sebesar 0.20 unit dalam tingkat stunting (y)..<br>"
            "3. 35.88 adalah intercept, yang menunjukkan perkiraan tingkat stunting ketika tingkat imunisasi dasar lengkap adalah nol.<br>"
        )
        additional_info = '<div style="text-align: justify; text-justify: inter-word; border: 1px solid red; padding: 10px">' + additional_info + '</div>'
        st.write("Informasi Tambahan:")
        st.markdown(additional_info, unsafe_allow_html=True)
        additional_info2 = (
            "jika tingkat imunisasi dasar lengkap meningkat (x meningkat), kita dapat memperkirakan penurunan tingkat stunting (y menurun), dan sebaliknya."
        )
        st.write("Kesimpulan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info2}</div>', unsafe_allow_html=True)


    elif Faktor == 'Ibu Melahirkan Usia < 20 Tahun':
        # Ambil satu kolom sebagai variabel x dan satu kolom sebagai variabel y
        y = df1['Stunting 2022']
        x = df1['Ibu Melahirkan <20tahun']  # Ubah kolom sesuai kebutuhan Anda
        # Menghitung regresi linear
        coefficients = np.polyfit(x, y, 1)
        m, b = coefficients
        # Menghitung korelasi antara variabel x dan y
        correlation = np.corrcoef(x, y)[0, 1]
        # Persamaan garis regresi linear
        equation = f'y = {m:.2f}x + {b:.2f}'
        # Membuat dataframe untuk plotting
        df_plot = pd.DataFrame({'x': x, 'y': y})
        # Plot scatter plot dan garis regresi linear menggunakan Altair
        scatter_plot = alt.Chart(df_plot).mark_circle().encode(
            x='x:Q',
            y='y:Q',
            tooltip=['x:Q', 'y:Q']
        )
        regression_line = alt.Chart(df_plot).transform_regression(
            'x', 'y'
        ).mark_line(color='red').encode(
            x='x',
            y='y'
        )
        plot = (scatter_plot + regression_line).properties(
            width= 800,
            height= 400,
            title='Scatter Plot antara Stunting dan Sanitasi Layak dengan Garis Regresi Linear'
        ).interactive()
        # Menampilkan plot menggunakan st.write()
        st.write(plot)
        st.write(f'Nilai Korelasi: {correlation:.2f}')
        st.write(f'Persamaan Regresi: {equation}')
        additional_info = (
            "1. Korelasi positif menunjukkan bahwa ketika satu variabel (misalnya, ibu melahirkan di bawah usia 20 tahun) meningkat, variabel lainnya (stunting) cenderung meningkat juga, dan sebaliknya.<br>"
            "2. Korelasi sebesar 0.33 menunjukkan bahwa hubungan antara tingkat stunting dan ibu melahirkan di bawah usia 20 tahun cukup lemah. Meskipun ada hubungan, tetapi tidak kuat.<br>"
            "3. 0.25 adalah koefisien kemiringan garis regresi. Ini menunjukkan bahwa setiap peningkatan satu unit dalam ibu melahirkan di bawah usia 20 tahun (x) akan diikuti oleh peningkatan sebesar 0.25 unit dalam tingkat stunting (y).<br>"
            "4. 11.84 adalah intercept, yang menunjukkan perkiraan tingkat stunting ketika ibu tidak melahirkan di bawah usia 20 tahun (x) adalah nol.<br>"
        )
        additional_info = '<div style="text-align: justify; text-justify: inter-word; border: 1px solid red; padding: 10px">' + additional_info + '</div>'
        st.write("Informasi Tambahan:")
        st.write(unsafe_allow_html=True)
        st.markdown(additional_info, unsafe_allow_html=True)
        additional_info2 = (
            "Jika jumlah ibu yang melahirkan di bawah usia 20 tahun meningkat (x meningkat), kita dapat memperkirakan peningkatan tingkat stunting (y meningkat), dan sebaliknya."
        )
        st.write("Kesimpulan:")
        st.markdown(f'<div style="border: 1px solid red; padding: 10px">{additional_info2}</div>', unsafe_allow_html=True)

st.sidebar.markdown("---")
st.sidebar.markdown("**Ditulis oleh:**")
st.sidebar.markdown("Syarifatul Ahda")
st.sidebar.markdown("email : syarifatulahdajy@gmail.com")