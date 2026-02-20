import streamlit as st

# 1. Configuração Inicial
st.set_page_config(
    page_title="Encanto Liliê",
    page_icon="✨",
    layout="wide",
)

# 2. Injeção de CSS (Visual Clean & Mobile-First)
st.markdown("""
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;800&display=swap');
        
        /* Reset de Interface */
        .stApp { background-color: #FFFFFF; }
        [data-testid="stHeader"], [data-testid="stFooter"] { visibility: hidden; }
        .block-container { padding-top: 2rem !important; }

        /* Tipografia de Alto Contraste */
        html, body, [class*="css"], p, span {
            font-family: 'Outfit', sans-serif !important;
            color: #0F172A !important; /* Texto Escuro para Leitura */
        }

        /* Banner Minimalista */
        .hero-section {
            background: linear-gradient(135deg, #8B5CF6 0%, #D946EF 100%);
            padding: 40px 20px;
            border-radius: 24px;
            text-align: center;
            margin-bottom: 30px;
            color: white !important;
        }
        .hero-section h1 { color: white !important; font-weight: 800; margin-bottom: 5px; }
        .hero-section p { color: #F5F3FF !important; font-weight: 400; opacity: 0.9; }

        /* Chips de Categoria */
        .chip {
            display: inline-block;
            padding: 6px 14px;
            background: #F8FAFC;
            border: 1px solid #E2E8F0;
            border-radius: 100px;
            margin: 4px;
            font-size: 0.85rem;
            font-weight: 600;
            color: #64748B;
        }

        /* Cards de Produto Estilo 'Boutique' */
        .product-card {
            background: #FFFFFF;
            border-radius: 20px;
            border: 1px solid #F1F5F9;
            padding: 16px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }
        .img-box {
            background: #F8FAFC;
            height: 180px;
            border-radius: 15px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 12px;
        }

        /* Botão de Ação */
        div.stButton > button {
            background-color: #0F172A !important;
            color: white !important;
            border-radius: 12px !important;
            border: none !important;
            width: 100% !important;
            height: 45px !important;
            font-weight: 600 !important;
            transition: 0.2s;
        }
        div.stButton > button:hover {
            background-color: #334155 !important;
            transform: translateY(-2px);
        }

        /* Rodapé Mobile */
        .footer-clean {
            text-align: center;
            padding: 40px 10px;
            margin-top: 30px;
            border-top: 1px solid #F1F5F9;
        }
    </style>
""", unsafe_allow_html=True)

# --- CONTEÚDO ---

# 1. Header Hero [Inspirado na Bio do Instagram]
st.markdown("""
    <div class="hero-section">
        <h1>Encanto Liliê</h1>
        <p>Criatividade que encanta, resultados que marcam 🎯</p>
    </div>
""", unsafe_allow_html=True)

# 2. Categorias (Filtros Limpos)
st.write("### Categorias")
st.markdown("""
    <div>
        <span class="chip">🎄 Natal</span>
        <span class="chip">📚 Escolar</span>
        <span class="chip">☕ Canecas</span>
        <span class="chip">🎂 Aniversário</span>
    </div>
    <br>
""", unsafe_allow_html=True)

# 3. Vitrine (Grid Simples para não quebrar no mobile)
st.write("### Destaques")

# Dados dos produtos
produtos = [
    {"n": "Kit Marmitinha", "t": "Aniversário", "icon": "🎁"},
    {"n": "Kit Escolar Heróis", "t": "Escolar", "icon": "🎨"},
    {"n": "Caneca Personalizada", "t": "Canecas", "icon": "☕"}
]

# Usando colunas simples (Streamlit cuida do mobile automaticamente)
col1, col2, col3 = st.columns([1, 1, 1])

for idx, p in enumerate(produtos):
    target = [col1, col2, col3][idx % 3]
    with target:
        st.markdown(f"""
            <div class="product-card">
                <div class="img-box">
                    <span style="font-size: 50px;">{p['icon']}</span>
                </div>
                <div style="font-size: 0.75rem; color: #8B5CF6; font-weight: 700; text-transform: uppercase;">{p['t']}</div>
                <div style="font-weight: 800; font-size: 1.1rem; margin-bottom: 10px;">{p['n']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.button("Pedir agora", key=f"p_{idx}")

# 4. Rodapé Limpo
st.markdown("""
    <div class="footer-clean">
        <p style="font-size: 0.9rem; font-weight: 600;">📍 Osasco, São Paulo</p>
        <p style="font-size: 0.8rem; color: #64748B;">@encantolilie_</p>
        <p style="font-size: 0.7rem; color: #94A3B8; margin-top: 20px;">© 2026 Encanto Liliê</p>
    </div>
""", unsafe_allow_html=True)
