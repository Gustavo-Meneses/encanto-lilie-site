import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | 2026",
    page_icon="🌸",
    layout="wide"
)

# 2. Estado do Carrinho
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar_ao_carrinho(nome, preco):
    st.session_state.carrinho.append({"nome": nome, "preco": preco})
    st.toast(f"✅ {nome} adicionado!", icon="🛒")

# 3. CSS Ajustado para Alto Contraste (Mobile Friendly)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;600;800&display=swap');
        
        /* Fundo e Fonte Base */
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        [data-testid="stHeader"] { display: none; }
        
        /* Título Principal - Roxo Vibrante e Legível */
        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: clamp(3rem, 10vw, 5rem);
            margin: 20px 0;
            font-weight: 800;
        }

        /* Cores de Fonte para Legibilidade Máxima */
        h1, h2, h3, h4, p, span, label {
            color: #000000 !important; /* Tudo em preto para máximo contraste */
        }
        
        .subtitulo-banner {
            color: #FFFFFF !important; /* Exceção para texto dentro do banner roxo */
            font-weight: 600;
        }

        /* Card de Produto */
        .card-produto {
            border: 2px solid #F3F4F6;
            border-radius: 20px;
            padding: 20px;
            text-align: center;
            margin-bottom: 15px;
            background: #FFFFFF;
        }
        
        .preco-produto {
            color: #111827 !important;
            font-size: 1.5rem;
            font-weight: 800;
            margin: 10px 0;
        }

        /* Banner */
        .banner-container {
            background: linear-gradient(135deg, #7C3AED, #EC4899);
            padding: 40px 20px;
            border-radius: 24px;
            text-align: center;
            margin: 20px 0;
        }
        .banner-container h2 { color: #FFFFFF !important; }

        /* Botões mais escuros para destaque */
        div.stButton > button {
            background-color: #7C3AED !important;
            color: #FFFFFF !important;
            border-radius: 12px !important;
            padding: 12px !important;
            font-weight: 700 !important;
            border: none !important;
            box-shadow: 0 4px 6px rgba(124, 58, 237, 0.3);
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

# Busca com bordas mais visíveis
_, col_busca, _ = st.columns([1, 8, 1])
with col_busca:
    busca = st.text_input("O que você procura?", placeholder="🔍 Digite aqui...", label_visibility="collapsed")

# --- CARRINHO (EXPANDER) ---
with st.expander(f"🛒 VER MEU CARRINHO ({len(st.session_state.carrinho)})"):
    if not st.session_state.carrinho:
        st.write("**Seu carrinho está vazio.**")
    else:
        total = sum(item['preco'] for item in st.session_state.carrinho)
        for item in st.session_state.carrinho:
            st.write(f"● **{item['nome']}** - R$ {item['preco']:.2f}")
        
        st.markdown(f"### Total: R$ {total:.2f}")
        
        # Dados do Cliente com labels em negrito
        st.markdown("**Preencha para enviar o pedido:**")
        nome = st.text_input("Seu Nome Completo")
        tel = st.text_input("Seu WhatsApp (com DDD)")
        
        if st.button("FINALIZAR PEDIDO NO WHATSAPP"):
            if nome and tel:
                itens_txt = "%0A".join([f"- {i['nome']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
                msg = f"Olá! Pedido de: *{nome}*%0A%0A*ITENS:*%0A{itens_txt}%0A%0ATotal: R$ {total:.2f}"
                st.markdown(f' <a href="https://wa.me/5511977253425?text={msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:15px; border-radius:12px; text-align:center; font-weight:bold; font-size:1.1rem;">CLIQUE AQUI PARA ENVIAR</div></a>', unsafe_allow_html=True)
            else:
                st.error("Por favor, preencha o nome e telefone.")

# --- BANNER DESTAQUE ---
st.markdown("""
    <div class="banner-container">
        <h2>Lançamentos 2026</h2>
        <p class="subtitulo-banner">Kits Escolares e Personalizados com Amor</p>
    </div>
""", unsafe_allow_html=True)

# --- VITRINE ---
produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "i": "🎒"},
    {"n": "Agenda 2026", "p": 65.00, "i": "📅"}
]

prod_filtrados = [p for p in produtos if busca.lower() in p['n'].lower()]

# Grid Responsivo
cols = st.columns(2) # 2 colunas no mobile fica excelente para leitura
for idx, p in enumerate(prod_filtrados):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="card-produto">
                <div style="font-size:50px; margin-bottom:10px;">{p['i']}</div>
                <h4 style="font-size:1.1rem; margin-bottom:5px;">{p['n']}</h4>
                <div class="preco-produto">R$ {p['p']:.2f}</div>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ADICIONAR", key=f"btn_{idx}"):
            adicionar_ao_carrinho(p['n'], p['p'])

# --- RODAPÉ ---
st.markdown("""
    <hr style="margin-top: 50px; border: 1px solid #000;">
    <div style="text-align: center; padding: 20px; background-color: #F9FAFB; border-radius: 20px;">
        <h4 style="margin-bottom:15px;">CONTATO DIRETO</h4>
        <p style="font-size:1.1rem;"><strong>Instagram:</strong> <a href="https://instagram.com/encantolilie_" style="color:#7C3AED;">@encantolilie_</a></p>
        <p style="font-size:1.1rem;"><strong>WhatsApp:</strong> <a href="https://wa.me/5511977253425" style="color:#7C3AED;">(11) 97725-3425</a></p>
        <br>
        <p style="font-size: 0.8rem; color: #555 !important;">© 2026 Encanto Liliê | Osasco, SP</p>
    </div>
    <div style="height: 50px;"></div>
""", unsafe_allow_html=True)
