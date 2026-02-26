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
    st.rerun()

def remover_do_carrinho(index):
    item_removido = st.session_state.carrinho.pop(index)
    st.toast(f"❌ {item_removido['nome']} removido.", icon="🗑️")
    st.rerun()

# 3. CSS Customizado
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;600;800&display=swap');
        
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: clamp(3rem, 10vw, 4.5rem);
            margin-top: 20px;
            font-weight: 800;
        }

        /* CARROSSEL AJUSTADO */
        .slider {
            width: 100%; height: 220px; position: relative; overflow: hidden;
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

        /* ABAS */
        .stTabs [data-baseweb="tab-list"] { gap: 10px; justify-content: center; }
        .stTabs [data-baseweb="tab"] {
            background-color: #F3F4F6 !important;
            border-radius: 10px !important;
            padding: 8px 16px !important;
        }
        .stTabs [aria-selected="true"] {
            background-color: #7C3AED !important;
            color: white !important;
        }

        div.stButton > button {
            background-color: #7C3AED !important;
            color: #FFFFFF !important;
            font-weight: 700 !important;
            border-radius: 12px !important;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)

_, col_busca, _ = st.columns([1, 8, 1])
with col_busca:
    busca = st.text_input("Busca", placeholder="🔍 O que você está procurando hoje?", label_visibility="collapsed")

# --- CARRINHO ---
with st.expander(f"🛒 MEU CARRINHO ({len(st.session_state.carrinho)})", expanded=len(st.session_state.carrinho) > 0):
    if not st.session_state.carrinho:
        st.markdown("<p style='color:black;'>Seu carrinho está vazio.</p>", unsafe_allow_html=True)
    else:
        total = sum(item['preco'] for item in st.session_state.carrinho)
        for idx, item in enumerate(st.session_state.carrinho):
            col_item, col_btn = st.columns([4, 1])
            with col_item:
                st.markdown(f"<p style='color:black; margin-top:10px;'>● <b>{item['nome']}</b> - R$ {item['preco']:.2f}</p>", unsafe_allow_html=True)
            with col_btn:
                if st.button("🗑️", key=f"cart_del_{idx}"):
                    remover_do_carrinho(idx)
        
        st.markdown(f"<h3 style='color:black;'>Total: R$ {total:.2f}</h3>", unsafe_allow_html=True)
        nome = st.text_input("Seu Nome Completo", key="nome_cli")
        tel = st.text_input("Seu WhatsApp (com DDD)", key="tel_cli")
        
        c1, c2 = st.columns(2)
        with c1:
            if st.button("FINALIZAR PEDIDO", key="checkout_main"):
                if nome and tel:
                    itens_txt = "%0A".join([f"- {i['nome']} (R$ {i['preco']:.2f})" for i in st.session_state.carrinho])
                    msg = f"Olá! Novo pedido de: *{nome}*%0A%0A*ITENS:*%0A{itens_txt}%0A%0ATotal: R$ {total:.2f}"
                    st.markdown(f' <a href="https://wa.me/5511977253425?text={msg}" target="_blank" style="text-decoration:none;"><div style="background-color:#25D366; color:white; padding:15px; border-radius:12px; text-align:center; font-weight:bold;">ABRIR WHATSAPP</div></a>', unsafe_allow_html=True)
        with c2:
            if st.button("Limpar Carrinho", key="clear_all"):
                st.session_state.carrinho = []
                st.rerun()

# --- CARROSSEL ---
st.markdown(f"""
    <div class="slider">
        <div class="slides">
            <div class="slide" style="background: linear-gradient(135deg, #7C3AED, #EC4899)"><h2>Kits Escolares 2026</h2><p>Organização e estilo para a volta às aulas</p></div>
            <div class="slide" style="background: linear-gradient(135deg, #3B82F6, #8B5CF6)"><h2>Canecas Pet</h2><p>Personalização premium para seu melhor amigo</p></div>
            <div class="slide" style="background: linear-gradient(135deg, #10B981, #059669)"><h2>Agendas 2026</h2><p>Planeje seu ano com muito encanto</p></div>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- PRODUTOS E ABAS ---
produtos = [
    {"n": "Kit Marmitinha", "p": 45.90, "i": "🍱", "c": "Escolar"},
    {"n": "Kit Escolar Hulk", "p": 89.00, "i": "🎒", "c": "Escolar"},
    {"n": "Caneca Pet", "p": 39.90, "i": "☕", "c": "Canecas"},
    {"n": "Caneca Floral", "p": 35.00, "i": "🌸", "c": "Canecas"},
    {"n": "Agenda 2026", "p": 65.00, "i": "📅", "c": "Agendas"},
    {"n": "Planner Mensal", "p": 42.00, "i": "🗒️", "c": "Agendas"}
]

def exibir_vitrine(lista, aba_id):
    filtrados = [p for p in lista if busca.lower() in p['n'].lower()]
    if not filtrados:
        st.info("Nenhum item encontrado.")
        return
    cols = st.columns(2)
    for idx, p in enumerate(filtrados):
        with cols[idx % 2]:
            st.markdown(f"""
                <div style="border: 1px solid #EEE; border-radius: 20px; padding: 15px; text-align: center; margin-bottom: 10px;">
                    <div style="font-size:40px;">{p['i']}</div>
                    <h4 style="color:black; margin:5px 0;">{p['n']}</h4>
                    <p style="font-weight:800; font-size:1.1rem; color:black;">R$ {p['p']:.2f}</p>
                </div>
            """, unsafe_allow_html=True)
            if st.button("ADICIONAR", key=f"add_{aba_id}_{idx}"):
                adicionar_ao_carrinho(p['n'], p['p'])

t1, t2, t3, t4 = st.tabs(["✨ Todos", "🎒 Escolar", "☕ Canecas", "📅 Agendas"])
with t1: exibir_vitrine(produtos, "all")
with t2: exibir_vitrine([p for p in produtos if p['c'] == "Escolar"], "esc")
with t3: exibir_vitrine([p for p in produtos if p['c'] == "Canecas"], "can")
with t4: exibir_vitrine([p for p in produtos if p['c'] == "Agendas"], "age")

# --- RODAPÉ PREMIUM RESTAURADO ---
st.markdown("""
    <hr style="margin-top: 50px; border: 0.5px solid #EEE;">
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; padding: 30px 10px; background-color: #F9FAFB; border-radius: 24px; gap: 30px;">
        <div style="min-width: 200px; text-align: left;">
            <h4 style="color:#000; font-weight:800; margin-bottom:20px;">CONTATO</h4>
            <p style="margin-bottom:10px;"><a href="https://wa.me/5511977253425" style="color:#7C3AED; text-decoration:none; font-weight:600;">💬 WhatsApp</a></p>
            <p style="margin-bottom:10px;"><a href="https://instagram.com/encantolilie_" style="color:#7C3AED; text-decoration:none; font-weight:600;">📸 Instagram</a></p>
        </div>
        <div style="min-width: 200px; text-align: left;">
            <h4 style="color:#000; font-weight:800; margin-bottom:20px;">LEGAL</h4>
            <p style="margin-bottom:10px; color:#444;">📄 Termos de Uso (LGPD 2026)</p>
            <p style="margin-bottom:10px; color:#444;">🔒 Privacidade</p>
        </div>
    </div>
    <div style="text-align:center; padding:20px; color:#888; font-size:0.85rem;">
        © 2026 Encanto Liliê | Osasco, SP | CNPJ: 00.000.000/0001-00
    </div>
""", unsafe_allow_html=True)
