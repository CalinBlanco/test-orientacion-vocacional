import streamlit as st
from PIL import Image

def run():
    im = Image.open("assets/spellcheck.ico")
    st.set_page_config(
        page_title="Test Orientación. Vocacional",
        page_icon=im,
        # layout="wide",
        # layout="centered",
        initial_sidebar_state="expanded",
    )
    with open('style/style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
