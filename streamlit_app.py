import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | Vitrine 2026",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed" # Inicia recolhido para não atrapalhar a visão
)

# 2. Inicialização do Carrinho no Session State
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

# Funções do Carrinho
def adicionar_ao_carrinho(nome, preco):
    st.session_state.carrinho.append({"nome": nome, "preco": preco})
    st.toast(f"✅ {nome} adicionado!", icon="🛒")

def limpar_carrinho():
    st.session_state.carrinho = []

# 3. Dados dos Banners e Produtos
banners = [
    {"titulo": "Kits Escolares 2026", "sub": "Organização e estilo para a volta às aulas.", "cor": "linear-gradient(135deg, #7C3AED 0%, #EC4899 100%)"},
    {"titulo": "Canecas de Porcelana", "sub": "Personalize com sua foto favorita.", "cor": "linear-gradient(135deg, #3B82F6 0%, #8B5CF6 100%)"},
    {"titulo": "Coleção Natalina", "sub": "Garanta seus presentes com antecedência.", "cor": "linear-gradient(135deg, #10B981 0%, #059669 100%)"}
]

produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "t": "Aniversário", "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "t": "Presentes", "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "t": "Escolar", "i": "🎒"},
    {"n": "Agenda 2026", "p": 65.00, "t": "Papelaria", "i": "📅"}
]

# 4. CSS Customizado
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;700;800&display=swap');
        
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        /* Ajuste para o Sidebar ficar na DIREITA */
        [data-testid="stSidebar"] {
            left: auto !important;
            right: 0 !important;
            width: 350px !important;
        }
        [data-testid="stSidebarNav"] { display: none; }
        
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
            0% { transform: translateX(0); }
            30% { transform: translateX(0); }
            33% { transform: translateX(-33.33%); }
            63% { transform: translateX(-33.33%); }
            66% { transform: translateX(-66.66%); }
            96% { transform: translateX(-66.66%); }
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

# --- CARRINHO NO CANTO DIREITO (SIDEBAR) ---
with st.sidebar:
    st.markdown("## 🛒 Meu Pedido")
    st.info("O carrinho agora fica aqui na direita! Você pode recolher na seta acima.")
    
    if not st.session_state.carrinho:
        st.write("Seu carrinho está vazio.")
    else:
        total = 0
        for i, item in enumerate(st.session_state.carrinho):
            st.markdown(f"**{item['nome']}** - R$ {item['preco']:.2f}")
            total += item['preco']
        
        st.divider()
        st.markdown(f"### Total: R$ {total:.2f}")
        
        # Formulário de Informações do Cliente
        st.markdown("### Seus Dados")
        nome_cliente = st.text_input("Nome Completo")
        email_cliente = st.text_input("E-mail")
        tel_cliente = st.text_input("Telefone de Contato")
        
        if st.button("Finalizar e Enviar WhatsApp"):
            if nome_cliente and email_cliente and tel_cliente:
                itens_lista = "%0A".join([f"- {i['nome']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
                
                # Montando a mensagem para URL
                texto_whatsapp = (
                    f"Olá! Novo pedido de: *{nome_cliente}*%0A"
                    f"E-mail: {email_cliente}%0A"
                    f"Telefone: {tel_cliente}%0A%0A"
                    f"*ITENS:*%0A{itens_lista}%0A%0A"
                    f"*TOTAL: R$ {total:.2f}*"
                )
                
                # Link com o seu número para teste
                link_wa = f"https://wa.me/5511977253425?text={texto_whatsapp}"
                
                st.markdown(f'<a href="{link_wa}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:10px; border-radius:10px; text-align:center; font-weight:bold;">ABRIR WHATSAPP AGORA</div></a>', unsafe_allow_html=True)
            else:
                st.error("Por favor, preencha todos os campos para finalizar.")
        
        if st.button("Limpar Tudo"):
            limpar_carrinho()
            st.rerun()

# --- CABEÇALHO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

col_vazia1, col_busca, col_vazia2 = st.columns([1, 2, 1])
with col_busca:
    busca = st.text_input("", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# --- CARROSSEL ---
_, c_body, _ = st.columns([0.1, 0.8, 0.1])
with c_body:
    st.markdown(f"""
        <div class="slider">
            <div class="slides">
                <div class="slide" style="background: {banners[0]['cor']}"><h1>{banners[0]['titulo']}</h1><p>{banners[0]['sub']}</p></div>
                <div class="slide" style="background: {banners[1]['cor']}"><h1>{banners[1]['titulo']}</h1><p>{banners[1]['sub']}</p></div>
                <div class="slide" style="background: {banners[2]['cor']}"><h1>{banners[2]['titulo']}</h1><p>{banners[2]['sub']}</p></div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# --- VITRINE ---
st.write("### Produtos em Destaque")
produtos_filtrados = [p for p in produtos if busca.lower() in p['n'].lower()]

if not produtos_filtrados:
    st.info("Nenhum item encontrado.")
else:
    cols = st.columns(4)
    for idx, p in enumerate(produtos_filtrados):
        with cols[idx % 4]:
            st.markdown(f"""
                <div style="border:1px solid #EEE; border-radius:20px; padding:20px; text-align:center;">
                    <div style="font-size:50px; margin-bottom:10px;">{p['i']}</div>
                    <p style="color:#7C3AED; font-weight:700; font-size:0.8rem; margin:0;">{p['t']}</p>
                    <h4 style="margin:5px 0;">{p['n']}</h4>
                    <h3 style="margin:10px 0;">R$ {p['p']:.2f}</h3>
                </div>
            """, unsafe_allow_html=True)
            if st.button("ADICIONAR", key=f"btn_{idx}"):
                adicionar_ao_carrinho(p['n'], p['p'])
