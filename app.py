import base64
from pathlib import Path
import streamlit as st

LINK_PENCARIAN_QUERY = "https://dashboard-gelatik-a6gbsfmcxgwueejswhve6a.streamlit.app/"
GELATIK_IMG_PATH = Path("gelatik.png")
BTB_IMG_PATH = Path("BTB.jpg")

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="GELATIK × BTB // Outsourcing DB Portal",
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
        f'border:1px solid rgba(245,158,11,0.45);display:inline-flex;align-items:center;'
        f'flex-shrink:0;">'
        f'<img src="data:image/{mime};base64,{b64}" alt="{alt}" '
        f'style="height:{height_px}px;width:auto;object-fit:contain;display:block;" /></span>'
    )


gelatik_sidebar_chip = make_logo_chip(gelatik_b64, "png", "Logo Gelatik", 22, "4px 8px")
btb_sidebar_chip = make_logo_chip(btb_b64, "jpeg", "Logo BTB", 22, "4px 8px")

gelatik_badge_chip = make_logo_chip(gelatik_b64, "png", "Logo Gelatik", 18, "3px 7px")
btb_badge_chip = make_logo_chip(btb_b64, "jpeg", "Logo BTB", 18, "3px 7px")

# 2. CSS Kustom: Korporat Agency Outsourcing (Navy Slate + Amber + Grid Halus)
st.markdown(
    """
    <style>
        .stApp {
            background-color: #0B111A;
            background-image:
                linear-gradient(to right, rgba(148, 163, 184, 0.04) 1px, transparent 1px),
                linear-gradient(to bottom, rgba(148, 163, 184, 0.04) 1px, transparent 1px),
                radial-gradient(circle at 88% 12%, rgba(245, 158, 11, 0.09), transparent 36%),
                radial-gradient(circle at 12% 88%, rgba(56, 189, 248, 0.06), transparent 40%);
            background-size: 32px 32px, 32px 32px, 100% 100%, 100% 100%;
        }

        .hero-outsourcing {
            background: linear-gradient(135deg, rgba(19, 28, 42, 0.95), rgba(12, 18, 28, 0.97));
            border: 1px solid rgba(148, 163, 184, 0.22);
            border-left: 5px solid #F59E0B;
            border-radius: 14px;
            padding: 28px 32px;
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.35);
            margin-bottom: 22px;
        }

        .corp-badge {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 11.5px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #FBBF24;
            background: rgba(245, 158, 11, 0.12);
            border: 1px solid rgba(245, 158, 11, 0.38);
            padding: 5px 12px;
            border-radius: 999px;
            margin-bottom: 12px;
        }

        .hero-title {
            font-size: 2rem;
            font-weight: 700;
            color: #F8FAFC;
            margin: 0 0 10px 0;
            letter-spacing: -0.3px;
        }

        .hero-desc {
            font-size: 0.98rem;
            color: #CBD5E1;
            margin: 0;
            max-width: 800px;
            line-height: 1.65;
        }

        .section-label {
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 1.3px;
            color: #FBBF24;
            font-weight: 700;
            margin-bottom: 12px;
        }

        .corp-btn {
            display: inline-block;
            text-decoration: none !important;
            background: linear-gradient(135deg, #F59E0B, #D97706);
            color: #0B111A !important;
            border: 1px solid #FCD34D;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.9rem;
            font-weight: 700;
            transition: transform 0.15s ease, box-shadow 0.2s ease;
            margin-top: 6px;
        }

        .corp-btn:hover {
            transform: translateY(-1px);
            box-shadow: 0 0 16px rgba(245, 158, 11, 0.32);
        }
    </style>
    """,
    unsafe_allow_html=True,
)


def new_tab_button(label: str, url: str) -> str:
    return (
        f'<a class="corp-btn" href="{url}" target="_blank" rel="noopener noreferrer">'
        f"{label}</a>"
    )


