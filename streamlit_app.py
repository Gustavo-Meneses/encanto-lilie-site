import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | Vitrine 2026",
    page_icon="🌸",
    layout="wide",
)

# 2. Dados dos Banners e Produtos
banners = [
    {"titulo": "Kits Escolares 2026", "sub": "Organização e estilo para a volta às aulas.", "cor": "linear-gradient(135deg, #7C3AED 0%, #EC4899 100%)"},
    {"titulo": "Canecas de Porcelana", "sub": "Personalize com sua foto favorita.", "cor": "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)"},
    {"titulo": "Coleção Natalina", "sub": "Garanta seus presentes com antecedência.", "cor": "linear-gradient(135deg, #10B981 0%, #059669 100%)"}
]

produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "t": "Aniversário", "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "t": "Presentes", "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "t": "Escolar", "i": "🎒"},
    {"n": "Agenda 2025", "p": 65.00, "t": "Papelaria", "i": "📅"}
]

# 3. CSS (Incluindo Fonte Script e Layout do Carrossel)
st.markdown("""
    <style>
        /* Importando Inter para texto normal e Dancing Script para o Título */
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;700;800&display=swap');
        
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        [data-testid="stHeader"] { visibility: hidden; }

        /* Estilo do Título Principal */
        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: 4rem;
            margin-bottom: 10px;
            margin-top: -30px;
        }

        /* Lógica do Carrossel Automático em CSS Puro */
        .slider {
            width: 100%;
            height: 250px;
            position: relative;
            overflow: hidden;
            border-radius: 24px;
            margin-top: 30px;
            margin-bottom: 40px;
        }
        .slides {
            display: flex;
            width: 300%;
            height: 100%;
            animation: slide 12s infinite; /* 3 slides x 4s cada */
        }
        .slide {
            width: 33.33%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            text-align: center;
            padding: 20px;
        }
        @keyframes slide {
            0% { transform: translateX(0); }
            30% { transform: translateX(0); }
            33% { transform: translateX(-33.33%); }
            63% { transform: translateX(-33.33%); }
            66% { transform: translateX(-66.66%); }
            96% { transform: translateX(-66.66%); }
            100% { transform: translateX(0); }
        }

        /* Botões Estilo Shopee/Instagram */
        div.stButton > button {
            background-color: #7C3AED !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            font-weight: 700 !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO CENTRALIZADO E BUSCA ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

# Usando colunas para manter a busca no centro, sem ocupar a tela inteira de ponta a ponta
col_vazia1, col_busca, col_vazia2 = st.columns([1, 2, 1])

with col_busca:
    busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# --- CARROSSEL AUTOMÁTICO COM SETAS ---
c_arrow_l, c_body, c_arrow_r = st.columns([0.1, 0.8, 0.1])

with c_body:
    st.markdown(f"""
        <div class="slider">
            <div class="slides">
                <div class="slide" style="background: {banners[0]['cor']}">
                    <h1>{banners[0]['titulo']}</h1>
                    <p>{banners[0]['sub']}</p>
                </div>
                <div class="slide" style="background: {banners[1]['cor']}">
                    <h1>{banners[1]['titulo']}</h1>
                    <p>{banners[1]['sub']}</p>
                </div>
                <div class="slide" style="background: {banners[2]['cor']}">
                    <h1>{banners[2]['titulo']}</h1>
                    <p>{banners[2]['sub']}</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- VITRINE COM BUSCA ---
st.write("### Produtos em Destaque")
produtos_filtrados = [p for p in produtos if busca.lower() in p['n'].lower() or busca.lower() in p['t'].lower()]

if not produtos_filtrados:
    st.info("Nenhum item encontrado para sua busca.")
else:
    cols = st.columns(4)
    for idx, p in enumerate(produtos_filtrados):
        with cols[idx % 4]:
            st.markdown(f"""
                <div style="border:1px solid #EEE; border-radius:20px; padding:20px; text-align:center;">
                    <div style="font-size:50px; margin-bottom:10px;">{p['i']}</div>
                    <p style="color:#7C3AED; font-weight:700; font-size:0.8rem; margin:0; text-transform:uppercase;">{p['t']}</p>
                    <h4 style="margin:5px 0; color:#111827;">{p['n']}</h4>
                    <h3 style="margin:10px 0; color:#111827;">R$ {p['p']:.2f}</h3>
                </div>
            """, unsafe_allow_html=True)
            st.button("ADICIONAR", key=f"btn_{idx}")

# --- RODAPÉ ALINHADO ---
st.markdown("""
    <hr style="margin-top: 60px;">
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 80px; padding: 20px 0;">
        <div style="display: flex; flex-direction: column; align-items: flex-start;">
            <h5 style="margin-bottom:15px; color:#11182
