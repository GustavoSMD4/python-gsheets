import streamlit as st
import pandas as pd
from datetime import date
from main import update

def loginForm():
    
    usuarios = st.session_state['usuarios']
    logs = st.session_state['logsLogin']
    
    with st.form('formLogin', clear_on_submit=True):
        st.header('Login')
        user = st.text_input('Usuário')
        senha = st.text_input("Senha", type="password")
        btnLogin = st.form_submit_button('Verificar')
        
    if btnLogin:
        if (usuarios['usuario'] == user).any() and (usuarios['senha'] == senha).any():
            usuarioLogado = usuarios[(usuarios['usuario'] == user) & (usuarios['senha'] == senha)].iloc[0]
            
            st.session_state['usuarioLogado'] = usuarioLogado
                
            st.success('Login sucesso')
            
            log = pd.DataFrame([
                {
                    
                    "user": usuarioLogado['usuario'],
                    "data": date.today()
                    
                }
            ])
            
            userUpdate = pd.concat([logs, log], ignore_index=True)
            update(userUpdate, worksheet='logLogins')
            
            st.session_state.logado = True
        else:
            st.warning('usuário/senha inválido')
            st.session_state.logado = False
