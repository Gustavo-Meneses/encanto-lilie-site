import streamlit as st

# 1. Configuração Inicial (Sempre a primeira linha)
st.set_page_config(
    page_title="Encanto Liliê",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. Injeção de CSS Robusta (Para não vazar texto e otimizar Mobile)
st.markdown("""
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />
    <style>
        /* Esconder elementos nativos do Streamlit */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding-top: 2rem; padding-bottom: 2rem;}

        /* Fontes e Background */
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Plus Jakarta Sans', sans-serif !important;
            background-color: #FFFFFF !important;
        }

        /* Texto com alto contraste */
        h1, h2, h3, p, span {
            color: #111827 !important; /* Quase preto para leitura perfeita */
        }

        /* Banner Clean */
        .hero {
            background: #7C3AED;
            padding: 30px 20px;
            border-radius: 24px;
            color: white !important;
            text-align: center;
            margin-bottom: 25px;
        }
        .hero h1 { color: white !important; font-size: 1.8rem !important; margin-bottom: 5px; }
        .hero p { color: #DDD6FE !important; font-size: 0.9rem !important; font-weight: 400; }

        /* Categorias Estilo 'Pill' */
        .category-chip {
            display: inline-flex;
            align-items: center;
            padding: 8px 16px;
            background: #F3F4F6;
            border-radius: 100px;
            margin: 4px;
            font-size: 0.85rem;
            font-weight: 600;
            color: #4B5563;
        }

        /* Cards de Produto - Estilo Minimalista */
        .product-card {
            background: #FFFFFF;
            border-radius: 20px;
            border: 1px solid #F3F4F6;
            padding: 12px;
            margin-bottom: 15px;
            transition: all 0.2s ease;
        }
        .product-image-placeholder {
            background: #F9FAFB;
            height: 160px;
            border-radius: 16px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #7C3AED;
        }
        .product-info { padding: 10px 5px; }
        .product-name { font-weight: 700; font-size: 1rem; color: #111827; }
        .product-price { color: #EC4899; font-weight: 800; font-size: 1.1rem; }

        /* Botão WhatsApp Estilo App */
        div.stButton > button {
            background: #111827 !important;
            color: #FFFFFF !important;
            border-radius: 14px !important;
            border: none !important;
            height: 48px !important;
            width: 100% !important;
            font-weight: 600 !important;
            font-size: 0.9rem !important;
            text-transform: none !important;
        }

        /* Ajustes de Grid para Celular */
        @media (max-width: 640px) {
            .hero { padding: 25px 15px; }
            .hero h1 { font-size: 1.5rem !important; }
        }
    </style>
""", unsafe_allow_html=True)

# --- INTERFACE ---

# 1. Header Hero
st.markdown("""
    <div class="hero">
        <h1>Encanto Liliê</h1>
        <p>Artesanatos feitos com amor e criatividade ✨</p>
    </div>
""", unsafe_allow_html=True)

# 2. Filtros/Categorias (Chips)
st.markdown("### <span class='material-symbols-rounded' style='vertical-align: middle; margin-right: 5px;'>grid_view</span> Categorias", unsafe_allow_html=True)
st.markdown("""
    <div style='margin-bottom: 20px;'>
        <span class="category-chip">🎄 Natal</span>
        <span class="category-chip">📚 Escolar</span>
        <span class="category-chip">☕ Canecas</span>
        <span class="category-chip">🎂 Festas</span>
    </div>
""", unsafe_allow_html=True)

# 3. Vitrine de Produtos (Grid Responsivo)
st.markdown("### <span class='material-symbols-rounded' style='vertical-align: middle; margin-right: 5px;'>auto_awesome</span> Destaques", unsafe_allow_html=True)

# Lista de itens baseada na imagem enviada
produtos = [
    {"nome": "Kit Marmitinha Personalizada", "tag": "Aniversário", "icon": "featured_seasonal"},
    {"nome": "Kit Escolar (Hulk/Heróis)", "tag": "Escolar", "icon": "school"},
    {"nome": "Caneca Amor em 4 Patas", "tag": "Presentes", "icon": "coffee"}
]

# Grid: 1 coluna no celular, 3 no computador
cols = st.columns([1, 1, 1] if not st.get_option("setup.is_shm_enabled") else 1) # Hack simples para mobile
col1, col2, col3 = st.columns(3)

for idx, p in enumerate(produtos):
    target_col = [col1, col2, col3][idx % 3]
    with target_col:
        st.markdown(f"""
            <div class="product-card">
                <div class="product-image-placeholder">
                    <span class="material-symbols-rounded" style="font-size: 48px;">{p['icon']}</span>
                </div>
                <div class="product-info">
                    <div style="font-size: 0.75rem; color: #7C3AED; font-weight: 600;">{p['tag']}</div>
                    <div class="product-name">{p['nome']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Encomendar", key=f"btn_{idx}")

# 4. Rodapé Minimalista
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
    <div style='text-align: center; border-top: 1px solid #F3F4F6; padding-top: 30px; margin-bottom: 50px;'>
        <div style='display: flex; justify-content: center; gap: 25px; color: #6B7280;'>
            <div style='text-align: center;'>
                <span class="material-symbols-rounded">local_shipping</span><br>
                <span style='font-size: 0.7rem; font-weight: 600;'>Envios</span>
            </div>
            <div style='text-align: center;'>
                <span class="material-symbols-rounded">verified_user</span><br>
                <span style='font-size: 0.7rem; font-weight: 600;'>Seguro</span>
            </div>
            <div style='text-align: center;'>
                <span class="material-symbols-rounded">chat_bubble</span><br>
                <span style='font-size: 0.7rem; font-weight: 600;'>Suporte</span>
            </div>
        </div>
        <p style='font-size: 0.75rem; color: #9CA3AF; margin-top: 25px;'>© 2026 Encanto Liliê | Osasco - SP</p>
    </div>
""", unsafe_allow_html=True)
