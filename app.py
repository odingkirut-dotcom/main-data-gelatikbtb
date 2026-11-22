import base64
from pathlib import Path
import streamlit as st

LINK_PENCARIAN_QUERY = "https://dashboard-gelatik-a6gbsfmcxgwueejswhve6a.streamlit.app/"
GELATIK_IMG_PATH = Path("gelatik.png")
BTB_IMG_PATH = Path("BTB.jpg")

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="GELATIK × BTB // DB Portal",
    page_icon=str(GELATIK_IMG_PATH) if GELATIK_IMG_PATH.exists() else "DB",
    layout="wide",
    initial_sidebar_state="expanded",
)


def get_base64_image(path: Path) -> str | None:
    if not path.exists():
        return None
    return base64.b64encode(path.read_bytes()).decode("utf-8")


gelatik_b64 = get_base64_image(GELATIK_IMG_PATH)
btb_b64 = get_base64_image(BTB_IMG_PATH)


def make_logo_chip(b64: str | None, mime: str, alt: str, height_px: int, pad: str) -> str:
    if not b64:
        return ""
    return (
        f'<span style="background:rgba(248,250,252,0.96);padding:{pad};border-radius:8px;'
        f'border:1px solid rgba(251,191,36,0.45);display:inline-flex;align-items:center;'
        f'flex-shrink:0;">'
        f'<img src="data:image/{mime};base64,{b64}" alt="{alt}" '
        f'style="height:{height_px}px;width:auto;object-fit:contain;display:block;" /></span>'
    )


gelatik_sidebar_chip = make_logo_chip(gelatik_b64, "png", "Logo Gelatik", 22, "4px 8px")
btb_sidebar_chip = make_logo_chip(btb_b64, "jpeg", "Logo BTB", 22, "4px 8px")

gelatik_badge_chip = make_logo_chip(gelatik_b64, "png", "Logo Gelatik", 18, "3px 7px")
btb_badge_chip = make_logo_chip(btb_b64, "jpeg", "Logo BTB", 18, "3px 7px")

