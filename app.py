import streamlit as st

# Configuración de página
st.set_page_config(page_title="Feliz 2026", page_icon="🥂")

# Globos al entrar
st.balloons()

# Estilos personalizados
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .main-container {
        text-align: center;
        padding: 30px;
        border-radius: 20px;
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        border: 2px solid #FFD700;
    }
    .titulo {
        color: #FFD700;
        font-family: 'Arial Black', sans-serif;
        font-size: 50px !important;
        margin-bottom: 20px;
    }
    .cita {
        color: white;
        font-style: italic;
        font-size: 20px;
        margin-top: 20px;
    }
    .nombre {
        color: #FFD700;
        font-weight: bold;
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# Contenido
st.markdown('<div class="main-container">', unsafe_allow_html=True)

st.markdown('<h1 class="titulo">¡FELIZ AÑO 2026!</h1>', unsafe_allow_html=True)

# Imagen de DiCaprio (El Gran Gatsby)
st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueGZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8Iv5lqKwKsZ2g/giphy.gif", use_container_width=True)

st.markdown("""
    <p class="cita">"El único límite es tu mente. ¡A triunfar este año!"</p>
    <p class="nombre">- LEONARDO DICAPRIO</p>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Un toque de nieve para que sea más lindo
st.snow()
