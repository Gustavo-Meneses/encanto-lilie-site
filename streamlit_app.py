import streamlit as st
import urllib.parse

# 1. Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê | Criatividade que Encanta",
    page_icon="🌸",
    layout="wide"
)

# 2. CSS Customizado
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;600;800&display=swap');
        
        .stApp { background-color: #FFFFFF; font-family: 'Inter', sans-serif; }
        
        /* Título Principal */
        .loja-titulo {
            text-align: center;
            font-family: 'Dancing Script', cursive;
            color: #7C3AED;
            font-size: clamp(3rem, 8vw, 4.5rem);
            margin-top: 10px;
            font-weight: 800;
        }

        /* Estilização das Abas (Menu de Navegação) */
        .stTabs [data-baseweb="tab-list"] {
            justify-content: center;
            gap: 10px;
            flex-wrap: wrap;
        }
        .stTabs [data-baseweb="tab"] {
            font-weight: 600;
            font-size: 1.1rem;
            color: #4B5563;
        }
        .stTabs [aria-selected="true"] {
            color: #7C3AED !important;
        }

        /* Card de Produto */
        .card-produto {
            border: 1px solid #E5E7EB;
            border-radius: 16px;
            padding: 16px;
            text-align: center;
            background: #FFFFFF;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
        }
        .img-placeholder {
            width: 100%; height: 200px; background-color: #F3F4F6;
            border-radius: 12px; display: flex; align-items: center; justify-content: center;
            font-size: 3rem; margin-bottom: 15px;
        }
        .desc-produto { color: #4B5563; font-size: 0.9rem; margin-bottom: 15px; min-height: 40px; }
        
        /* Botão WhatsApp Direto */
        a.btn-wpp {
            display: block; width: 100%; background-color: #25D366; color: white !important;
            text-align: center; padding: 12px; border-radius: 8px; font-weight: bold;
            text-decoration: none; transition: 0.2s;
        }
        a.btn-wpp:hover { background-color: #1DA851; }
    </style>
""", unsafe_allow_html=True)

# 3. Função para renderizar os produtos padronizados
def exibir_produto(nome, descricao, preco, icone_temp="📦"):
    # Prepara a mensagem exata para o WhatsApp
    numero_wpp = "5511953766456"
    texto_msg = f"Olá, Encanto Liliê! Tenho interesse no produto: *{nome}* (R$ {preco}). Como podemos personalizar?"
    link_wpp = f"https://wa.me/{numero_wpp}?text={urllib.parse.quote(texto_msg)}"
    
    st.markdown(f"""
        <div class="card-produto">
            <div class="img-placeholder">{icone_temp}</div>
            <h4 style="color:#000; margin-bottom: 5px;">{nome}</h4>
            <p class="desc-produto">{descricao}</p>
            <h3 style="color:#000; margin-bottom: 15px;">R$ {preco}</h3>
            <a href="{link_wpp}" target="_blank" class="btn-wpp">Pedir no WhatsApp</a>
        </div>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown("<div class='loja-titulo'>Encanto Liliê</div>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#666; font-weight:600;'>Criatividade que encanta, resultados que marcam.</p>", unsafe_allow_html=True)
st.divider()

# --- NAVEGAÇÃO POR ABAS ---
aba_home, aba_pf, aba_corp, aba_sazonal, aba_sobre, aba_contato = st.tabs([
    "🏠 Início", 
    "🛍️ Produtos (PF)", 
    "💼 Corporativo", 
    "🎄 Sazonais", 
    "📖 Sobre a Marca", 
    "📞 Contato"
])

# --- CONTEÚDO: INÍCIO ---
with aba_home:
    st.markdown("<h2 style='text-align:center; color:#000;'>Bem-vindo ao Espaço Criativo</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#444;'>Transformamos suas ideias reais em peças úteis e afetivas.</p>", unsafe_allow_html=True)
    
    # Banner Destaque
    st.markdown("""
        <div style="background: linear-gradient(135deg, #7C3AED, #EC4899); border-radius: 20px; padding: 40px 20px; text-align: center; color: white; margin-top: 20px;">
            <h2>Personalização Feita com Afeto</h2>
            <p>De lembranças individuais a brindes corporativos marcantes.</p>
        </div>
    """, unsafe_allow_html=True)

# --- CONTEÚDO: PRODUTOS PF ---
with aba_pf:
    st.markdown("### Para Presentear e Encantar")
    st.write("Conheça nossos catálogos voltados para o cliente final.")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        exibir_produto("Caneca Personalizada", "325ml, cerâmica branca. Artes prontas ou do zero.", "35,00", "☕")
    with col2:
        exibir_produto("Buquê de Bombom", "7 bombons com tag personalizada. Pronto para presentear com afeto.", "45,00", "🍫")
    with
