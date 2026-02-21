import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | 2026",
    page_icon="🌸",
    layout="wide"
)

# 2. Estado do Carrinho e Funções
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

def adicionar_ao_carrinho(nome, preco):
    st.session_state.carrinho.append({"nome": nome, "preco": preco})
    st.toast(f"✅ {nome} adicionado!", icon="🛒")
    st.rerun() # FORÇA A ATUALIZAÇÃO IMEDIATA DA LISTA

# 3. CSS PROFISSIONAL (Mobile Clean + Carrossel + Rodapé)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;600;800&display=swap');
        
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        /* Título Responsivo */
        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: clamp(3rem, 10vw, 4.5rem);
            margin-top: 20px;
            font-weight: 800;
        }

        /* CAMPOS DE TEXTO "CLEAN" (Branco com texto Preto) */
        input {
            background-color: #FFFFFF !important;
            color: #000000 !important;
            border: 1px solid #D1D5DB !important;
        }
        div[data-baseweb="input"] {
            background-color: #FFFFFF !important;
            border-radius: 10px !important;
        }

        /* CARROSSEL RESTAURADO */
        .slider {
            width: 100%; height: 200px; position: relative; overflow: hidden;
            border-radius: 20px; margin: 20px 0;
        }
        .slides { display: flex; width: 300%; height: 100%; animation: slide 12s infinite; }
        .slide { 
            width: 33.33%; display: flex; flex-direction: column; 
            justify-content: center; align-items: center; color: white; 
            text-align: center; padding: 20px;
        }
        @keyframes slide {
            0%, 30% { transform: translateX(0); }
            33%, 63% { transform: translateX(-33.33%); }
            66%, 96% { transform: translateX(-66.66%); }
            100% { transform: translateX(0); }
        }

        /* Cards de Produto */
        .card-produto {
            border: 1px solid #F3F4F6;
            border-radius: 20px;
            padding: 15px;
            text-align: center;
            background: #FFFFFF;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        }
        
        /* Botões */
        div.stButton > button {
            background-color: #7C3AED !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            width: 100% !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

# Busca
_, col_busca, _ = st.columns([1, 8, 1])
with col_busca:
    busca = st.text_input("Busca", placeholder="🔍 O que você procura hoje?", label_visibility="collapsed")

# --- CARRINHO ATUALIZÁVEL ---
with st.expander(f"🛒 MEU CARRINHO ({len(st.session_state.carrinho)} ITENS)", expanded=len(st.session_state.carrinho) > 0):
    if not st.session_state.carrinho:
        st.write("Seu carrinho está vazio.")
    else:
        total = sum(item['preco'] for item in st.session_state.carrinho)
        for i, item in enumerate(st.session_state.carrinho):
            st.markdown(f"**{item['nome']}** - R$ {item['preco']:.2f}")
        
        st.markdown(f"### Total: R$ {total:.2f}")
        
        # Inputs com visual Clean
        nome = st.text_input("Nome Completo", key="nome_c")
        tel = st.text_input("WhatsApp (com DDD)", key="tel_c")
        
        if st.button("FINALIZAR NO WHATSAPP"):
            if nome and tel:
                itens_txt = "%0A".join([f"- {i['nome']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
                msg = f"Olá! Pedido de: *{nome}*%0A%0A*ITENS:*%0A{itens_txt}%0A%0ATotal: R$ {total:.2f}"
                st.markdown(f' <a href="https://wa.me/5511977253425?text={msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:15px; border-radius:12px; text-align:center; font-weight:bold;">ENVIAR PEDIDO</div></a>', unsafe_allow_html=True)
            else:
                st.error("Preencha nome e WhatsApp.")
        
        if st.button("Esvaziar Carrinho"):
            st.session_state.carrinho = []
            st.rerun()

# --- CARROSSEL ---
st.markdown(f"""
    <div class="slider">
        <div class="slides">
            <div class="slide" style="background: linear-gradient(135deg, #7C3AED, #EC4899)"><h2>Kits Escolares 2026</h2><p>Tudo personalizado para volta às aulas</p></div>
            <div class="slide" style="background: linear-gradient(135deg, #3B82F6, #8B5CF6)"><h2>Canecas de Porcelana</h2><p>Sua foto favorita em uma caneca premium</p></div>
            <div class="slide" style="background: linear-gradient(135deg, #10B981, #059669)"><h2>Coleção Natalina</h2><p>Garanta presentes mágicos</p></div>
        </div>
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
cols = st.columns(2)
for idx, p in enumerate(prod_filtrados):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="card-produto">
                <div style="font-size:40px;">{p['i']}</div>
                <h4 style="color:#000;">{p['n']}</h4>
                <p style="font-weight:800; font-size:1.2rem; color:#000;">R$ {p['p']:.2f}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button("ADICIONAR", key=f"btn_{idx}"):
            adicionar_ao_carrinho(p['n'], p['p'])

# --- RODAPÉ FORMATADO ---
st.markdown("""
    <hr style="margin-top: 50px; border: 0.5px solid #EEE;">
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; padding: 20px; background-color: #F9FAFB; border-radius: 20px;">
        <div style="min-width: 150px;">
            <h5 style="color:#000; font-weight:800;">CONTATO</h5>
            <p><a href="https://wa.me/5511977253425" style="color:#7C3AED; text-decoration:none;">WhatsApp</a></p>
            <p><a href="https://instagram.com/encantolilie_" style="color:#7C3AED; text-decoration:none;">Instagram</a></p>
        </div>
        <div style="min-width: 150px;">
            <h5 style="color:#000; font-weight:800;">LEGAL</h5>
            <p style="color:#666; font-size:0.9rem;">Termos de Uso</p>
            <p style="color:#666; font-size:0.9rem;">Privacidade</p>
        </div>
    </div>
    <p style="text-align:center; color:#AAA; font-size:0.8rem; margin-top:20px;">© 2026 Encanto Liliê | Osasco, SP</p>
""", unsafe_allow_html=True)
