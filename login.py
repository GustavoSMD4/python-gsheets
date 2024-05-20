import streamlit as st
import pandas as pd
from datetime import date
from main import update, login

def loginForm():
    
    usuarios = st.session_state['usuarios']
    logs = st.session_state['logsLogin']
    
    tipo = st.selectbox('Login/Criar Conta', options=['Login', 'Criar Conta'])
    
    if tipo == 'Login':
        with st.form('formLogin'):
            st.header('Login')
            user = st.text_input('Usuário')
            senha = st.text_input("Senha", type="password")
            btnLogin = st.form_submit_button('Verificar')

        if btnLogin == True:
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
                return True
            else:
                st.warning('usuário/senha inválido')
                st.session_state.logado = False
                return False

    if tipo == 'Criar Conta':

        with st.form('formCriarConta'):
            st.header('Criar Conta')
            user = st.text_input('Usuário')
            senha = st.text_input("Senha", type="password")
            btnCriar = st.form_submit_button('Verificar')

        if btnCriar == True:
            if user and senha and (usuarios['usuario'] != user).any():

                userCreate = pd.DataFrame([
                    {
                        'usuario': user,
                        'senha': senha,
                        'role': 'user'
                    }
                ])

                dfUpdate = pd.concat([usuarios, userCreate], ignore_index=True)

                update(data=dfUpdate, worksheet='login')
                st.success('Usuário cadastrado')
                login()

                st.session_state.criarConta = False

            elif not user and not senha:
                st.warning('Usuario ou senha não infomados ou usuário já existe.')

            elif (usuarios['usuario'] == user).any():
                st.warning('Nome de usuário já existe')
