import streamlit as st

def loginForm(fetchUsuarios):
    
    fetchUsuarios()
    usuarios = st.session_state['usuarios']
    
    with st.form('formLogin', clear_on_submit=True):
        user = st.text_input('Usuário')
        senha = st.text_input("Senha", type="password")
        btnLogin = st.form_submit_button('Verificar')
        
    if btnLogin:
        if (usuarios['usuario'] == user).any() and (usuarios['senha'] == senha).any():
            st.success('Login sucesso')
            return True
        else:
            st.warning('usuário/senha inválido')
            return False
