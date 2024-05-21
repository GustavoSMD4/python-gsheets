import streamlit as st
import streamlit_shadcn_ui as ui

def consulta():
    
    usuarios = st.session_state['usuarios']
    
    ui.table(usuarios[['nome','usuario', 'role']])