import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Encanto Liliê - Personalizados",
    page_icon="✨",
    layout="wide",
)

# --- ESTILO CSS PERSONALIZADO (Vibe Coding) ---
st.markdown("""
    <style>
    /* Cores e Fontes */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600&family=Nunito:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Nunito', sans-serif;
        background-color: #FAF5FF;
    }

    h1, h2, h3 {
        font-family: 'Fredoka', sans-serif;
        color: #7C3AED; /* Roxo principal */
    }

    /* Botão de WhatsApp flutuante ou destaque */
    .stButton>button {
        background-color: #EC4899; /* Rosa */
        color: white;
        border-radius: 25px;
        border: none;
        padding: 10px 25px;
        font-weight: bold;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #DB2777;
        transform: scale(1.05);
        color: white;
    }

    /* Cards de Produtos */
    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(124, 58, 237, 0.1);
        text-align: center;
        margin-bottom: 20px;
    }

    /* Banner Principal */
    .hero {
        background: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%);
        padding: 60px;
        border-radius: 30px;
        color: white;
        text-align: center;
        margin-bottom: 40px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO / HERO ---
st.markdown("""
    <div class="hero">
        <h1>Encanto Liliê ✨</h1>
        <p style='font-size: 1.2rem;'>Criatividade que encanta, resultados que marcam 🎯</p>
    </div>
    """, unsafe_allow_html=True)

# --- CATEGORIAS (ESTILO INSTAGRAM) ---
st.write("### 📂 Explore por categoria")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🎄 Natal 2025"):
        st.toast("Carregando itens de Natal...")
with col2:
    if st.button("☕ Canecas"):
        st.toast("Carregando Canecas...")
with col3:
    if st.button("🎂 Aniversários"):
        st.toast("Carregando Kits Festa...")
with col4:
    if st.button("📚 Escolar"):
        st.toast("Carregando Kits Escolares...")

st.divider()

# --- MOSTRUÁRIO DE PRODUTOS ---
st.write("### 🛍️ Nossos Destaques")

# Simulando dados de produtos (Você pode substituir pelos links das suas fotos)
produtos = [
    {
        "nome": "Kit Marmitinha Bolofofos",
        "desc": "Personalizada com nome e idade. Perfeita para lembrancinhas!",
        "img": "https://placehold.co/400x400/8B5CF6/white?text=Kit+Marmitinha", # Placeholder
        "link": "https://wa.me/seunumeroaqui"
    },
    {
        "nome": "Kit Escolar Hulk",
        "desc": "Toalhinha e etiquetas resistentes à água para o maternal.",
        "img": "https://placehold.co/400x400/22C55E/white?text=Kit+Escolar", # Placeholder
        "link": "https://wa.me/seunumeroaqui"
    },
    {
        "nome": "Caneca Amor em 4 Patas",
        "desc": "Personalize com a foto do seu pet favorito.",
        "img": "https://placehold.co/400x400/EC4899/white?text=Caneca+Pet", # Placeholder
        "link": "https://wa.me/seunumeroaqui"
    }
]

# Grid de Produtos
cols = st.columns(3)
for i, p in enumerate(produtos):
    with cols[i % 3]:
        st.markdown(f"""
            <div class="product-card">
                <img src="{p['img']}" style="width:100%; border-radius:15px; margin-bottom:15px;">
                <h4>{p['nome']}</h4>
                <p style="font-size: 0.9rem; color: #666;">{p['desc']}</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Pedir no WhatsApp", key=f"btn_{i}"):
            st.write(f"Direcionando para o WhatsApp do item: {p['nome']}...")

# --- RODAPÉ ---
st.divider()
st.markdown("""
    <div style='text-align: center; color: #7C3AED; padding: 20px;'>
        <p>🚚 <b>Enviamos para todo o Brasil</b></p>
        <p>📍 Osasco, São Paulo | @encantolilie_</p>
    </div>
    """, unsafe_allow_html=True)
