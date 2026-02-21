import streamlit as st
import time

# 1. Configuração de Página
st.set_page_config(
    page_title="Encanto Liliê | Vitrine 2026",
    page_icon="🌸",
    layout="wide",
)

# 2. Dados dos Produtos e Carrossel
produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "t": "Aniversário", "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "t": "Presentes", "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "t": "Escolar", "i": "🎒"},
    {"n": "Agenda 2025", "p": 65.00, "t": "Papelaria", "i": "📅"}
]

banners = [
    {"titulo": "Kits Escolares 2026", "sub": "Organização e estilo para a volta às aulas.", "cor": "linear-gradient(135deg, #7C3AED 0%, #EC4899 100%)"},
    {"titulo": "Canecas de Porcelana", "sub": "Personalize com sua foto favorita.", "cor": "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)"},
    {"titulo": "Coleção Natalina", "sub": "Garanta seus presentes com antecedência.", "cor": "linear-gradient(135deg, #10B981 0%, #059669 100%)"}
]

# 3. Estilo CSS (Foco em Clean Design e Rodapé)
st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        .stApp {{ background-color: #FFFFFF; }}
        [data-testid="stHeader"] {{ visibility: hidden; }}
        
        /* Cabeçalho */
        .header-clean {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
            border-bottom: 1px solid #F3F4F6;
        }}
        
        /* Banner Carrossel */
        .banner-box {{
            padding: 40px;
            border-radius: 20px;
            color: white !important;
            text-align: center;
            transition: all 0.5s ease;
            margin: 20px 0;
        }}

        /* Botão Adicionar */
        div.stButton > button {{
            background-color: #7C3AED !important;
            color: white !important;
            font-weight: 700 !important;
            border-radius: 10px !important;
            width: 100% !important;
            height: 45px !important;
            border: none !important;
        }}

        /* Rodapé Profissional */
        .footer-v2 {{
            background-color: #F9FAFB;
            padding: 50px 20px;
            margin-top: 80px;
            border-top: 1px solid #E5E7EB;
        }}
        .footer-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 30px;
            max-width: 1100px;
            margin: 0 auto;
        }}
        .footer-col h5 {{ color: #111827; font-weight: 800; margin-bottom: 15px; }}
        .footer-col a {{ 
            color: #6B7280 !important; 
            text-decoration: none; 
            display: block; 
            margin-bottom: 10px; 
            font-size: 0.9rem;
        }}
        .footer-col a:hover {{ color: #7C3AED !important; }}
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
col_logo, col_search = st.columns([1, 2])
with col_logo:
    st.markdown("<h2 style='margin-top:10px;'>Encanto Liliê</h2>", unsafe_allow_html=True)

with col_search:
    busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# --- CARROSSEL AUTOMÁTICO ---
# Lógica de tempo para 2026: Carrossel reseta a cada 3 segundos
if 'count' not in st.session_state:
    st.session_state.count = 0

placeholder_banner = st.empty()
atual = banners[st.session_state.count % len(banners)]

with placeholder_banner.container():
    st.markdown(f"""
        <div class="banner-box" style="background: {atual['cor']}">
            <h1 style="color:white !important;">{atual['titulo']}</h1>
            <p style="color:white !important; font-size:1.2rem;">{atual['sub']}</p>
        </div>
    """, unsafe_allow_html=True)

# Lógica de rotação (Em um app real, o usuário interage ou o script re-executa)
# Aqui usamos um botão discreto para simular a troca ou o refresh do Streamlit
if st.button("Próxima Novidade ❯"):
    st.session_state.count += 1
    st.rerun()

# --- VITRINE COM BUSCA ---
st.write("### Nossos Produtos")

# Filtragem funcional
produtos_filtrados = [p for p in produtos if busca.lower() in p['n'].lower() or busca.lower() in p['t'].lower()]

if not produtos_filtrados:
    st.warning("Nenhum produto encontrado com esse nome.")
else:
    cols = st.columns(4)
    for idx, p in enumerate(produtos_filtrados):
        with cols[idx % 4]:
            st.markdown(f"""
                <div style="border:1px solid #EEE; border-radius:15px; padding:15px; background:white; margin-bottom:10px;">
                    <div style="font-size:50px; text-align:center; background:#F9FAFB; border-radius:10px; padding:20px;">{p['i']}</div>
                    <p style="color:#7C3AED; font-weight:700; font-size:0.7rem; margin-top:10px;">{p['t']}</p>
                    <h4 style="margin:0; font-size:1rem;">{p['n']}</h4>
                    <h3 style="margin:10px 0; color:#111827;">R$ {p['p']:.2f}</h3>
                </div>
            """, unsafe_allow_html=True)
            st.button("ADICIONAR", key=f"v_{idx}")

# --- RODAPÉ ---
st.markdown("""
    <div class="footer-v2">
        <div class="footer-grid">
            <div class="footer-col">
                <h5>Canais Oficiais</h5>
                <a href="https://wa.me/55119XXXXXXXX">WhatsApp</a>
                <a href="https://instagram.com/encantolilie_">Instagram</a>
                <a href="https://tr.ee/ZtbOcerQhG">Loja Shopee</a>
            </div>
            <div class="footer-col">
                <h5>Atendimento</h5>
                <a href="https://tr.ee/5D7-CjgLk5">Catálogo Digital</a>
                <a href="#">Meus Pedidos</a>
                <a href="#">Suporte</a>
            </div>
            <div class="footer-col">
                <h5>Jurídico 2026</h5>
                <a href="#">Termos de Uso (LGPD 2.0)</a>
                <a href="#">Privacidade e Dados</a>
                <a href="#">Trocas e Devoluções</a>
            </div>
        </div>
        <div style="text-align:center; margin-top:40px; color:#9CA3AF; font-size:0.8rem;">
            © 2026 Encanto Liliê - Criatividade que encanta. <br>
            CNPJ 00.000.000/0001-00 | Osasco, São Paulo.
        </div>
    </div>
""", unsafe_allow_html=True)
