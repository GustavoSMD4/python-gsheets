import streamlit as st

def loginForm():
    
    usuarios = st.session_state['usuarios']
    
    with st.form('formLogin', clear_on_submit=True):
        st.header('Login')
        user = st.text_input('Usuário')
        senha = st.text_input("Senha", type="password")
        btnLogin = st.form_submit_button('Verificar')
        
    if btnLogin:
        if (usuarios['usuario'] == user).any() and (usuarios['senha'] == senha).any():
            st.success('Login sucesso')
            st.session_state.bolean = True
        else:
            st.warning('usuário/senha inválido')
            st.session_state.bolean = False
