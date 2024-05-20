import streamlit as st
import pandas as pd
from datetime import date
from main import update, login

def loginForm():
    
    usuarios = st.session_state['usuarios']
    logs = st.session_state['logLogins']
    
    tipo = st.selectbox('Login/Criar Conta', options=['Login', 'Criar Conta'])
    
    if tipo == 'Login':
        with st.form('formLogin'):
            st.header('Login')
            user = st.text_input('Usuário')
            senha = st.text_input("Senha", type="password")
            btnLogin = st.form_submit_button('Verificar')
            
        
            if btnLogin == True:
                if not user or not senha:
                    st.warning('Usuário ou senha inválidos.')
                else:
                    usuarioDigitadoExiste = usuarios.loc[usuarios['usuario'] == user]
                    if len(usuarioDigitadoExiste) > 1 and usuarioDigitadoExiste['senha'].iloc[0] != senha:
                        st.warning('Usuário ou senha inválidos')

                    else:
                        if (usuarios['usuario'] == user).any() and (usuarios['senha'] == senha).any():
                            usuarioLogado = usuarios[(usuarios['usuario'] == user) & (usuarios['senha'] == senha)].iloc[0]

                            st.session_state['usuarioLogado'] = usuarioLogado

                            st.success('Usuário e senha localizados, clique em logar para continuar.')

                            log = pd.DataFrame([
                            {
                                "user": usuarioLogado['usuario'],
                                "data": date.today()
                            }
                        ])

                            if len(logs[logs['user'] == user]) < 1:
                                userUpdate = pd.concat([logs, log], ignore_index=True)
                                update(userUpdate, worksheet='logLogins')

                            st.session_state.logado = True
                            return True
                        else:
                            st.warning('usuário/senha inválido')
                            st.session_state.logado = False
                            return False

    elif tipo == 'Criar Conta':

        with st.form('formCriarConta'):
            st.header('Criar Conta')
            user = st.text_input('Usuário')
            senha = st.text_input("Senha", type="password")
            btnCriar = st.form_submit_button('Verificar')

        if btnCriar == True:
            if not user or not senha:
                st.warning('Usuario ou senha não infomados.')

            elif (usuarios['usuario'] == user).any():
                st.warning('Nome de usuário já existe.')
                
            elif user and senha and (usuarios['usuario'] != user).any():

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

            
