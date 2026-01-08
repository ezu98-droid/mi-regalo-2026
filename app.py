import streamlit as st

st.set_page_config(page_title="Feliz 2026", page_icon="🎊")

# Efectos especiales de globos Y nieve
st.balloons()
st.snow()

st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
    }
    .main-card {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
        padding: 50px;
        border-radius: 30px;
        border: 2px solid #FFD700;
        text-align: center;
        box-shadow: 0 0 50px rgba(255, 215, 0, 0.2);
        margin-top: 50px;
    }
    .titulo {
        font-family: 'Georgia', serif;
        color: #FFD700;
        font-size: 70px !important;
        font-weight: bold;
        text-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
        margin-bottom: 10px;
    }
    .deseo {
        color: white;
        font-size: 24px;
        font-family: 'Arial', sans-serif;
        letter-spacing: 2px;
    }
    </style>
    
    <div class="main-card">
        <h1 class="titulo">🎊 2026 🎊</h1>
        <p class="deseo">¡QUE TODOS TUS SUEÑOS SE HAGAN REALIDAD!</p>
        <hr style="border-color: #FFD700;">
        <p style="color: #FFD700; font-size: 40px;">🥂✨🚀</p>
    </div>
    """, unsafe_allow_html=True)