# 2. CSS Kustom: Gabungan Gelatik & BTB (Amber/Hex)
st.markdown(
    """
    <style>
        .stApp {
            background-color: #0E1216;
            background-image:
                radial-gradient(circle at 85% 15%, rgba(251, 191, 36, 0.10), transparent 35%),
                radial-gradient(circle at 15% 85%, rgba(148, 163, 184, 0.10), transparent 40%),
                radial-gradient(rgba(251, 191, 36, 0.06) 1px, transparent 1px),
                radial-gradient(rgba(148, 163, 184, 0.05) 1px, #0E1216 1px);
            background-size: 100% 100%, 100% 100%, 28px 28px, 28px 28px;
            background-position: 0 0, 0 0, 0 0, 14px 14px;
        }

        .hero-gelatik-btb {
            background: linear-gradient(135deg, rgba(24, 32, 40, 0.94), rgba(15, 20, 26, 0.96));
            border: 1px solid rgba(251, 191, 36, 0.35);
            border-left: 5px solid #FBBF24;
            border-radius: 16px;
            padding: 28px 32px;
            box-shadow: 0 10px 28px rgba(0, 0, 0, 0.35);
            margin-bottom: 20px;
        }

        .fusion-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #FBBF24;
            background: rgba(251, 191, 36, 0.12);
            border: 1px solid rgba(251, 191, 36, 0.40);
            padding: 5px 12px;
            border-radius: 999px;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: 2.05rem;
            font-weight: 700;
            color: #F8FAFC;
            margin: 0 0 10px 0;
            letter-spacing: -0.4px;
        }

        .hero-desc {
            font-size: 1rem;
            color: #CBD5E1;
            margin: 0;
            max-width: 780px;
            line-height: 1.65;
        }

        .section-label {
            font-size: 0.85rem;
            text-transform: uppercase;
            letter-spacing: 1.3px;
            color: #FBBF24;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .hive-btn {
            display: inline-block;
            text-decoration: none !important;
            background: linear-gradient(135deg, #FBBF24, #F59E0B);
            color: #0E1216 !important;
            border: 1px solid #FDE68A;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: 700;
            transition: transform 0.15s ease, box-shadow 0.2s ease;
            margin-top: 6px;
        }

        .hive-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 0 16px rgba(251, 191, 36, 0.35);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def new_tab_button(label: str, url: str) -> str:
    return (
        f'<a class="hive-btn" href="{url}" target="_blank" rel="noopener noreferrer">'
        f"{label}</a>"
    )


# 3. Sidebar Navigasi
with st.sidebar:
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:6px;">'
        f'{gelatik_sidebar_chip}'
        f'<span style="color:#FBBF24;font-weight:700;">×</span>'
        f'{btb_sidebar_chip}</div>'
        f'<div style="font-size:1.15rem;font-weight:700;color:#F8FAFC;letter-spacing:0.3px;">'
        f'GELATIK × BTB</div>',
        unsafe_allow_html=True,
    )
    st.caption("Portal Utama Sistem Database")
    st.divider()

    menu = st.radio(
        "NAVIGASI MODUL",
        [
            "Beranda Utama",
            "Katalog Database",
            "Pencarian & Query",
            "Input & Pembaruan",
            "Arsitektur & Panduan",
            "Tautan & Integrasi",
        ],
    )

    st.divider()
    st.caption("AKSES CEPAT")
    st.markdown(
        new_tab_button("Buka Dashboard Query ↗", LINK_PENCARIAN_QUERY),
        unsafe_allow_html=True,
    )

# 4. Halaman Utama (Tanpa Data Dummy)
if menu == "Beranda Utama":
    st.markdown(
        f"""
        <div class="hero-gelatik-btb">
            <div class="fusion-badge">
                {gelatik_badge_chip}
                <span>×</span>
                {btb_badge_chip}
                <span>GELATIK × BTB • Database Hub</span>
            </div>
            <div class="hero-title">Pusat Navigasi & Gerbang Database</div>
            <p class="hero-desc">
                Halaman utama terpadu untuk mengakses berbagai modul database, katalog koleksi,
                pencarian terstruktur, dan formulir pembaruan. Pilih menu pada bilah samping
                atau kartu modul di bawah ini.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-label">Daftar Modul Utama</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.caption("MODUL 01")
            st.markdown("#### Katalog Database")
            st.write("Akses indeks koleksi database, kategori arsip, dan daftar repositori data.")
            st.button("Akses Segera Hadir", key="m1", disabled=True)

    with col2:
        with st.container(border=True):
            st.caption("MODUL 02 • TERHUBUNG")
            st.markdown("#### Pencarian & Query")
            st.write("Penelusuran data terarah menggunakan filter kategori, parameter, dan kata kunci.")
            st.markdown(
                new_tab_button("Buka Pencarian & Query ↗", LINK_PENCARIAN_QUERY),
                unsafe_allow_html=True,
            )

    with col3:
        with st.container(border=True):
            st.caption("MODUL 03")
            st.markdown("#### Input & Pembaruan")
            st.write("Portal terpusat untuk menambahkan entri baru dan memperbarui data tersimpan.")
            st.button("Akses Segera Hadir", key="m3", disabled=True)

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            st.caption("MODUL 04")
            st.markdown("#### Arsitektur & Panduan")
            st.write("Referensi struktur tabel, standar format data, dan pedoman penggunaan.")
            st.button("Akses Segera Hadir", key="m4", disabled=True)

    with col5:
        with st.container(border=True):
            st.caption("MODUL 05")
            st.markdown("#### Tautan & Integrasi")
            st.write("Jalur penghubung ke sumber data eksternal, sheet, atau layanan pendukung.")
            st.button("Akses Segera Hadir", key="m5", disabled=True)

    with col6:
        with st.container(border=True):
            st.caption("MODUL 06")
            st.markdown("#### Protokol & Akses")
            st.write("Pengaturan hak akses, aturan keamanan, dan catatan pembaruan sistem.")
            st.button("Akses Segera Hadir", key="m6", disabled=True)

# 5. Halaman Pencarian & Query
elif menu == "Pencarian & Query":
    st.markdown('<div class="section-label">MODUL 02 • PENCARIAN & QUERY</div>', unsafe_allow_html=True)
    st.title("Pencarian & Query")
    st.write("Dashboard dibuka di tab baru sementara halaman utama GELATIK × BTB tetap terbuka.")
    st.markdown(
        new_tab_button("Buka Dashboard Pencarian & Query ↗", LINK_PENCARIAN_QUERY),
        unsafe_allow_html=True,
    )

# 6. Halaman Placeholder untuk Menu Lain
else:
    st.markdown(f'<div class="section-label">{menu}</div>', unsafe_allow_html=True)
    st.title(menu)
    st.info("Kerangka halaman sudah siap. Tautan dan fitur modul ini akan ditambahkan menyusul.")
