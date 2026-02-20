import streamlit as st

# 1. Configuração Inicial
st.set_page_config(
    page_title="Encanto Liliê | Catálogo",
    page_icon="✨",
    layout="wide",
)

# 2. Injeção de CSS (Correção de Contraste e Botões)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        .stApp { background-color: #FFFFFF; }
        [data-testid="stHeader"] { visibility: hidden; }
        .block-container { padding-top: 2rem !important; }

        /* Tipografia Principal */
        html, body, [class*="css"], p, span {
            font-family: 'Outfit', sans-serif !important;
            color: #1A1A1A !important; 
        }

        /* Banner Hero */
        .hero-section {
            background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
            padding: 40px 20px;
            border-radius: 24px;
            text-align: center;
            margin-bottom: 30px;
            color: white !important;
        }
        .hero-section h1 { color: white !important; font-weight: 800; margin-bottom: 5px; }
        .hero-section p { color: #FFFFFF !important; opacity: 0.9; }

        /* Links Rápidos (Estilo Linktree) */
        .link-bar {
            background-color: #F3E8FF;
            padding: 15px;
            border-radius: 15px;
            text-align: center;
            margin-bottom: 10px;
            border: 1px solid #DDD6FE;
            transition: 0.3s;
            cursor: pointer;
            display: block;
            text-decoration: none !important;
        }
        .link-bar:hover { background-color: #EDE9FE; transform: translateY(-2px); }
        .link-text { color: #7C3AED !important; font-weight: 700; font-size: 0.9rem; }

        /* Cards de Produto */
        .product-card {
            background: #FFFFFF;
            border-radius: 20px;
            border: 1px solid #F1F5F9;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.03);
        }
        .product-title {
            color: #1A1A1A !important;
            font-weight: 800 !important;
            font-size: 1.2rem !important;
            margin: 15px 0 5px 0 !important;
            display: block;
        }
        .product-tag {
            color: #7C3AED !important;
            font-weight: 700;
            text-transform: uppercase;
            font-size: 0.75rem;
        }

        /* --- AJUSTE DEFINITIVO DOS BOTÕES --- */
        div.stButton > button {
            background-color: #7C3AED !important; /* Roxo Vibrante */
            color: #FFFFFF !important;           /* Texto Branco Puro */
            border-radius: 12px !important;
            border: none !important;
            width: 100% !important;
            height: 55px !important;
            font-size: 1.1rem !important;
            font-weight: 800 !important;         /* Texto Extra Negrito */
            text-transform: uppercase !important;
            letter-spacing: 1px !important;
            box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3) !important;
            margin-top: 10px;
        }
        div.stButton > button:hover {
            background-color: #EC4899 !important; /* Rosa ao passar o mouse */
        }
    </style>
""", unsafe_allow_html=True)

# --- ESTRUTURA DO SITE ---

# 1. Cabeçalho
st.markdown("""
    <div class="hero-section">
        <h1>Encanto Liliê</h1>
        <p>Criatividade que encanta, resultados que marcam 🎯✨</p>
    </div>
""", unsafe_allow_html=True)

# 2. Seção de Canais Oficiais (Baseado no Linktree)
st.write("### 🔗 Nossos Canais")
col_l1, col_l2 = st.columns(2)

with col_l1:
    st.markdown('<a href="https://tr.ee/ZtbOcerQhG" class="link-bar"><span class="link-text">🛍️ LOJA NA SHOPEE</span></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://tr.ee/5D7-CjgLk5" class="link-bar"><span class="link-text">📖 CATÁLOGO CRIATIVO</span></a>', unsafe_allow_html=True)

with col_l2:
    st.markdown('<a href="https://wa.me/55119XXXXXXXX" class="link-bar"><span class="link-text">💬 WHATSAPP DIRETO</span></a>', unsafe_allow_html=True)
    st.markdown('<a href="https://instagram.com/encantolilie_" class="link-bar"><span class="link-text">📸 INSTAGRAM</span></a>', unsafe_allow_html=True)

st.divider()

# 3. Vitrine de Destaques (Inspirado no Instagram)
st.write("### ✨ Destaques da Encanto")

produtos = [
    {"n": "Kit Marmitinha", "t": "Aniversário", "icon": "🍱"},
    {"n": "Kit Escolar Hulk", "t": "Escolar", "icon": "🎒"},
    {"n": "Caneca Pet", "t": "Canecas", "icon": "☕"}
]

c1, c2, c3 = st.columns(3)
for idx, p in enumerate(produtos):
    with [c1, c2, c3][idx]:
        st.markdown(f"""
            <div class="product-card">
                <div style="background:#F8FAFC; padding:30px; border-radius:15px; font-size:60px;">{p['icon']}</div>
                <div class="product-tag">{p['t']}</div>
                <strong class="product-title">{p['n']}</strong>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"Comprar {p['n']}", key=f"btn_{idx}")

# 4. Rodapé
st.markdown(f"""
    <div style='text-align: center; margin-top: 50px; padding: 30px; border-top: 1px solid #EEE;'>
        <p style='font-weight: 800; color: #7C3AED;'>📍 Osasco, São Paulo</p>
        <p style='color: #666; font-size: 0.8rem;'>Enviamos para todo o Brasil 🇧🇷</p>
    </div>
""", unsafe_allow_html=True)
