import streamlit as st
import pandas as pd
from main import update, login

def create():
    
    usuarios = st.session_state['usuarios']
    
    with st.form('formCriarConta'):
        st.header('Criar Conta')
        col1, col2 = st.columns(2)
        col3, col4 = st.columns([2, 1])
        
        user = col1.text_input('Nome de usuário', autocomplete='off').rstrip()
        nome = col2.text_input('Nome', autocomplete='off').rstrip()
        senha = col3.text_input("Senha", type="password").rstrip()
        role = col4.selectbox('Role', options=['admin', 'financeiro', 'user'])
        btnCriar = st.form_submit_button('Criar conta')
        
        if btnCriar == True:
            if not user or not senha or not nome:
                st.warning('Usuario ou senha não infomados.')

            elif (usuarios['usuario'] == user).any():
                st.warning('Nome de usuário já existe.')
                
            elif user and senha and nome and (usuarios['usuario'] != user).any():

                userCreate = pd.DataFrame([
                    {
                        'usuario': user,
                        'nome': nome,
                        'senha': senha,
                        'role': role
                    }
                ])

                dfUpdate = pd.concat([usuarios, userCreate], ignore_index=True)

                update(data=dfUpdate, worksheet='usuario')
                st.success('Usuário cadastrado')
                usuarios = dfUpdate
                login()