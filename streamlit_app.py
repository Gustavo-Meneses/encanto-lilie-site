import streamlit as st

# 1. Configuração da Página (Deve ser a 1ª linha)
st.set_page_config(
    page_title="Encanto Liliê | 2026",
    page_icon="🌸",
    layout="wide"
)

# 2. CSS Customizado
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;600;800&display=swap');
        
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        [data-testid="stHeader"] { display: none; }

        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: clamp(3rem, 8vw, 4.5rem);
            margin-bottom: 0px;
            font-weight: 800;
        }

        /* Estilo das Abas */
        .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 10px; }
        .stTabs [data-baseweb="tab"] { font-weight: 600; color: #4B5563; border-radius: 10px; }
        
        /* Cards de Produto */
        .card-produto {
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            background: #FFFFFF;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            margin-bottom: 20px;
        }
        .img-fake {
            width: 100%; height: 180px; background-color: #F3F4F6;
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-size: 3rem; margin-bottom: 15px;
        }
        
        /* Botão WhatsApp */
        .btn-wpp {
            display: inline-block; width: 100%; background-color: #25D366; 
            color: white !important; text-align: center; padding: 12px; 
            border-radius: 10px; font-weight: bold; text-decoration: none;
        }

        /* Inputs Clean */
        div[data-baseweb="input"], div[data-baseweb="textarea"] {
            background-color: #FFFFFF !important;
            border: 1px solid #D1D5DB !important;
            color: #000 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Função para gerar o link do WhatsApp sem precisar de bibliotecas extras
def criar_link_wpp(produto, preco):
    texto = f"Olá! Vi no site e tenho interesse no item: {produto} (R$ {preco}). Pode me ajudar?"
    # Formatação básica de URL manual para evitar erros de import
    texto_url = texto.replace(" ", "%20").replace("!", "%21").replace(":", "%3A")
    return f"https://wa.me/5511953766456?text={texto_url}"

# --- TOPO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; margin-top:-10px;'>Criatividade que encanta, resultados que marcam.</p>", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
aba_home, aba_pf, aba_corp, aba_sazonal, aba_sobre, aba_contato = st.tabs([
    "🏠 Início", "🛍️ Produtos", "💼 Corporativo", "🎄 Sazonais", "📖 Sobre", "📞 Contato"
])

with aba_home:
    st.markdown("<h2 style='text-align:center; color:#000;'>Destaques da Semana</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background: linear-gradient(135deg, #7C3AED, #EC4899); border-radius: 20px; padding: 40px; text-align: center; color: white;">
            <h1>Transforme Ideias em Presentes</h1>
            <p>Personalizados feitos com amor e exclusividade.</p>
        </div>
    """, unsafe_allow_html=True)

with aba_pf:
    st.write("### Catálogo para Você")
    c1, c2, c3 = st.columns(3)
    
    produtos_pf = [
        {"n": "Caneca Cerâmica", "p": "35,00", "i": "☕", "d": "325ml. Alta qualidade e brilho."},
        {"n": "Buquê de Bombom", "p": "45,00", "i": "🍫", "d": "7 unidades com tag inclusa."},
        {"n": "Quadrinho MDF", "p": "15,00", "i": "🖼️", "d": "Tamanho 20x28cm. Arte pronta."}
    ]
    
    colunas = [c1, c2, c3]
    for i, p in enumerate(produtos_pf):
        with colunas[i]:
            st.markdown(f"""
                <div class="card-produto">
                    <div class="img-fake">{p['i']}</div>
                    <h4 style="color:#000;">{p['n']}</h4>
                    <p style="color:#666; font-size:0.9rem;">{p['d']}</p>
                    <h3 style="color:#000;">R$ {p['p']}</h3>
                    <a href="{criar_link_wpp(p['n'], p['p'])}" target="_blank" class="btn-wpp">Pedir no WhatsApp</a>
                </div>
            """, unsafe_allow_html=True)

with aba_corp:
    st.write("### Soluções para Empresas")
    st.info("Atendimento diferenciado e preços para atacado acima de 10 unidades.")
    cc1, cc2 = st.columns(2)
    with cc1:
        st.markdown(f"""
            <div class="card-produto">
                <div class="img-fake">🤝</div>
                <h4 style="color:#000;">Kits Onboarding</h4>
                <p style="color:#666;">Dê as boas-vindas com a cara da sua marca.</p>
                <a href="{criar_link_wpp('Kit Onboarding', 'Orçamento')}" target="_blank" class="btn-wpp">Solicitar Orçamento</a>
            </div>
        """, unsafe_allow_html=True)
    with cc2:
        st.markdown(f"""
            <div class="card-produto">
                <div class="img-fake">🏢</div>
                <h4 style="color:#000;">Brindes em Lote</h4>
                <p style="color:#666;">Canecas, agendas e mimos para eventos corporativos.</p>
                <a href="{criar_link_wpp('Brindes em Lote', 'Orçamento')}" target="_blank" class="btn-wpp">Falar com Consultor</a>
            </div>
        """, unsafe_allow_html=True)

with aba_sazonal:
    st.write("### Coleções de Época")
    st.warning("Novidades de Páscoa chegando em breve!")

with aba_sobre:
    st.write("### Nossa História")
    st.markdown("""
        A **Encanto Liliê** nasceu em Osasco para levar mais afeto ao dia a dia das pessoas. 
        O que começou como um hobby de sublimação, hoje é uma marca que atende famílias e empresas.
    """)

with aba_contato:
    st.write("### Entre em Contato")
    col_f, col_l = st.columns(2)
    with col_f:
        st.text_input("Seu Nome", key="ct_nome")
        st.text_area("Sua Mensagem", key="ct_msg")
        st.button("Enviar Mensagem")
    with col_l:
        st.markdown("**Redes Sociais**")
        st.write("📸 [Instagram @encantolilie_](https://instagram.com/encantolilie_)")
        st.write("💬 WhatsApp: (11) 95376-6456")
        st.write("📍 Osasco - SP")

# --- RODAPÉ ---
st.markdown("""
    <hr>
    <div style="text-align:center; padding: 20px; color:#888;">
        © 2026 Encanto Liliê | Criatividade que Encanta
    </div>
""", unsafe_allow_html=True)
