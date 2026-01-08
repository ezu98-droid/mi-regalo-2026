import streamlit as st

# Configuración de página
st.set_page_config(page_title="Feliz 2026", page_icon="🥂")

# Importar una fuente elegante de Google Fonts para el toque navideño
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
        color: #FFFFFF !important; /* Blanco Puro */
        font-size: 85px !important;
        text-shadow: 2px 2px 15px rgba(255, 255, 255, 0.5);
        margin-bottom: 10px;
        font-weight: 100;
    }
    .cita {
        color: #FFD700;
        font-style: italic;
        font-size: 22px;
        margin-top: 25px;
        font-family: 'Arial', sans-serif;
    }
    .nombre {
        color: #FFFFFF;
        font-weight: bold;
        font-size: 18px;
        letter-spacing: 3px;
    }
    </style>
    """, unsafe_allow_html=True)

# Animaciones
st.balloons()
st.snow()

# Contenido
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# Título en blanco y cursivo
st.markdown('<h1 class="titulo-navideno">¡Feliz Año 2026!</h1>', unsafe_allow_html=True)

# Imagen de DiCaprio (El Gran Gatsby)
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8Iv5lqKwKsZ2g/giphy.gif", use_container_width=True)

st.markdown("""
    <p class="cita">"El único límite es tu mente. ¡A triunfar este año!"</p>
    <p class="nombre">- LEONARDO DICAPRIO -</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
