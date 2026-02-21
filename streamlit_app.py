import streamlit as st

# 1. Configuração de Layout Estilo Loja Virtual
st.set_page_config(
    page_title="Encanto Liliê | Vitrine Personalizada",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# 2. CSS Estilo "Vitrine do Artesanato" (Limpo, Profissional, Contraste Alto)
st.markdown("""
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@24,400,0,0" />
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=Outfit:wght@700&display=swap');
        
        /* Fundo e Container */
        .stApp { background-color: #F9FAFB; }
        .block-container { padding: 0rem 1rem 2rem 1rem !important; max-width: 1200px; }
        
        /* Barra de Topo (Header) */
        .header-loja {
            background-color: #FFFFFF;
            padding: 15px 0;
            border-bottom: 2px solid #7C3AED;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        /* Tipografia de Contraste */
        h1, h2, h3, p, span { font-family: 'Inter', sans-serif !important; color: #111827 !important; }
        .price-tag { color: #EC4899 !important; font-weight: 800; font-size: 1.3rem; }

        /* Banner Principal (Estilo Carrossel) */
        .promo-banner {
            background: linear-gradient(90deg, #7C3AED 0%, #A78BFA 100%);
            color: white !important;
            padding: 40px;
            border-radius: 16px;
            text-align: left;
            margin-bottom: 30px;
            box-shadow: 0 10px 15px -3px rgba(124, 58, 237, 0.2);
        }
        .promo-banner h1 { color: white !important; font-family: 'Outfit', sans-serif !important; margin: 0; }
        .promo-banner p { color: #F3E8FF !important; margin-top: 5px; font-weight: 500; }

        /* Grid de Categorias */
        .cat-card {
            background: white;
            padding: 15px;
            border-radius: 12px;
            text-align: center;
            border: 1px solid #E5E7EB;
            font-weight: 600;
            color: #4B5563;
        }

        /* Card de Produto (Baseado na Vitrine do Artesanato) */
        .product-box {
            background: white;
            border-radius: 12px;
            border: 1px solid #E5E7EB;
            padding: 0;
            overflow: hidden;
            transition: 0.3s;
            margin-bottom: 10px;
        }
        .product-box:hover { border-color: #7C3AED; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
        .img-placeholder {
            background: #F3F4F6;
            height: 200px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #D1D5DB;
        }
        .product-content { padding: 15px; }
        .product-title { font-weight: 700; font-size: 0.95rem; height: 40px; overflow: hidden; }

        /* Botão "Comprar" Robusto */
        div.stButton > button {
            background-color: #7C3AED !important;
            color: white !important;
            font-weight: 800 !important;
            border-radius: 8px !important;
            width: 100% !important;
            height: 48px !important;
            border: none !important;
            text-transform: uppercase;
            font-size: 0.85rem !important;
        }
        div.stButton > button:hover { background-color: #6D28D9 !important; }

        /* Rodapé Informativo */
        .footer-loja {
            background: #111827;
            color: #9CA3AF !important;
            padding: 40px 20px;
            border-radius: 16px 16px 0 0;
            margin-top: 50px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER & BUSCA ---
st.markdown("""
    <div style='display: flex; align-items: center; justify-content: space-between; padding: 10px 0;'>
        <h2 style='margin:0; color:#7C3AED !important; font-family:Outfit;'>Encanto Liliê</h2>
        <div style='background:#F3F4F6; padding:8px 15px; border-radius:8px; width:50%; color:#9CA3AF;'>
            <span class="material-symbols-rounded" style='vertical-align:middle; font-size:18px;'>search</span> Buscar itens personalizados...
        </div>
    </div>
""", unsafe_allow_html=True)

# --- BANNER PRINCIPAL ---
st.markdown("""
    <div class="promo-banner">
        <p>LANÇAMENTO 2025</p>
        <h1>Kits Escolares Personalizados</h1>
        <p>Tudo o que seu pequeno precisa para brilhar na volta às aulas.</p>
    </div>
""", unsafe_allow_html=True)

# --- CANAIS (LINKTREE INTEGRADO) ---
c1, c2, c3, c4 = st.columns(4)
with c1: st.markdown('<div class="cat-card">🛍️ Shopee</div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="cat-card">📖 Catálogo</div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="cat-card">📸 Instagram</div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="cat-card">💬 WhatsApp</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# --- VITRINE DE PRODUTOS ---
st.write("### 💎 Sugestões para Você")

produtos = [
    {"nome": "Kit Marmitinha Personalizada", "preco": "R$ 45,90", "tag": "Aniversário"},
    {"nome": "Caneca Amor em 4 Patas", "preco": "R$ 39,90", "tag": "Presentes"},
    {"nome": "Kit Escolar Hulk (Completo)", "preco": "R$ 89,90", "tag": "Volta às Aulas"},
    {"nome": "Agenda 2025 Personalizada", "preco": "R$ 65,00", "tag": "Papelaria"}
]

col1, col2, col3, col4 = st.columns(4)
cols = [col1, col2, col3, col4]

for i, p in enumerate(produtos):
    with cols[i]:
        st.markdown(f"""
            <div class="product-box">
                <div class="img-placeholder">
                    <span class="material-symbols-rounded" style="font-size: 60px;">image</span>
                </div>
                <div class="product-content">
                    <span style="font-size: 0.7rem; color: #7C3AED; font-weight: 700;">{p['tag']}</span>
                    <div class="product-title">{p['nome']}</div>
                    <div class="price-tag">{p['preco']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.button("ADICIONAR", key=f"prod_{i}")

# --- RODAPÉ ESTILO VITRINE DO ARTESANATO ---
st.markdown("""
    <div class="footer-loja">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 20px;">
            <div>
                <span class="material-symbols-rounded" style="color:#7C3AED">local_shipping</span><br>
                <b>Entrega Segura</b><br><small>Para todo Brasil</small>
            </div>
            <div>
                <span class="material-symbols-rounded" style="color:#7C3AED">payments</span><br>
                <b>Pagamento Facilitado</b><br><small>Pix ou Cartão</small>
            </div>
            <div>
                <span class="material-symbols-rounded" style="color:#7C3AED">verified</span><br>
                <b>Qualidade Encanto</b><br><small>100% artesanal</small>
            </div>
        </div>
        <p style="margin-top:40px; font-size:0.7rem;">Encanto Liliê - Osasco/SP | CNPJ: 00.000.000/0001-00</p>
    </div>
""", unsafe_allow_html=True)
