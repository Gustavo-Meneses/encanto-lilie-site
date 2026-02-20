import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê - Catálogo",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Injeção de CSS e Ícones (Tudo em um único bloco para evitar erros)
st.markdown("""
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/duotone/style.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Nunito:wght@400;700;800&display=swap');
    
    /* Reset e Cores de Fundo */
    .main {
        background-color: #FCFAFF;
    }

    /* Fontes e Textos - Ajustados para alta visibilidade */
    html, body, [class*="css"], p, span {
        font-family: 'Nunito', sans-serif !important;
        color: #1A0B2E !important; /* Roxo Quase Preto para leitura perfeita */
    }

    h1, h2, h3 {
        font-family: 'Fredoka', sans-serif !important;
        color: #4C1D95 !important; /* Roxo Profundo */
        font-weight: 600;
    }

    /* Banner Principal */
    .hero-container {
        background: linear-gradient(135deg, #6D28D9 0%, #BE185D 100%);
        padding: 50px 20px;
        border-radius: 25px;
        color: #FFFFFF !important;
        text-align: center;
        margin-bottom: 35px;
        box-shadow: 0 8px 25px rgba(109, 40, 217, 0.2);
    }

    /* Cards de Produtos */
    .st-emotion-cache-1r6slb0, .product-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 20px;
        border: 2px solid #F3E8FF; /* Borda mais nítida */
        box-shadow: 0 4px 10px rgba(0,0,0,0.03);
        text-align: center;
    }

    .product-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: #4C1D95;
        margin-top: 15px;
    }

    .product-desc {
        font-size: 1rem;
        color: #374151 !important; /* Cinza Escuro (Grafite) */
        line-height: 1.5;
        margin-bottom: 20px;
    }

    /* Botão Rosa Encanto */
    div.stButton > button:first-child {
        background-color: #EC4899 !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 15px 25px !important;
        font-weight: 700 !important;
        width: 100% !important;
        transition: 0.3s ease !important;
    }
    
    div.stButton > button:first-child:hover {
        background-color: #BE185D !important;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4) !important;
        transform: scale(1.02);
    }

    /* Rodapé Delicado */
    .footer {
        background-color: #F5F3FF;
        padding: 40px 20px;
        border-radius: 30px 30px 0 0;
        text-align: center;
        margin-top: 60px;
        border-top: 2px solid #EDE9FE;
    }

    .footer i {
        font-size: 28px;
        color: #7C3AED;
        display: block;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- INÍCIO DO CONTEÚDO VISÍVEL ---

# Banner Hero
st.markdown("""
    <div class="hero-container">
        <h1 style="color: white; margin-bottom: 10px;">Encanto Liliê ✨</h1>
        <p style="color: #FDF2F8; font-size: 1.2rem; font-weight: 600;">Criatividade que encanta, resultados que marcam</p>
    </div>
    """, unsafe_allow_html=True)

# Categorias
st.subheader("Categorias")
c1, c2, c3 = st.columns(3)
with c1: st.button("🎄 Natal 2025", key="cat1")
with c2: st.button("📚 Kits Escolares", key="cat2")
with c3: st.button("☕ Canecas", key="cat3")

st.markdown("<br>", unsafe_allow_html=True)

# Vitrine de Produtos
st.markdown("### Destaques do Catálogo")

# Lista de Produtos (Exemplo)
produtos = [
    {"nome": "Kit Marmitinha", "desc": "Personalizada com nome e idade. Ideal para festas infantis.", "cor": "#A78BFA"},
    {"nome": "Kit Escolar Hulk", "desc": "Etiquetas e toalhinha para volta às aulas resistentes à água.", "cor": "#34D399"},
    {"nome": "Caneca Pet", "desc": "Sua foto favorita estampada em porcelana de alta qualidade.", "cor": "#F472B6"}
]

cols = st.columns(3)

for i, p in enumerate(produtos):
    with cols[i]:
        # Card Visual
        st.markdown(f"""
            <div class="product-card">
                <div style="background:{p['cor']}; height:180px; border-radius:12px; display:flex; align-items:center; justify-content:center; color:white; font-size:50px;">
                    <i class="ph-duotone ph-gift"></i>
                </div>
                <div class="product-title">{p['nome']}</div>
                <div class="product-desc">{p['desc']}</div>
            </div>
        """, unsafe_allow_html=True)
        # Botão de Ação
        st.button(f"Pedir no WhatsApp", key=f"btn_{i}")

# Rodapé
st.markdown("""
    <div class="footer">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px;">
            <div>
                <i class="ph-duotone ph-truck"></i>
                <b style="color:#5B21B6">Envio Nacional</b>
            </div>
            <div>
                <i class="ph-duotone ph-instagram-logo"></i>
                <b style="color:#5B21B6">@encantolilie_</b>
            </div>
            <div>
                <i class="ph-duotone ph-whatsapp-logo"></i>
                <b style="color:#5B21B6">Osasco, SP</b>
            </div>
        </div>
        <p style="margin-top:40px; font-size:0.9rem; color:#6B7280;">© 2026 Encanto Liliê | Feito com carinho para você.</p>
    </div>
    """, unsafe_allow_html=True)
