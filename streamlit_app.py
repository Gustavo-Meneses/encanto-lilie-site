import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. Configuração de Página
st.set_page_config(
    page_title="Encanto Liliê | Loja Criativa",
    page_icon="🌸",
    layout="wide",
)

# 2. Lógica do Carrossel Automático (3 segundos)
# Atualiza o app a cada 3000ms (3 segundos)
count = st_autorefresh(interval=3000, key="carouselframerate")

# 3. Dados dos Produtos e Banners
banners = [
    {"titulo": "Kits Escolares 2026", "sub": "Organização e estilo para a volta às aulas.", "cor": "linear-gradient(135deg, #7C3AED 0%, #EC4899 100%)", "icon": "🎒"},
    {"titulo": "Canecas de Porcelana", "sub": "Personalize com sua foto favorita.", "cor": "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)", "icon": "☕"},
    {"titulo": "Coleção Natalina", "sub": "Garanta seus presentes com antecedência.", "cor": "linear-gradient(135deg, #10B981 0%, #059669 100%)", "icon": "🎄"}
]

produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "t": "Aniversário", "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "t": "Presentes", "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "t": "Escolar", "i": "🎒"},
    {"n": "Agenda 2025", "p": 65.00, "t": "Papelaria", "i": "📅"}
]

# 4. Estilização CSS Clean
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        .stApp {{ background-color: #FFFFFF; }}
        [data-testid="stHeader"] {{ visibility: hidden; }}
        
        /* Banner Carrossel */
        .banner-box {{
            padding: 50px 30px;
            border-radius: 24px;
            color: white !important;
            text-align: center;
            margin-bottom: 30px;
            animation: fadeIn 0.8s;
        }}
        @keyframes fadeIn {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}

        /* Botão Adicionar */
        div.stButton > button {{
            background-color: #7C3AED !important;
            color: white !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            width: 100% !important;
            border: none !important;
            height: 45px !important;
        }}

        /* Rodapé */
        .footer-v2 {{
            background-color: #F9FAFB;
            padding: 60px 20px 30px 20px;
            margin-top: 80px;
            border-top: 1px solid #EEE;
        }}
        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 40px;
            max-width: 1200px;
            margin: 0 auto;
        }}
        .footer-col h5 {{ color: #111827; font-weight: 800; margin-bottom: 20px; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }}
        .footer-col a {{ color: #6B7280 !important; text-decoration: none; display: block; margin-bottom: 12px; font-size: 0.9rem; }}
        .footer-col a:hover {{ color: #7C3AED !important; }}
    </style>
""", unsafe_allow_html=True)

# --- HEADER & BUSCA ---
col_logo, col_search = st.columns([1, 2])
with col_logo:
    st.markdown("<h2 style='margin: 0;'>Encanto Liliê</h2>", unsafe_allow_html=True)

with col_search:
    busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# --- CARROSSEL AUTOMÁTICO (Lógica de Troca) ---
# O 'count' do autorefresh faz o índice mudar sozinho
idx_banner = count % len(banners)
atual = banners[idx_banner]

st.markdown(f"""
    <div class="banner-box" style="background: {atual['cor']}">
        <div style="font-size: 50px; margin-bottom: 10px;">{atual['icon']}</div>
        <h1 style="color:white !important; margin:0;">{atual['titulo']}</h1>
        <p style="color:white !important; opacity:0.9; font-size:1.1rem;">{atual['sub']}</p>
    </div>
""", unsafe_allow_html=True)

# --- VITRINE COM BUSCA ---
st.write("### Destaques para você")
produtos_filtrados = [p for p in produtos if busca.lower() in p['n'].lower() or busca.lower() in p['t'].lower()]

if not produtos_filtrados:
    st.info("Nenhum item encontrado. Tente buscar por 'Caneca' ou 'Escolar'.")
else:
    cols = st.columns(4)
    for idx, p in enumerate(produtos_filtrados):
        with cols[idx % 4]:
            st.markdown(f"""
                <div style="border:1px solid #F1F1F1; border-radius:20px; padding:20px; background:white; transition: 0.3s;">
                    <div style="font-size:55px; text-align:center; padding:25px; background:#FDFDFD; border-radius:15px;">{p['i']}</div>
                    <p style="color:#7C3AED; font-weight:800; font-size:0.7rem; text-transform:uppercase; margin-top:15px;">{p['t']}</p>
                    <h4 style="margin:5px 0; font-size:1rem; color:#111827;">{p['n']}</h4>
                    <h3 style="margin:10px 0; color:#111827;">R$ {p['p']:.2f}</h3>
                </div>
            """, unsafe_allow_html=True)
            st.button("ADICIONAR", key=f"prod_{idx}")

# --- RODAPÉ ---
st.markdown("""
    <div class="footer-v2">
        <div class="footer-grid">
            <div class="footer-col">
                <h5>Canais Oficiais</h5>
                <a href="https://wa.me/55119XXXXXXXX" target="_blank">💬 WhatsApp</a>
                <a href="https://instagram.com/encantolilie_" target="_blank">📸 Instagram</a>
                <a href="https://tr.ee/ZtbOcerQhG" target="_blank">🛍️ Loja Shopee</a>
            </div>
            <div class="footer-col">
                <h5>Atendimento</h5>
                <a href="https://tr.ee/5D7-CjgLk5" target="_blank">📖 Catálogo Digital</a>
                <a href="#">📦 Rastrear Pedido</a>
                <a href="#">💡 Dúvidas Frequentes</a>
            </div>
            <div class="footer-col">
                <h5>Jurídico 2026</h5>
                <a href="#" onclick="alert('Termos de Uso LGPD 2026: Seus dados estão protegidos por criptografia de ponta e são usados apenas para processamento de pedidos.')">📄 Termos de Uso</a>
                <a href="#" onclick="alert('Política de Privacidade: Não compartilhamos dados com terceiros e seguimos as normas vigentes de proteção ao consumidor.')">🔒 Privacidade</a>
            </div>
        </div>
        <div style="text-align:center; margin-top:50px; color:#9CA3AF; font-size:0.75rem; border-top: 1px solid #EEE; padding-top: 20px;">
            © 2026 Encanto Liliê | Criatividade que encanta. <br>
            CNPJ 00.000.000/0001-00 | Osasco, São Paulo.
        </div>
    </div>
""", unsafe_allow_html=True)
