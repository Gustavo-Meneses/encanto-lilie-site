import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | Vitrine Criativa",
    page_icon="🌸",
    layout="wide",
)

# 2. CSS Estilo Vitrine Clean (Inspirado no layout solicitado)
st.markdown("""
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
        
        /* Reset e Fundo */
        .stApp { background-color: #FDFDFD; }
        [data-testid="stHeader"] { visibility: hidden; }
        .block-container { padding: 1rem 2rem !important; max-width: 1100px; }

        /* CABEÇALHO CLEAN */
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 15px 0;
            border-bottom: 1px solid #F1F1F1;
            margin-bottom: 25px;
        }
        .logo-text {
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            font-size: 1.5rem;
            color: #111827 !important;
        }
        .search-bar-sim {
            background: #F3F4F6;
            padding: 8px 15px;
            border-radius: 20px;
            width: 40%;
            color: #9CA3AF;
            font-size: 0.9rem;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        /* BANNER NOVIDADE */
        .hero-banner {
            background: linear-gradient(135deg, #8B5CF6 0%, #D946EF 100%);
            border-radius: 16px;
            padding: 40px;
            color: white !important;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 40px;
        }
        .hero-text h1 { color: white !important; font-size: 2rem !important; margin: 0; }
        .hero-text p { color: #F5F3FF !important; opacity: 0.9; margin-top: 10px; }

        /* CATEGORIAS (CHIPS) */
        .category-container {
            display: flex;
            gap: 10px;
            margin-bottom: 30px;
            flex-wrap: wrap;
        }
        .cat-chip {
            background: #F3E8FF;
            color: #7C3AED !important;
            padding: 6px 16px;
            border-radius: 100px;
            font-size: 0.85rem;
            font-weight: 600;
            border: 1px solid #DDD6FE;
        }

        /* CARD DE PRODUTO CLEAN */
        .product-box {
            background: white;
            border: 1px solid #E5E7EB;
            border-radius: 12px;
            padding: 0;
            text-align: left;
            transition: 0.2s;
            margin-bottom: 15px;
        }
        .product-box:hover { border-color: #8B5CF6; box-shadow: 0 4px 12px rgba(0,0,0,0.05); }
        .img-area {
            background: #F9FAFB;
            height: 180px;
            border-radius: 12px 12px 0 0;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 50px;
        }
        .info-area { padding: 15px; }
        .info-area span { font-size: 0.7rem; font-weight: 700; color: #8B5CF6; text-transform: uppercase; }
        .info-area h4 { font-size: 1rem !important; margin: 5px 0 !important; color: #111827 !important; }
        .price { font-size: 1.2rem; font-weight: 700; color: #111827; }

        /* BOTÃO ADICIONAR */
        div.stButton > button {
            background-color: #7C3AED !important;
            color: white !important;
            border: none !important;
            border-radius: 8px !important;
            width: 100% !important;
            font-weight: 700 !important;
            height: 40px !important;
            font-size: 0.8rem !important;
        }

        /* RODAPÉ CLEAN */
        .footer-clean {
            border-top: 1px solid #F1F1F1;
            margin-top: 60px;
            padding: 30px 0;
            text-align: left;
        }
        .footer-links { display: flex; gap: 20px; margin-bottom: 15px; }
        .footer-links a { color: #6B7280 !important; text-decoration: none; font-size: 0.85rem; font-weight: 500; }
        .copyright { color: #9CA3AF !important; font-size: 0.75rem; }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("""
    <div class="header-container">
        <div class="logo-text">Encanto Liliê</div>
        <div class="search-bar-sim">
            <span class="material-symbols-rounded">search</span> Buscar na loja...
        </div>
        <div style="display:flex; gap:15px; color:#6B7280;">
             <span class="material-symbols-rounded">shopping_cart</span>
             <span class="material-symbols-rounded">person</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- BANNER ---
st.markdown("""
    <div class="hero-banner">
        <div class="hero-text">
            <p style="background:rgba(255,255,255,0.2); display:inline-block; padding:2px 10px; border-radius:5px; font-size:0.7rem; font-weight:700;">NOVIDADE!</p>
            <h1>Kits de Decoração para Festas</h1>
            <p>Transforme momentos em memórias inesquecíveis.</p>
        </div>
        <div style="font-size:80px; opacity:0.8;">✨</div>
    </div>
""", unsafe_allow_html=True)

# --- CATEGORIAS ---
st.markdown("""
    <div class="category-container">
        <div class="cat-chip">🎄 Natal 2025</div>
        <div class="cat-chip">📚 Escolar</div>
        <div class="cat-chip">☕ Canecas</div>
        <div class="cat-chip">🎂 Aniversário</div>
    </div>
""", unsafe_allow_html=True)

# --- PRODUTOS ---
st.markdown("### Produtos em Destaque")
col1, col2, col3, col4 = st.columns(4)

produtos = [
    {"n": "Kit Marmitinha", "p": "R$ 45,90", "t": "Aniversário", "i": "🍱"},
    {"n": "Caneca Pet", "p": "R$ 39,90", "t": "Presentes", "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": "R$ 89,00", "t": "Volta às Aulas", "i": "🎒"},
    {"n": "Agenda 2025", "p": "R$ 65,00", "t": "Papelaria", "i": "📅"}
]

for idx, p in enumerate(produtos):
    with [col1, col2, col3, col4][idx]:
        st.markdown(f"""
            <div class="product-box">
                <div class="img-area">{p['i']}</div>
                <div class="info-area">
                    <span>{p['t']}</span>
                    <h4>{p['n']}</h4>
                    <div class="price">{p['p']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("ADICIONAR", key=f"btn_{idx}")

# --- RODAPÉ ---
st.markdown(f"""
    <div class="footer-clean">
        <div class="footer-links">
            <a href="#">Termos</a>
            <a href="#">Privacidade</a>
            <a href="https://wa.me/55119XXXXXXXX">Contato</a>
            <a href="https://instagram.com/encantolilie_">Instagram</a>
        </div>
        <div class="copyright">
            © 2026 Encanto Liliê | Osasco, SP | CNPJ: 00.000.000/0001-00
        </div>
    </div>
""", unsafe_allow_html=True)
