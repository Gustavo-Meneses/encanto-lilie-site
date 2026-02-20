import streamlit as st

# 1. CONFIGURAÇÃO DA PÁGINA (Precisa ser a primeira linha)
st.set_page_config(
    page_title="Encanto Liliê - Catálogo",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. INJEÇÃO DE ESTILO (Ajustado para não vazar texto no topo)
def aplicar_estilo():
    st.markdown("""
        <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/duotone/style.css">
        <style>
            /* Esconde elementos nativos desnecessários */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}

            /* Fontes e Cores Base */
            @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Nunito:wght@400;700;800&display=swap');
            
            .stApp {
                background-color: #FCFAFF;
            }

            /* Texto com Contraste Máximo */
            h1, h2, h3, h4, p, span, div {
                font-family: 'Nunito', sans-serif !important;
                color: #1A0B2E !important; /* Roxo Noite para leitura clara */
            }

            .hero-title {
                font-family: 'Fredoka', sans-serif !important;
                font-size: 2.5rem !important;
                font-weight: 600 !important;
                color: #FFFFFF !important;
                margin-bottom: 0px;
            }

            /* Banner */
            .hero-container {
                background: linear-gradient(135deg, #7C3AED 0%, #EC4899 100%);
                padding: 40px 20px;
                border-radius: 20px;
                text-align: center;
                margin-bottom: 30px;
                box-shadow: 0 10px 20px rgba(124, 58, 237, 0.15);
            }

            /* Cards de Produto */
            .product-card {
                background-color: #FFFFFF;
                padding: 15px;
                border-radius: 18px;
                border: 1px solid #E9D5FF;
                box-shadow: 0 4px 6px rgba(0,0,0,0.02);
                text-align: center;
                margin-bottom: 10px;
            }

            .product-title {
                font-weight: 800;
                color: #4C1D95 !important;
                font-size: 1.1rem;
                margin-top: 10px;
            }

            .product-desc {
                font-size: 0.9rem;
                color: #374151 !important; /* Cinza escuro/grafite */
                line-height: 1.3;
            }

            /* Botão Customizado */
            div.stButton > button {
                background-color: #EC4899 !important;
                color: white !important;
                border: none !important;
                border-radius: 12px !important;
                padding: 10px 20px !important;
                font-weight: 700 !important;
                width: 100%;
                transition: 0.3s;
            }
            div.stButton > button:hover {
                background-color: #BE185D !important;
                transform: scale(1.02);
            }

            /* Rodapé */
            .footer-box {
                background-color: #F5F3FF;
                padding: 30px;
                border-radius: 20px;
                text-align: center;
                margin-top: 40px;
            }
        </style>
    """, unsafe_allow_html=True)

aplicar_estilo()

# --- CONTEÚDO DA PÁGINA ---

# Banner Principal
st.markdown("""
    <div class="hero-container">
        <h1 class="hero-title">Encanto Liliê ✨</h1>
        <p style="color: #FDF2F8 !important; font-weight: 600; opacity: 0.9;">Criatividade que encanta, resultados que marcam</p>
    </div>
    """, unsafe_allow_html=True)

# Categorias Rápidas
st.markdown("### <i class='ph-duotone ph-circles-four'></i> Categorias", unsafe_allow_html=True)
cat_cols = st.columns(3)
with cat_cols[0]: st.button("🎄 Natal")
with cat_cols[1]: st.button("📚 Escolar")
with cat_cols[2]: st.button("☕ Canecas")

st.markdown("---")

# Vitrine de Produtos (Inspirada no Instagram)
st.markdown("### <i class='ph-duotone ph-star'></i> Mais Vendidos", unsafe_allow_html=True)

# Simulando fotos do catálogo com ícones delicados
produtos = [
    {"nome": "Kit Marmitinha", "desc": "Personalizada com o tema da sua festa.", "cor": "#DDD6FE", "ícone": "ph-package"},
    {"nome": "Kit Escolar Hulk", "desc": "Toalhinha e etiquetas resistentes.", "cor": "#D1FAE5", "ícone": "ph-backpack"},
    {"nome": "Caneca Pet", "desc": "Sua foto favorita em uma caneca linda.", "cor": "#FCE7F3", "ícone": "ph-coffee"}
]

prod_cols = st.columns(3)
for idx, p in enumerate(produtos):
    with prod_cols[idx]:
        st.markdown(f"""
            <div class="product-card">
                <div style="background:{p['cor']}; height:150px; border-radius:12px; display:flex; align-items:center; justify-content:center;">
                    <i class="{p['ícone']}" style="font-size: 50px; color: #6D28D9;"></i>
                </div>
                <div class="product-title">{p['nome']}</div>
                <div class="product-desc">{p['desc']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"Pedir no WhatsApp", key=f"p_{idx}")

# Rodapé Delicado
st.markdown("""
    <div class="footer-box">
        <div style="display: flex; justify-content: center; gap: 30px; margin-bottom: 15px;">
            <span><i class="ph-duotone ph-truck" style="font-size:24px; color:#7C3AED;"></i><br><b>Envios</b></span>
            <span><i class="ph-duotone ph-instagram-logo" style="font-size:24px; color:#7C3AED;"></i><br><b>Instagram</b></span>
            <span><i class="ph-duotone ph-map-pin" style="font-size:24px; color:#7C3AED;"></i><br><b>Osasco</b></span>
        </div>
        <p style="font-size: 0.8rem; opacity: 0.7;">© 2026 Encanto Liliê - Papelaria e Personalizados</p>
    </div>
    """, unsafe_allow_html=True)
