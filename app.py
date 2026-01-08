import streamlit as st

# Configuración de la pestaña con tu nuevo nombre
st.set_page_config(page_title="Mensaje Toro 2026", page_icon="🐂")

# Estilos y Tipografía Navideña
st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">
    
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .main-container {
        text-align: center;
        padding: 40px;
        border-radius: 25px;
        background: linear-gradient(135deg, #1a1a2e 0%, #000000 100%);
        border: 2px solid #FFD700;
        box-shadow: 0px 0px 30px rgba(255, 215, 0, 0.3);
    }
    .titulo-navideno {
        font-family: 'Great Vibes', cursive;
        color: #FFFFFF !important;
        font-size: 80px !important;
        text-shadow: 2px 2px 15px rgba(255, 255, 255, 0.5);
        margin-bottom: 20px;
        font-weight: 100;
    }
    .mensaje-exito {
        color: #FFD700;
        font-size: 28px;
        margin-top: 25px;
        font-family: 'Arial', sans-serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Animaciones
st.balloons()
st.snow()

# Contenido
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título Blanco
st.markdown('<h1 class="titulo-navideno">¡Feliz Año 2026!</h1>', unsafe_allow_html=True)

# Tu foto (mifoto.png)
st.image("mifoto.png", use_container_width=True)

# Tu frase
st.markdown('<p class="mensaje-exito">"Este año te deseo el mayor de los éxitos"</p>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
