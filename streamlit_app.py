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

# 3. CSS Responsivo (Foco em Mobile)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;700&display=swap');
        
        /* Reset para Mobile */
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        [data-testid="stHeader"] { display: none; }
        
        /* Título Adaptável */
        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: clamp(2.5rem, 8vw, 4.5rem);
            margin: 10px 0;
        }

        /* Container de Produtos Responsivo */
        .card-produto {
            border: 1px solid #EEE;
            border-radius: 20px;
            padding: 15px;
            text-align: center;
            margin-bottom: 20px;
            background: white;
            box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        }

        /* Banner Mobile Friendly */
        .banner-container {
            background: linear-gradient(135deg, #7C3AED, #EC4899);
            color: white;
            padding: 30px 20px;
            border-radius: 20px;
            text-align: center;
            margin: 20px 0;
        }

        /* Ajuste para botões não sumirem no mobile */
        div.stButton > button {
            width: 100% !important;
            border-radius: 12px !important;
            padding: 10px !important;
            font-weight: 700 !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

# Centralizar busca em qualquer tela
_, col_busca, _ = st.columns([1, 6, 1])
with col_busca:
    busca = st.text_input("", placeholder="🔍 O que você procura?", label_visibility="collapsed")

# --- CARRINHO (EXPANDER NO TOPO PARA MOBILE) ---
with st.expander(f"🛒 Meu Carrinho ({len(st.session_state.carrinho)} itens)"):
    if not st.session_state.carrinho:
        st.write("Seu carrinho está vazio.")
    else:
        total = sum(item['preco'] for item in st.session_state.carrinho)
        for i, item in enumerate(st.session_state.carrinho):
            st.write(f"**{item['nome']}** - R$ {item['preco']:.2f}")
        
        st.divider()
        st.subheader(f"Total: R$ {total:.2f}")
        
        # Dados do Cliente
        nome = st.text_input("Seu Nome")
        tel = st.text_input("Seu WhatsApp")
        
        if st.button("Finalizar no WhatsApp", key="finalizar"):
            if nome and tel:
                itens_txt = "%0A".join([f"- {i['nome']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
                msg = f"Olá! Pedido de: *{nome}*%0A%0A*ITENS:*%0A{itens_txt}%0A%0ATotal: R$ {total:.2f}"
                link = f"https://wa.me/5511977253425?text={msg}"
                st.markdown(f' <a href="{link}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:12px; border-radius:10px; text-align:center; font-weight:bold;">ENVIAR AGORA</div></a>', unsafe_allow_html=True)
            else:
                st.error("Preencha nome e telefone.")
        
        if st.button("Esvaziar Carrinho"):
            st.session_state.carrinho = []
            st.rerun()

# --- CONTEÚDO ---
st.markdown("""
    <div class="banner-container">
        <h2>Kits Escolares 2026</h2>
        <p>Personalização que encanta!</p>
    </div>
""", unsafe_allow_html=True)

# Vitrine Responsiva (Garante que no mobile os cards fiquem um abaixo do outro)
produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "i": "🍱"},
    {"n": "Caneca Pet", "p": 39.90, "i": "☕"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "i": "🎒"},
    {"n": "Agenda 2026", "p": 65.00, "i": "📅"}
]

# Filtragem
prod_filtrados = [p for p in produtos if busca.lower() in p['n'].lower()]

# Grid que se adapta: 4 colunas no PC, 1 ou 2 no Celular
cols = st.columns([1, 1, 1, 1] if len(prod_filtrados) >= 4 else len(prod_filtrados))
for idx, p in enumerate(prod_filtrados):
    with cols[idx % (4 if len(prod_filtrados) >= 4 else len(prod_filtrados))]:
        st.markdown(f"""
            <div class="card-produto">
                <div style="font-size:40px;">{p['i']}</div>
                <h4>{p['n']}</h4>
                <p>R$ {p['p']:.2f}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ADICIONAR", key=f"btn_{idx}"):
            adicionar_ao_carrinho(p['n'], p['p'])

# --- RODAPÉ (RESTAURADO E FIXO) ---
st.markdown("""
    <hr style="margin-top: 50px;">
    <div style="text-align: center; padding-bottom: 40px;">
        <h5 style="color: #7C3AED;">CONTATO</h5>
        <p>📸 <a href="https://instagram.com/encantolilie_" style="color:#666; text-decoration:none;">@encantolilie_</a></p>
        <p>💬 <a href="https://wa.me/5511977253425" style="color:#666; text-decoration:none;">(11) 97725-3425</a></p>
        <p style="font-size: 0.8rem; color: #AAA; margin-top: 20px;">© 2026 Encanto Liliê | Osasco, SP</p>
    </div>
""", unsafe_allow_html=True)
