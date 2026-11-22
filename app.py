import streamlit as st

# Konfigurasi halaman utama
st.set_page_config(
    page_title="Database Portal",
    page_icon="🗄️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Navigasi menu di sidebar kiri
with st.sidebar:
    st.title("🗄️ DB Portal")
    st.caption("Portal Utama Sistem Database")
    st.divider()

    menu = st.radio(
        "Menu Navigasi",
        [
            "🏠 Halaman Utama",
            "📂 Katalog Database",
            "🔍 Pencarian & Query",
            "📝 Input & Pembaruan",
            "📘 Panduan & Struktur",
        ],
    )

    st.divider()
    st.caption("Tautan tiap menu menyusul")

# Konten halaman utama (landing / beranda)
if menu == "🏠 Halaman Utama":
    st.title("Pusat Informasi & Manajemen Database")
    st.markdown(
        "Selamat datang di halaman utama web database. "
        "Silakan pilih menu di sidebar kiri atau kartu layanan di bawah ini."
    )

    st.write("")
    st.subheader("Daftar Menu Utama")

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.markdown("### 📂 Katalog Database")
            st.write("Akses daftar koleksi database utama dan kategori arsip.")
            st.button("Buka Menu →", key="menu_katalog", disabled=True)

    with col2:
        with st.container(border=True):
            st.markdown("### 🔍 Pencarian & Query")
            st.write("Telusuri data tertentu menggunakan kata kunci atau filter.")
            st.button("Buka Menu →", key="menu_query", disabled=True)

    with col3:
        with st.container(border=True):
            st.markdown("### 📝 Input & Pembaruan")
            st.write("Tambah entri baru atau perbarui catatan database.")
            st.button("Buka Menu →", key="menu_input", disabled=True)

    st.write("")

    col4, col5, _ = st.columns(3)

    with col4:
        with st.container(border=True):
            st.markdown("### 📘 Panduan & Struktur")
            st.write("Dokumentasi skema tabel, aturan data, dan alur kerja.")
            st.button("Buka Menu →", key="menu_panduan", disabled=True)

    with col5:
        with st.container(border=True):
            st.markdown("### 🔗 Integrasi & Tautan")
            st.write("Akses cepat ke sumber data atau layanan eksternal.")
            st.button("Buka Menu →", key="menu_integrasi", disabled=True)

# Tampilan sementara untuk menu lain di sidebar
else:
    st.title(menu)
    st.info("Halaman ini masih dalam tahap kerangka. Link dan isinya akan ditambahkan menyusul.")