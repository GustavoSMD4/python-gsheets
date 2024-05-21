import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from streamlit_option_menu import option_menu
from datetime import date
from main import update, login, logsLogin

def loginForm():
    
    usuarios = st.session_state['usuarios']
    logs = st.session_state['logsLogin']
    
    options=['Login', 'Criar Conta']
    tipo = option_menu(menu_title='Login/Criar Conta',
                       options=options,
                       icons=['box-arrow-in-right', 'plus-square'],
                       orientation='horizontal')
    
    if tipo == 'Login':
        with st.form('formLogin'):
            st.header('Login')
            user = st.text_input('Usuário', autocomplete='off')
            senha = st.text_input("Senha", type="password")
            btnLogin = st.form_submit_button('Verificar')
            
        
            if btnLogin == True:
                if not user or not senha:
                    st.warning('Usuário ou senha inválidos.')
                else:
                    usuarioDigitadoExiste = usuarios.loc[usuarios['usuario'] == user]
                    if len(usuarioDigitadoExiste) < 1 or usuarioDigitadoExiste['senha'].iloc[0] != senha:
                        st.warning('Usuário ou senha inválidos')

                    else:
                        if (usuarios['usuario'] == user).any() and (usuarios['senha'] == senha).any():
                            usuarioLogado = usuarios[(usuarios['usuario'] == user) & (usuarios['senha'] == senha)].iloc[0]

                            st.session_state['usuarioLogado'] = usuarioLogado

                            st.success('Usuário e senha localizados, clique em logar para continuar.')

                            log = pd.DataFrame([
                            {
                                "usuario": usuarioLogado['usuario'],
                                "data": date.today()
                            }
                        ])

                            if len(logs[logs['usuario'] == user]) < 1:
                                userUpdate = pd.concat([logs, log], ignore_index=True)
                                update(worksheet='logsLogin', data=userUpdate)
                                logsLogin()

                            return True
                        else:
                            st.warning('usuário/senha inválido')
                            return False

    elif tipo == 'Criar Conta':

        with st.form('formCriarConta'):
            st.header('Criar Conta')
            nome = st.text_input('Nome', autocomplete='off')
            user = st.text_input('Nome usuário', autocomplete='off')
            senha = st.text_input("Senha", type="password")
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
                        'role': 'user'
                    }
                ])

                dfUpdate = pd.concat([usuarios, userCreate], ignore_index=True)

                update(data=dfUpdate, worksheet='usuario')
                st.success('Usuário cadastrado')
                login()

            
