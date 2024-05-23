import streamlit as st

def home():
    
    usuarioLogado = st.session_state['usuarioLogado']
    
    st.header(F"Bem-vindo {usuarioLogado['nome']}")
    
    with st.container(border=True):
        st.subheader(F"O seu usuário é {usuarioLogado['role']}")