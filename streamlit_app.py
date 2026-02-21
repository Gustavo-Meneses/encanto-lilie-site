import streamlit as st
from streamlit_autorefresh import st_autorefresh

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | Vitrine 2026",
    page_icon="🌸",
    layout="wide",
)

# 2. Autorefresh para garantir o giro (3000ms = 3 segundos)
# O componente agora vai ouvir esse contador para mudar de slide
count = st_autorefresh(interval=3000, key="carouselframer")

# 3. Dados dos Banners e Produtos
banners = [
    {"titulo": "Kits Escolares 2026", "sub": "Organização e estilo para a volta às aulas.", "cor": "linear-gradient(135deg, #7C3AED 0%, #EC4899 100%)", "id": 0},
    {"titulo": "Canecas de Porcelana", "sub": "Personalize com sua foto favorita.", "cor": "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)", "id": 1},
    {"titulo": "Coleção Natalina", "sub": "Garanta seus presentes com antecedência.", "cor": "linear-gradient(135deg, #10B981 0%, #059669 100%)", "id": 2}
]

produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "t": "Aniversário", "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "t": "Presentes", "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "t": "Escolar", "i": "🎒"},
    {"n": "Agenda 2025", "p": 65.00, "t": "Papelaria", "i": "📅"}
]

# 4. Estilo CSS para as Setas e Layout Clean
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
        
        .stApp { background-color: #FFFFFF; }
        [data-testid="stHeader"] { visibility: hidden; }

        /* Estilização do Banner com Setas */
        .carousel-container {
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 40px;
        }
        
        .banner-box {
            width: 100%;
            padding: 60px 20px;
            border-radius: 24px;
            color: white !important;
            text-align: center;
            transition: background 0.5s ease-in-out;
        }

        .nav-arrow {
            position: absolute;
            background: rgba(255,255,255,0.2);
            border: none;
            color: white;
            padding: 15px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
            transition: 0.3s;
            z-index: 10;
        }
        .nav-arrow:hover { background: rgba(255,255,255,0.4); }
        .arrow-left { left: 20px; }
        .arrow-right { right: 20px; }

        /* Rodapé e Botões */
        div.stButton > button {
            background-color: #7C3AED !important;
            color: white !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            width: 100% !important;
            height: 45px !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- HEADER & BUSCA ---
col_logo, col_search = st.columns([1, 2])
with col_logo:
    st.markdown("<h2 style='margin: 0;'>Encanto Liliê</h2>", unsafe_allow_html=True)

with col_search:
    busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# --- CARROSSEL COM SETAS E GIRO AUTOMÁTICO ---
if 'banner_idx' not in st.session_state:
    st.session_state.banner_idx = 0

# Lógica de troca automática acionada pelo autorefresh
st.session_state.banner_idx = count % len(banners)
atual = banners[st.session_state.banner_idx]

# Layout do carrossel
c_prev, c_main, c_next = st.columns([0.1, 0.8, 0.1])

with c_prev:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    if st.button("❮", key="prev"):
        st.session_state.banner_idx = (st.session_state.banner_idx - 1) % len(banners)

with c_main:
    st.markdown(f"""
        <div class="banner-box" style="background: {atual['cor']}">
            <h1 style="color:white !important; margin:0; font-size: 2.5rem;">{atual['titulo']}</h1>
            <p style="color:white !important; opacity:0.9; font-size:1.2rem; margin-top:10px;">{atual['sub']}</p>
        </div>
    """, unsafe_allow_html=True)

with c_next:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    if st.button("❯", key="next"):
        st.session_state.banner_idx = (st.session_state.banner_idx + 1) % len(banners)

# --- VITRINE COM BUSCA ---
st.write("### Produtos em Destaque")
produtos_filtrados = [p for p in produtos if busca.lower() in p['n'].lower()]

if not produtos_filtrados:
    st.info("Nenhum item encontrado.")
else:
    cols = st.columns(4)
    for idx, p in enumerate(produtos_filtrados):
        with cols[idx % 4]:
            st.markdown(f"""
                <div style="border:1px solid #F1F1F1; border-radius:20px; padding:20px; background:white;">
                    <div style="font-size:55px; text-align:center; padding:25px; background:#FDFDFD; border-radius:15px;">{p['i']}</div>
                    <p style="color:#7C3AED; font-weight:800; font-size:0.7rem; text-transform:uppercase; margin-top:15px;">{p['t']}</p>
                    <h4 style="margin:5px 0; font-size:1rem; color:#111827;">{p['n']}</h4>
                    <h3 style="margin:10px 0; color:#111827;">R$ {p['p']:.2f}</h3>
                </div>
            """, unsafe_allow_html=True)
            st.button("ADICIONAR", key=f"p_{idx}")

# --- RODAPÉ INTEGRADO ---
st.markdown("""
    <div style="background-color: #F9FAFB; padding: 60px 20px; margin-top: 80px; border-top: 1px solid #EEE;">
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 40px; max-width: 1200px; margin: 0 auto;">
            <div>
                <h5 style="color:#111827; font-weight:800; margin-bottom:20px;">CANAIS OFICIAIS</h5>
                <a href="https://wa.me/55119XXXXXXXX" style="color:#6B7280; text-decoration:none; display:block; margin-bottom:10px;">💬 WhatsApp</a>
                <a href="https://instagram.com/encantolilie_" style="color:#6B7280; text-decoration:none; display:block; margin-bottom:10px;">📸 Instagram</a>
                <a href="https://tr.ee/ZtbOcerQhG" style="color:#6B7280; text-decoration:none; display:block; margin-bottom:10px;">🛍️ Loja Shopee</a>
            </div>
            <div>
                <h5 style="color:#111827; font-weight:800; margin-bottom:20px;">JURÍDICO 2026</h5>
                <a href="#" onclick="alert('Conforme LGPD 2026: Seus dados estão protegidos.')" style="color:#6B7280; text-decoration:none; display:block; margin-bottom:10px;">📄 Termos de Uso</a>
                <a href="#" onclick="alert('Privacidade: Usamos cookies apenas para melhorar sua experiência.')" style="color:#6B7280; text-decoration:none; display:block; margin-bottom:10px;">🔒 Privacidade</a>
            </div>
        </div>
        <div style="text-align:center; margin-top:40px; color:#9CA3AF; font-size:0.75rem;">
            © 2026 Encanto Liliê | Osasco, SP | CNPJ: 00.000.000/0001-00
        </div>
    </div>
""", unsafe_allow_html=True)
