import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | Vitrine 2026",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Inicialização do Carrinho
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar_ao_carrinho(nome, preco):
    st.session_state.carrinho.append({"nome": nome, "preco": preco})
    st.toast(f"✅ {nome} adicionado!", icon="🛒")

def limpar_carrinho():
    st.session_state.carrinho = []

# 3. CSS para Layout (Sidebar na Direita + Estilização)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;700;800&display=swap');
        
        /* Mover Sidebar para a Direita */
        [data-testid="stSidebar"] { order: 2 !important; }
        section[data-testid="stMain"] { order: 1 !important; }
        .stApp { flex-direction: row !important; }

        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        [data-testid="stHeader"] { visibility: hidden; }

        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: 4.5rem;
            margin-bottom: 5px;
            margin-top: -40px;
        }

        /* Carrossel */
        .slider {
            width: 100%; height: 250px; position: relative; overflow: hidden;
            border-radius: 24px; margin-top: 30px; margin-bottom: 40px;
        }
        .slides { display: flex; width: 300%; height: 100%; animation: slide 12s infinite; }
        .slide { width: 33.33%; display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; text-align: center; padding: 20px; }
        @keyframes slide {
            0%, 30% { transform: translateX(0); }
            33%, 63% { transform: translateX(-33.33%); }
            66%, 96% { transform: translateX(-66.66%); }
            100% { transform: translateX(0); }
        }

        /* Botões */
        div.stButton > button {
            background-color: #7C3AED !important; color: white !important;
            border-radius: 12px !important; border: none !important;
            font-weight: 700 !important; width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CARRINHO NA DIREITA (SIDEBAR) ---
with st.sidebar:
    st.markdown("## 🛒 Meu Pedido")
    
    if not st.session_state.carrinho:
        st.write("Seu carrinho está vazio.")
    else:
        total = 0
        for item in st.session_state.carrinho:
            st.markdown(f"**{item['nome']}** - R$ {item['preco']:.2f}")
            total += item['preco']
        
        st.divider()
        st.markdown(f"### Total: R$ {total:.2f}")
        
        st.markdown("### Seus Dados")
        nome_c = st.text_input("Nome Completo")
        email_c = st.text_input("E-mail")
        tel_c = st.text_input("WhatsApp")
        
        if st.button("Finalizar Pedido"):
            if nome_c and email_c and tel_c:
                itens_txt = "%0A".join([f"- {i['nome']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
                msg = (f"Olá! Novo pedido de: *{nome_c}*%0A"
                       f"E-mail: {email_c}%0A"
                       f"Tel: {tel_c}%0A%0A"
                       f"*ITENS:*%0A{itens_txt}%0A%0A"
                       f"*TOTAL: R$ {total:.2f}*")
                
                # Link para o seu número 11 97725-3425
                st.markdown(f'<a href="https://wa.me/5511977253425?text={msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:12px; border-radius:10px; text-align:center; font-weight:bold;">ENVIAR PARA WHATSAPP</div></a>', unsafe_allow_html=True)
            else:
                st.warning("Preencha os campos para finalizar.")
        
        if st.button("Limpar Carrinho"):
            limpar_carrinho()
            st.rerun()

# --- CONTEÚDO PRINCIPAL ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

col_v1, col_busca, col_v2 = st.columns([1, 2, 1])
with col_busca:
    busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# Banner Carrossel
banners = [
    {"t": "Kits Escolares 2026", "s": "Organização e estilo.", "c": "linear-gradient(135deg, #7C3AED, #EC4899)"},
    {"t": "Canecas de Porcelana", "s": "Personalização premium.", "c": "linear-gradient(135deg, #3B82F6, #8B5CF6)"},
    {"t": "Coleção Natalina", "s": "Presentes mágicos.", "c": "linear-gradient(135deg, #10B981, #059669)"}
]

st.markdown(f"""
    <div class="slider">
        <div class="slides">
            <div class="slide" style="background: {banners[0]['c']}"><h1>{banners[0]['t']}</h1><p>{banners[0]['s']}</p></div>
            <div class="slide" style="background: {banners[1]['c']}"><h1>{banners[1]['t']}</h1><p>{banners[1]['s']}</p></div>
            <div class="slide" style="background: {banners[2]['c']}"><h1>{banners[2]['t']}</h1><p>{banners[2]['s']}</p></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Vitrine de Produtos
st.write("### Produtos em Destaque")
produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "t": "Aniversário", "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "t": "Presentes", "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "t": "Escolar", "i": "🎒"},
    {"n": "Agenda 2026", "p": 65.00, "t": "Papelaria", "i": "📅"}
]

produtos_filtrados = [p for p in produtos if busca.lower() in p['n'].lower()]
cols = st.columns(4)
for idx, p in enumerate(produtos_filtrados):
    with cols[idx % 4]:
        st.markdown(f"""
            <div style="border:1px solid #EEE; border-radius:20px; padding:20px; text-align:center; margin-bottom:10px;">
                <div style="font-size:50px; margin-bottom:10px;">{p['i']}</div>
                <p style="color:#7C3AED; font-weight:700; font-size:0.8rem; margin:0;">{p['t']}</p>
                <h4 style="margin:5px 0;">{p['n']}</h4>
                <h3 style="margin:10px 0;">R$ {p['p']:.2f}</h3>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ADICIONAR", key=f"btn_{idx}"):
            adicionar_ao_carrinho(p['n'], p['p'])

# --- RODAPÉ RESTAURADO ---
st.markdown("""
    <hr style="margin-top: 60px; border-color: #EEE;">
    <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 80px; padding: 20px 0;">
        <div style="display: flex; flex-direction: column; align-items: flex-start;">
            <h5 style="margin-bottom:15px; color:#111827; font-weight:800;">CONTATO</h5>
            <a href="https://wa.me/5511977253425" target="_blank" style="text-decoration:none; color:#666; margin-bottom:8px; font-size:0.95rem;">💬 WhatsApp</a>
            <a href="https://instagram.com/encantolilie_" target="_blank" style="text-decoration:none; color:#666; margin-bottom:8px; font-size:0.95rem;">📸 Instagram</a>
            <a href="https://shopee.com.br" target="_blank" style="text-decoration:none; color:#666; margin-bottom:8px; font-size:0.95rem;">🛍️ Shopee</a>
        </div>
        <div style="display: flex; flex-direction: column; align-items: flex-start;">
            <h5 style="margin-bottom:15px; color:#111827; font-weight:800;">LEGAL</h5>
            <a href="#" style="text-decoration:none; color:#666; margin-bottom:8px; font-size:0.95rem;">📄 Termos de Uso (LGPD 2026)</a>
            <a href="#" style="text-decoration:none; color:#666; margin-bottom:8px; font-size:0.95rem;">🔒 Privacidade e Dados</a>
        </div>
    </div>
    <div style="text-align:center; padding:20px; color:#AAA; font-size:0.8rem;">
        © 2026 Encanto Liliê | Osasco, SP | CNPJ: 00.000.000/0001-00
    </div>
""", unsafe_allow_html=True)
