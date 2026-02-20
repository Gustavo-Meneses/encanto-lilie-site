import streamlit as st

# Configuração da Página para Mobile First
st.set_page_config(
    page_title="Encanto Liliê - Personalizados",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --- ESTILO CSS PERSONALIZADO (Mobile Friendly & Alta Legibilidade) ---
st.markdown("""
    <link rel="stylesheet" type="text/css" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/duotone/style.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Nunito:wght@400;700;800&display=swap');
    
    /* Configurações Gerais */
    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
        background-color: #FCFAFF;
        color: #2D1B4E; /* Roxo ultra escuro para máxima legibilidade */
    }

    /* Ajuste para Mobile */
    @media (max-width: 768px) {
        .hero h1 { font-size: 2rem !important; }
        .hero p { font-size: 1rem !important; }
        .product-card { margin-bottom: 15px; }
    }

    /* Títulos Delicados */
    h1, h2, h3 {
        font-family: 'Fredoka', sans-serif;
        color: #5B21B6; /* Roxo Vibrante Profundo */
        font-weight: 600;
    }

    /* Banner Principal (Hero) */
    .hero {
        background: linear-gradient(135deg, #7C3AED 0%, #DB2777 100%);
        padding: 40px 20px;
        border-radius: 25px;
        color: white;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 20px rgba(124, 58, 237, 0.2);
    }
    .hero p {
        color: #FDF2F8; /* Rosa claríssimo quase branco para contraste */
        font-weight: 600;
    }

    /* Cards de Produtos */
    .product-card {
        background-color: white;
        padding: 15px;
        border-radius: 20px;
        border: 1px solid #F3E8FF;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        text-align: center;
        transition: transform 0.2s ease;
    }
    .product-card:hover {
        transform: translateY(-5px);
        border-color: #DDD6FE;
    }
    .product-title {
        font-size: 1.2rem;
        font-weight: 800;
        color: #4C1D95;
        margin: 10px 0 5px 0;
    }
    .product-desc {
        font-size: 0.95rem;
        color: #4B5563; /* Cinza grafite (melhor que cinza claro) */
        line-height: 1.4;
        margin-bottom: 15px;
    }

    /* Botões */
    .stButton>button {
        background: #EC4899;
        color: white !important;
        border-radius: 15px;
        border: none;
        padding: 12px 20px;
        font-weight: 700;
        width: 100%;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background: #BE185D;
        box-shadow: 0 5px 15px rgba(236, 72, 153, 0.4);
    }

    /* Rodapé Delicado */
    .footer-container {
        text-align: center;
        padding: 40px 20px;
        background: #F5F3FF;
        border-radius: 30px 30px 0 0;
        margin-top: 50px;
    }
    .footer-icon {
        font-size: 24px;
        color: #7C3AED;
        margin-bottom: 8px;
    }
    .footer-text {
        font-size: 0.9rem;
        font-weight: 700;
        color: #5B21B6;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTEÚDO ---

# Banner
st.markdown("""
    <div class="hero">
        <h1 style="margin:0; color:white;">Encanto Liliê ✨</h1>
        <p style="margin:10px 0 0 0;">Criatividade que encanta, resultados que marcam</p>
    </div>
    """, unsafe_allow_html=True)

# Categorias
st.markdown("### <i class='ph-duotone ph-sparkles' style='color:#7C3AED'></i> Explore nossas fofuras", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1: st.button("🎄 Natal 2025")
with c2: st.button("📚 Kits Escolares")
with c3: st.button("☕ Canecas")

st.markdown("<br>", unsafe_allow_html=True)

# Vitrine
st.markdown("### <i class='ph-duotone ph-heart' style='color:#EC4899'></i> Destaques do Catálogo", unsafe_allow_html=True)

items = [
    {"n": "Kit Marmitinha Bolofofos", "d": "Personalizada com nome e idade. Ideal para festas infantis.", "c": "#A78BFA"},
    {"n": "Kit Escolar Heróis", "d": "Etiquetas e toalhinha para volta às aulas.", "c": "#34D399"},
    {"n": "Caneca Amor Pet", "d": "Sua foto favorita estampada com alta qualidade.", "c": "#F472B6"}
]

cols = st.columns(3)
for i, item in enumerate(items):
    with cols[i]:
        st.markdown(f"""
            <div class="product-card">
                <div style="background:{item['c']}; height:180px; border-radius:12px; display:flex; align-items:center; justify-content:center; color:white; font-size:40px;">
                    <i class="ph-duotone ph-package"></i>
                </div>
                <div class="product-title">{item['n']}</div>
                <div class="product-desc">{item['d']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"Encomendar via WhatsApp", key=f"btn_{i}")

# --- RODAPÉ DELICADO ---
st.markdown("""
    <div class="footer-container">
        <div style="display: flex; justify-content: space-around; max-width: 600px; margin: 0 auto;">
            <div>
                <i class="ph-duotone ph-truck footer-icon"></i>
                <div class="footer-text">Envio Nacional</div>
            </div>
            <div>
                <i class="ph-duotone ph-instagram-logo footer-icon"></i>
                <div class="footer-text">@encantolilie_</div>
            </div>
            <div>
                <i class="ph-duotone ph-map-pin footer-icon"></i>
                <div class="footer-text">Osasco, SP</div>
            </div>
        </div>
        <p style="margin-top:30px; font-size:0.8rem; color:#9CA3AF;">© 2026 Encanto Liliê - Feito com carinho.</p>
    </div>
    """, unsafe_allow_html=True)
