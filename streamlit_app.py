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

# 3. CSS para Mover Sidebar para a DIREITA
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;700;800&display=swap');
        
        /* Inverte o layout: Sidebar para a direita, Conteúdo para a esquerda */
        [data-testid="stSidebar"] {
            order: 2 !important;
        }
        section[data-testid="stMain"] {
            order: 1 !important;
        }
        .stApp {
            flex-direction: row !important;
        }

        /* Estilos Visuais */
        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: 4.5rem;
            margin-top: -40px;
        }
        
        div.stButton > button {
            background-color: #7C3AED !important;
            color: white !important;
            border-radius: 12px !important;
            font-weight: 700 !important;
            width: 100% !important;
        }

        /* Ajuste do Carrossel */
        .slider {
            width: 100%; height: 250px; position: relative; overflow: hidden;
            border-radius: 24px; margin: 30px 0;
        }
        .slides { display: flex; width: 300%; height: 100%; animation: slide 12s infinite; }
        .slide { width: 33.33%; display: flex; flex-direction: column; justify-content: center; align-items: center; color: white; text-align: center; padding: 20px; }
        @keyframes slide {
            0%, 30% { transform: translateX(0); }
            33%, 63% { transform: translateX(-33.33%); }
            66%, 96% { transform: translateX(-66.66%); }
            100% { transform: translateX(0); }
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
        
        # Coleta de Dados
        st.markdown("### Seus Dados")
        nome = st.text_input("Nome Completo")
        email = st.text_input("E-mail")
        fone = st.text_input("Telefone")
        
        if st.button("Finalizar no WhatsApp"):
            if nome and email and fone:
                itens_txt = "%0A".join([f"- {i['nome']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
                msg = (f"Olá! Novo pedido de: *{nome}*%0A"
                       f"E-mail: {email}%0A"
                       f"Tel: {fone}%0A%0A"
                       f"*ITENS:*%0A{itens_txt}%0A%0A"
                       f"*TOTAL: R$ {total:.2f}*")
                
                # Link com o seu número solicitado
                st.markdown(f' <a href="https://wa.me/5511977253425?text={msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:12px; border-radius:10px; text-align:center; font-weight:bold;">ENVIAR PEDIDO AGORA</div></a>', unsafe_allow_html=True)
            else:
                st.warning("Preencha seus dados para continuar.")

# --- CONTEÚDO PRINCIPAL ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

col_v1, col_busca, col_v2 = st.columns([1, 2, 1])
with col_busca:
    busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# Banners (Carrossel)
banners = [
    {"t": "Kits Escolares 2026", "c": "linear-gradient(135deg, #7C3AED, #EC4899)"},
    {"t": "Canecas Pet", "c": "linear-gradient(135deg, #3B82F6, #8B5CF6)"},
    {"t": "Natal 2025", "c": "linear-gradient(135deg, #10B981, #059669)"}
]

st.markdown(f"""
    <div class="slider">
        <div class="slides">
            {"".join([f'<div class="slide" style="background:{b["c"]}"><h1>{b["t"]}</h1></div>' for b in banners])}
        </div>
    </div>
""", unsafe_allow_html=True)

# Produtos
st.write("### Destaques")
produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "i": "🎒"},
    {"n": "Agenda 2026", "p": 65.00, "i": "📅"}
]

cols = st.columns(4)
for idx, p in enumerate(produtos):
    if busca.lower() in p['n'].lower():
        with cols[idx % 4]:
            st.markdown(f"""
                <div style="border:1px solid #EEE; border-radius:20px; padding:20px; text-align:center; margin-bottom:10px;">
                    <div style="font-size:40px;">{p['i']}</div>
                    <h4>{p['n']}</h4>
                    <p>R$ {p['p']:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("ADICIONAR", key=f"p_{idx}"):
                adicionar_ao_carrinho(p['n'], p['p'])