# 3. Sidebar Navigasi
with st.sidebar:
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:6px;">'
        f'{gelatik_sidebar_chip}'
        f'<span style="color:#F59E0B;font-weight:700;">×</span>'
        f'{btb_sidebar_chip}</div>'
        f'<div style="font-size:1.15rem;font-weight:700;color:#F8FAFC;letter-spacing:0.3px;">'
        f'GELATIK × BTB</div>',
        unsafe_allow_html=True,
    )
    st.caption("Outsourcing Workforce & Database Portal")
    st.divider()

    menu = st.radio(
        "MENU OPERASIONAL",
        [
            "Beranda Utama",
            "Katalog & Direktori",
            "Pencarian & Query",
            "Input & Pembaruan Data",
            "SOP & Struktur Data",
            "Integrasi & Tautan",
        ],
    )

    st.divider()
    st.caption("PORTAL CEPAT")
    st.markdown(
        new_tab_button("Buka Dashboard Query ↗", LINK_PENCARIAN_QUERY),
        unsafe_allow_html=True,
    )

# 4. Halaman Utama (Tanpa Data Dummy)
if menu == "Beranda Utama":
    st.markdown(
        f"""
        <div class="hero-outsourcing">
            <div class="corp-badge">
                {gelatik_badge_chip}
                <span>×</span>
                {btb_badge_chip}
                <span>GELATIK × BTB • Workforce &amp; Outsourcing Hub</span>
            </div>
            <div class="hero-title">Portal Terpadu Data &amp; Operasional Outsourcing</div>
            <p class="hero-desc">
                Gerbang utama pengelolaan basis data operasional, direktori penempatan, pencarian
                terstruktur, serta administrasi data tenaga kerja dan klien. Pilih modul pada
                navigasi samping atau kartu layanan di bawah ini.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="section-label">Layanan &amp; Modul Utama</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container(border=True):
            st.caption("MODUL 01 • DIREKTORI")
            st.markdown("#### Katalog &amp; Direktori")
            st.write("Akses indeks basis data penempatan, daftar unit kerja, dan arsip dokumen operasional.")
            st.button("Segera Tersedia", key="m1", disabled=True)

    with col2:
        with st.container(border=True):
            st.caption("MODUL 02 • TERHUBUNG")
            st.markdown("#### Pencarian &amp; Query")
            st.write("Telusuri data operasional dan penempatan secara cepat melalui filter serta query.")
            st.markdown(
                new_tab_button("Buka Pencarian & Query ↗", LINK_PENCARIAN_QUERY),
                unsafe_allow_html=True,
            )

    with col3:
        with st.container(border=True):
            st.caption("MODUL 03 • ADMINISTRASI")
            st.markdown("#### Input &amp; Pembaruan Data")
            st.write("Portal pencatatan data baru, pembaruan status, dan penyesuaian catatan administrasi.")
            st.button("Segera Tersedia", key="m3", disabled=True)

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        with st.container(border=True):
            st.caption("MODUL 04 • TATA KELOLA")
            st.markdown("#### SOP &amp; Struktur Data")
            st.write("Acuan standar format data, alur kerja operasional, dan pedoman pengelolaan.")
            st.button("Segera Tersedia", key="m4", disabled=True)

    with col5:
        with st.container(border=True):
            st.caption("MODUL 05 • KONEKTIVITAS")
            st.markdown("#### Integrasi &amp; Tautan")
            st.write("Tautan penghubung ke lembar kerja, sistem pelaporan, dan layanan pendukung.")
            st.button("Segera Tersedia", key="m5", disabled=True)

    with col6:
        with st.container(border=True):
            st.caption("MODUL 06 • KEPATUHAN")
            st.markdown("#### Akses &amp; Kebijakan")
            st.write("Pengaturan otorisasi akses, kerahasiaan data, dan catatan pembaruan sistem.")
            st.button("Segera Tersedia", key="m6", disabled=True)

# 5. Halaman Pencarian & Query
elif menu == "Pencarian & Query":
    st.markdown('<div class="section-label">MODUL 02 • PENCARIAN &amp; QUERY</div>', unsafe_allow_html=True)
    st.title("Pencarian & Query")
    st.write("Dashboard dibuka di tab baru sementara portal utama GELATIK × BTB tetap terbuka.")
    st.markdown(
        new_tab_button("Buka Dashboard Pencarian & Query ↗", LINK_PENCARIAN_QUERY),
        unsafe_allow_html=True,
    )

# 6. Halaman Placeholder untuk Menu Lain
else:
    st.markdown(f'<div class="section-label">{menu}</div>', unsafe_allow_html=True)
    st.title(menu)
    st.info("Kerangka modul sudah siap. Tautan dan fitur halaman ini akan ditambahkan menyusul.")
