import streamlit as st

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | 2026",
    page_icon="🌸",
    layout="wide"
)

# 2. CSS PROFISSIONAL (Mobile Clean + Carrossel + Rodapé)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;600;800&display=swap');
        
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        [data-testid="stHeader"] { display: none; }

        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: clamp(3rem, 10vw, 4.5rem);
            margin-bottom: 0px;
            font-weight: 800;
        }

        /* Estilo das Abas */
        .stTabs [data-baseweb="tab-list"] { justify-content: center; gap: 10px; }
        .stTabs [data-baseweb="tab"] { font-weight: 600; color: #4B5563; }

        /* CARROSSEL ANIMADO */
        .slider {
            width: 100%; height: clamp(180px, 30vh, 250px); 
            position: relative; overflow: hidden;
            border-radius: 20px; margin: 20px 0;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        }
        .slides { display: flex; width: 300%; height: 100%; animation: slide 12s infinite; }
        .slide { 
            width: 33.33%; display: flex; flex-direction: column; 
            justify-content: center; align-items: center; color: white; 
            text-align: center; padding: 20px;
        }
        @keyframes slide {
            0%, 25% { transform: translateX(0); }
            33%, 58% { transform: translateX(-33.33%); }
            66%, 91% { transform: translateX(-66.66%); }
            100% { transform: translateX(0); }
        }

        /* Cards de Produto */
        .card-produto {
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 20px;
            text-align: center;
            background: #FFFFFF;
            margin-bottom: 20px;
        }
        .img-fake {
            width: 100%; height: 150px; background-color: #F3F4F6;
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
        div[data-baseweb="input"] input, div[data-baseweb="textarea"] textarea {
            color: #000 !important;
            background-color: #FFF !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. Função de Link WhatsApp
def link_wpp(prod, preco):
    msg = f"Olá! Gostaria de encomendar: {prod} (R$ {preco})".replace(" ", "%20")
    return f"https://wa.me/5511953766456?text={msg}"

# --- CABEÇALHO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; margin-top:-10px;'>Criatividade que encanta, resultados que marcam.</p>", unsafe_allow_html=True)

# --- NAVEGAÇÃO ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Início", "🛍️ Produtos", "💼 Corporativo", "🎄 Sazonais", "📖 Sobre", "📞 Contato"
])

# --- ABA 1: INÍCIO (COM CARROSSEL) ---
with tab1:
    st.markdown(f"""
        <div class="slider">
            <div class="slides">
                <div class="slide" style="background: linear-gradient(135deg, #7C3AED, #EC4899)">
                    <h1>Kits Escolares 2026</h1>
                    <p>Organização com o herói favorito do seu filho!</p>
                </div>
                <div class="slide" style="background: linear-gradient(135deg, #3B82F6, #8B5CF6)">
                    <h1>Canecas Premium</h1>
                    <p>Sua foto favorita com qualidade fotográfica.</p>
                </div>
                <div class="slide" style="background: linear-gradient(135deg, #10B981, #059669)">
                    <h1>Brindes Corporativos</h1>
                    <p>Sua marca na mão de quem importa.</p>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ✨ Destaques de Hoje")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="card-produto"><div class="img-fake">☕</div><h4>Caneca Branca</h4><p>R$ 35,00</p><a href="{link_wpp("Caneca Branca", "35,00")}" class="btn-wpp">Pedir Agora</a></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="card-produto"><div class="img-fake">🍫</div><h4>Buquê Bombom</h4><p>R$ 45,00</p><a href="{link_wpp("Buquê Bombom", "45,00")}" class="btn-wpp">Pedir Agora</a></div>', unsafe_allow_html=True)

# --- ABA 2: PRODUTOS (PF) ---
with tab2:
    st.write("### Catálogo Completo")
    col1, col2, col3 = st.columns(3)
    # Lista baseada no catálogo fornecido
    prods = [
        {"n": "Quadrinho MDF", "p": "15,00", "i": "🖼️"},
        {"n": "Caneca Criativa", "p": "27,00", "i": "🖍️"},
        {"n": "Polaroids 7x9", "p": "Consulte", "i": "📸"}
    ]
    for i, p in enumerate(prods):
        with [col1, col2, col3][i]:
            st.markdown(f'<div class="card-produto"><div class="img-fake">{p["i"]}</div><h4>{p["n"]}</h4><p>R$ {p["p"]}</p><a href="{link_wpp(p["n"], p["p"])}" class="btn-wpp">Ver Detalhes</a></div>', unsafe_allow_html=True)

# --- ABA 3: CORPORATIVO ---
with tab3:
    st.write("### Para sua Empresa")
    st.markdown("""
        <div style="padding:20px; border-left: 5px solid #7C3AED; background: #F9FAFB; margin-bottom:20px;">
            <h4 style="color:#000;">Atendimento B2B</h4>
            <p style="color:#444;">Desenvolvemos artes exclusivas com sua logomarca para eventos e brindes de fim de ano.</p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown(f'<a href="{link_wpp("Orçamento Corporativo", "Sob Consulta")}" class="btn-wpp" style="background-color:#7C3AED;">SOLICITAR ORÇAMENTO EMPRESARIAL</a>', unsafe_allow_html=True)

# --- ABA 4: SAZONAIS ---
with tab4:
    st.info("🕒 **Em Breve:** Coleção Especial de Páscoa e Dia das Mães!")
    st.markdown(f'<div class="card-produto"><div class="img-fake">🎒</div><h4>Kit Escolar 2026</h4><p>A partir de R$ 45,00</p><a href="{link_wpp("Kit Escolar", "45,00")}" class="btn-wpp">Garantir Kit</a></div>', unsafe_allow_html=True)

# --- ABA 5: SOBRE ---
with tab5:
    st.write("### Criatividade que Encanta")
    st.write("A Encanto Liliê transforma ideias em peças úteis e afetivas. Localizada em Osasco, SP, somos especialistas em sublimação e presentes personalizados.")

# --- ABA 6: CONTATO ---
with tab6:
    st.write("### Fale com a gente")
    nome = st.text_input("Nome")
    msg = st.text_area("Como podemos te ajudar?")
    if st.button("Enviar"):
        st.success("Obrigado! Retornaremos em breve.")
    
    st.divider()
    st.markdown("""
        **Nossos Canais:** 📸 [Instagram @encantolilie_](https://instagram.com/encantolilie_)  
        💬 WhatsApp: (11) 95376-6456
    """)

# --- RODAPÉ ---
st.markdown("""
    <hr style="margin-top: 50px; border: 0.5px solid #EEE;">
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; padding: 30px; background-color: #F9FAFB; border-radius: 24px;">
        <div>
            <h5 style="color:#000; font-weight:800;">ENCANTO LILIÊ</h5>
            <p style="color:#666; font-size:0.9rem;">(11) 95376-6456</p>
            <p style="color:#666; font-size:0.9rem;">Osasco, SP</p>
        </div>
        <div>
            <h5 style="color:#000; font-weight:800;">LINKS</h5>
            <p><a href="https://instagram.com/encantolilie_" style="color:#7C3AED; text-decoration:none;">Instagram</a></p>
            <p><a href="#" style="color:#7C3AED; text-decoration:none;">Shopee</a></p>
        </div>
    </div>
    <p style="text-align:center; color:#AAA; font-size:0.8rem; margin-top:20px;">© 2026 Encanto Liliê</p>
""", unsafe_allow_html=True)
