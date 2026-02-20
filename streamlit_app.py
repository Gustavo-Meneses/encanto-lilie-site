import streamlit as st

# 1. Configuração Inicial
st.set_page_config(
    page_title="Encanto Liliê",
    page_icon="✨",
    layout="wide",
)

# 2. Injeção de CSS (Foco total na correção dos botões e contraste)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        /* Reset Geral */
        .stApp { background-color: #FFFFFF; }
        [data-testid="stHeader"] { visibility: hidden; }
        .block-container { padding-top: 2rem !important; }

        /* Tipografia de Alto Contraste para nomes e textos */
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
        .hero-section h1 { color: white !important; font-weight: 800; }
        .hero-section p { color: #FFFFFF !important; font-weight: 400; opacity: 0.9; }

        /* Chips de Categoria */
        .chip {
            display: inline-block;
            padding: 8px 16px;
            background: #F3E8FF;
            border-radius: 100px;
            margin: 4px;
            font-size: 0.85rem;
            font-weight: 700;
            color: #7C3AED !important;
        }

        /* Cards de Produto */
        .product-card {
            background: #FFFFFF;
            border-radius: 20px;
            border: 1px solid #F1F5F9;
            padding: 16px;
            margin-bottom: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
            text-align: center;
        }
        .img-box {
            background: #F8FAFC;
            height: 180px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 15px;
        }

        /* --- CORREÇÃO DOS BOTÕES (VISIBILIDADE TOTAL) --- */
        div.stButton > button {
            background-color: #7C3AED !important; /* Roxo vibrante */
            color: #FFFFFF !important;           /* Texto Branco */
            border-radius: 12px !important;
            border: none !important;
            width: 100% !important;
            height: 50px !important;
            font-size: 1rem !important;
            font-weight: 800 !important;        /* Texto bem grosso */
            box-shadow: 0 4px 10px rgba(124, 58, 237, 0.3) !important;
            transition: 0.3s ease !important;
            margin-top: 5px;
        }

        div.stButton > button:hover {
            background-color: #EC4899 !important; /* Muda para Rosa no hover */
            transform: scale(1.02);
        }

        /* Ajuste para o texto do produto não ficar apagado */
        .product-title {
            color: #1A1A1A !important;
            font-weight: 800 !important;
            font-size: 1.1rem !important;
            margin: 10px 0 !important;
            display: block;
        }

        .product-tag {
            color: #7C3AED !important;
            font-weight: 700 !important;
            text-transform: uppercase;
            font-size: 0.75rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTEÚDO DA PÁGINA ---

# Banner
st.markdown("""
    <div class="hero-section">
        <h1>Encanto Liliê</h1>
        <p>Criatividade que encanta, resultados que marcam 🎯</p>
    </div>
""", unsafe_allow_html=True)

# Categorias
st.write("### Categorias")
st.markdown("""
    <div>
        <span class="chip">🎄 Natal 2025</span>
        <span class="chip">📚 Kits Escolares</span>
        <span class="chip">☕ Canecas</span>
        <span class="chip">🎂 Aniversário</span>
    </div>
    <br>
""", unsafe_allow_html=True)

# Destaques
st.write("### Destaques do Catálogo")

# Dados atualizados conforme as fotos do Instagram enviadas
produtos = [
    {"n": "Kit Marmitinha", "t": "Aniversário", "icon": "🎁"},
    {"n": "Kit Escolar Heróis", "t": "Escolar", "icon": "🎨"},
    {"n": "Caneca Personalizada", "t": "Canecas", "icon": "☕"}
]

col1, col2, col3 = st.columns(3)

for idx, p in enumerate(produtos):
    with [col1, col2, col3][idx]:
        st.markdown(f"""
            <div class="product-card">
                <div class="img-box">
                    <span style="font-size: 55px;">{p['icon']}</span>
                </div>
                <div class="product-tag">{p['t']}</div>
                <div class="product-title">{p['n']}</div>
            </div>
        """, unsafe_allow_html=True)
        # O botão agora terá o texto "Ver Detalhes" ou "Pedir no Whats" bem visível
        st.button(f"Pedir no WhatsApp", key=f"btn_{idx}")

# Rodapé
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; border-top: 1px solid #EEE; padding-top: 20px;'>
        <p style='font-weight: 600; color: #7C3AED;'>📍 Osasco, São Paulo</p>
        <p style='font-size: 0.8rem; color: #666;'>© 2026 Encanto Liliê | @encantolilie_</p>
    </div>
""", unsafe_allow_html=True)
