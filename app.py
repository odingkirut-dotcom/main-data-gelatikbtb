import streamlit as st

LINK_PENCARIAN_QUERY = "https://dashboard-gelatik-a6gbsfmcxgwueejswhve6a.streamlit.app/"

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="NEXUS DB // Portal",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# 2. CSS Kustom Nuansa Futuristik + Tombol Link New Tab
st.markdown(
    """
    <style>
        .stApp {
            background: radial-gradient(circle at top right, rgba(0, 229, 255, 0.08), transparent 35%),
                        radial-gradient(circle at bottom left, rgba(59, 130, 246, 0.08), transparent 40%),
                        #070B14;
        }

        .hero-box {
            background: linear-gradient(135deg, rgba(15, 23, 42, 0.92), rgba(10, 17, 32, 0.92));
            border: 1px solid rgba(0, 229, 255, 0.28);
            border-radius: 16px;
            padding: 28px 32px;
            box-shadow: 0 0 28px rgba(0, 229, 255, 0.07);
            margin-bottom: 20px;
        }

        .sys-badge {
            display: inline-block;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            color: #00E5FF;
            background: rgba(0, 229, 255, 0.10);
            border: 1px solid rgba(0, 229, 255, 0.35);
            padding: 4px 12px;
            border-radius: 999px;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: 2.1rem;
            font-weight: 700;
            color: #F8FAFC;
            margin: 0 0 10px 0;
            letter-spacing: -0.5px;
        }

        .hero-desc {
            font-size: 1rem;
            color: #94A3B8;
            margin: 0;
            max-width: 780px;
            line-height: 1.6;
        }

        .section-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1.4px;
            color: #00E5FF;
            font-weight: 600;
            margin-bottom: 12px;
        }

        .cyber-btn {
            display: inline-block;
            text-decoration: none !important;
            background: rgba(0, 229, 255, 0.12);
            color: #00E5FF !important;
            border: 1px solid rgba(0, 229, 255, 0.45);
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: 600;
            transition: all 0.2s ease;
            margin-top: 6px;
        }

        .cyber-btn:hover {
            background: rgba(0, 229, 255, 0.22);
            border-color: #00E5FF;
            box-shadow: 0 0 14px rgba(0, 229, 255, 0.25);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def new_tab_button(label: str, url: str) -> str:
    return (
        f'<a class="cyber-btn" href="{url}" target="_blank" rel="noopener noreferrer">'
        f"{label}</a>"
    )


# 3. Sidebar Navigasi
with st.sidebar:
    st.markdown("### ⚡ NEXUS // DB CORE")
    st.caption("Database Gateway & Navigation")
    st.divider()

    menu = st.radio(
        "MODUL NAVIGASI",
        [
            "🏠 Beranda Sistem",
            "📂 Katalog Database",
            "🔍 Pencarian & Query",
            "📝 Input & Pembaruan",
            "📘 Arsitektur & Panduan",
            "🔗 Tautan & Integrasi",
        ],
    )

    st.divider()
    st.caption("MODE: ACTIVE GATEWAY")
    st.markdown(
        new_tab_button("Buka Dashboard Query ↗", LINK_PENCARIAN_QUERY),
        unsafe_allow_html=True,
    )

# 4. Halaman Utama (Tanpa Data Dummy)
if menu == "🏠 Beranda Sistem":
    st.markdown(
        """
        <div class="hero-box">
            <div class="sys-badge">● Database Interface Online</div>
            <div class="hero-title">Pusat Kontrol & Navigasi Database</div>
            <p class="hero-desc">
                Antarmuka utama untuk mengakses berbagai modul database, katalog penyimpanan,
                pencarian terstruktur, serta formulir pengelolaan data. Pilih modul pada panel
                navigasi atau kartu di bawah ini.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-label">// Daftar Modul Utama</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.caption("MODUL 01")
            st.markdown("#### 📂 Katalog Database")
            st.write("Akses indeks koleksi database, kategori arsip, dan daftar repositori data.")
            st.button("Akses Segera Hadir", key="m1", disabled=True)

    with col2:
        with st.container(border=True):
            st.caption("MODUL 02 • TERHUBUNG")
            st.markdown("#### 🔍 Pencarian & Query")
            st.write("Penelusuran data terarah menggunakan filter kategori, parameter, dan kata kunci.")
            st.markdown(
                new_tab_button("Buka Pencarian & Query ↗", LINK_PENCARIAN_QUERY),
                unsafe_allow_html=True,
            )

    with col3:
        with st.container(border=True):
            st.caption("MODUL 03")
            st.markdown("#### 📝 Input & Pembaruan")
            st.write("Portal terpusat untuk menambahkan entri baru dan memperbarui data tersimpan.")
            st.button("Akses Segera Hadir", key="m3", disabled=True)

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            st.caption("MODUL 04")
            st.markdown("#### 📘 Arsitektur & Panduan")
            st.write("Referensi struktur tabel, standar format data, dan pedoman penggunaan.")
            st.button("Akses Segera Hadir", key="m4", disabled=True)

    with col5:
        with st.container(border=True):
            st.caption("MODUL 05")
            st.markdown("#### 🔗 Tautan & Integrasi")
            st.write("Jalur penghubung ke sumber data eksternal, sheet, atau layanan pendukung.")
            st.button("Akses Segera Hadir", key="m5", disabled=True)

    with col6:
        with st.container(border=True):
            st.caption("MODUL 06")
            st.markdown("#### 🛡️ Protokol & Akses")
            st.write("Pengaturan hak akses, aturan keamanan, dan catatan pembaruan sistem.")
            st.button("Akses Segera Hadir", key="m6", disabled=True)

# 5. Halaman Pencarian & Query
elif menu == "🔍 Pencarian & Query":
    st.markdown('<div class="section-label">// MODUL 02 • PENCARIAN & QUERY</div>', unsafe_allow_html=True)
    st.title("🔍 Pencarian & Query")
    st.write("Modul pencarian dan query terhubung ke aplikasi dashboard eksternal di tab baru.")
    st.markdown(
        new_tab_button("Buka Dashboard Pencarian & Query ↗", LINK_PENCARIAN_QUERY),
        unsafe_allow_html=True,
    )

# 6. Halaman Placeholder untuk Menu Lain
else:
    st.markdown(f'<div class="section-label">// {menu}</div>', unsafe_allow_html=True)
    st.title(menu)
    st.info("Kerangka halaman sudah siap. Tautan dan fitur modul ini akan ditambahkan menyusul.")
