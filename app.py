import streamlit as st

# Configuración de la pestaña
st.set_page_config(page_title="Feliz 2026", page_icon="🎊")

# Lanzar globos automáticamente
st.balloons()

# Diseño del Cartel
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .card {
        background: linear-gradient(135deg, #ff4b2b 0%, #ff416c 100%);
        padding: 60px;
        border-radius: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }
    </style>
    <div class="card">
        <h1 style="color: white; font-size: 80px; margin: 0;">🎊 ¡FELIZ AÑO! 🎊</h1>
        <h2 style="color: white; font-size: 30px; opacity: 0.9;">Que el 2026 sea tu mejor año</h2>
    </div>
    """, unsafe_allow_html=True)
