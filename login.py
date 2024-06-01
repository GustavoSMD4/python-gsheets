import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from streamlit_option_menu import option_menu
from datetime import date
from main import update, login, logsLogin
from validacoes import validarInputs

def loginForm() -> bool:
    """Se o login for realizado com sucesso retornará True"""
    
    usuarios: pd.DataFrame = st.session_state['usuarios']
    logs: pd.DataFrame = st.session_state['logsLogin']
    
    options=['Login', 'Criar Conta']
    
    with st.sidebar:
        
        tipo = option_menu(menu_title='Login',
                           options=options,
                           icons=['box-arrow-in-right', 'plus-square'])
    
    if tipo == 'Login':
        with st.form('formLogin'):
            st.header('Login')
            user = st.text_input('Usuário', autocomplete='off').rstrip()
            senha = st.text_input("Senha", type="password").rstrip()
            btnLogin = st.form_submit_button('Logar')
            
        
            if btnLogin == True:
                try:
                    validarInputs((user, senha), (str, str), ('Usuário', 'Senha'))
                
                    usuarioDigitadoExiste = usuarios.loc[usuarios['usuario'] == user]
                    if len(usuarioDigitadoExiste) < 1 or usuarioDigitadoExiste['senha'].iloc[0] != senha:
                        st.warning('Usuário ou senha inválidos')

                    else:
                        if (usuarios['usuario'] == user).any() and (usuarios['senha'] == senha).any():
                            usuarioLogado = usuarios[(usuarios['usuario'] == user) & (usuarios['senha'] == senha)].iloc[0]

                            st.session_state['usuarioLogado'] = usuarioLogado

                            st.success('Fazendo login.')

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
                        
                except ValueError as e:
                    st.warning(e)

    elif tipo == 'Criar Conta':

        with st.form('formCriarConta'):
            st.header('Criar Conta')
            nome = st.text_input('Nome', autocomplete='off').rstrip()
            user = st.text_input('Usuário', autocomplete='off').rstrip()
            senha = st.text_input("Senha", type="password").rstrip()
            btnCriar = st.form_submit_button('Criar conta')

            if btnCriar == True:
                try:
                    validarInputs([nome, user, senha], [str, str, str], ['Nome', 'Usuário', 'Senha'])

                    if (usuarios['usuario'] == user).any():
                        st.warning('Nome de usuário já existe.')

                    elif (usuarios['usuario'] != user).any():

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

                    
                except ValueError as e:
                    st.warning(e)
                
                
            
