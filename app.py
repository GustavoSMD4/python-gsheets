import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from login import loginForm
from home import home
from views.funcionario.mainFuncionarios import viewFuncionarios
from views.usuarios.mainUsuarios import viewUsuarios
from views.conta.mainContas import viewContas
from views.caixa.mainCaixa import viewCaixa
from views.recebimento.mainRecebimento import viewRecebimentos
import main

# st.set_page_config(layout='wide')

st.markdown(
        """
            <style>
                .appview-container .main .block-container {{
                    padding-top: {padding_top}rem;
                    padding-bottom: {padding_bottom}rem;
                    }}

            </style>""".format(
            padding_top=3, padding_bottom=1
        ),
        unsafe_allow_html=True,
    )

if 'logado' not in st.session_state:
    st.session_state.logado = False
    
if 'usuarios' not in st.session_state:
    main.login()
    
if 'logsLogin' not in st.session_state:
    main.logsLogin()
    
if 'usuarioLogado' not in st.session_state:
    st.session_state['usuarioLogado'] = pd.DataFrame()
    
if st.session_state.logado == False:
    logged = loginForm()
    if logged == True:
        st.session_state.logado = True
        st.rerun()

usuarioLogado = st.session_state['usuarioLogado']

optionsMenu = []
icons = []

if st.session_state.logado == True and usuarioLogado['role'] == 'admin':
    optionsMenu = ['Home', 'Gestão de Usuários', 'Funcionários', 'Caixa', 'Contas a Pagar', 'Recebimento']
    icons = ['house-door-fill', 'person-fill-gear', 'person-vcard-fill', 'card-heading', 'credit-card-2-back-fill']
    
elif st.session_state.logado == True and usuarioLogado['role'] == 'financeiro':
    optionsMenu = ['Home', 'Caixa', 'Contas a Pagar', 'Recebimento']
    icons = ['house-door-fill', 'card-heading', 'credit-card-2-back-fill']
        
elif st.session_state.logado == True and usuarioLogado['role'] == 'user':
    optionsMenu = ['Home']
    icons = ['house-door-fill']
    

if st.session_state.logado == True:
    with st.sidebar:
        menuSelecionado = option_menu(menu_title=F"Olá, {usuarioLogado['nome']}",
                                options=optionsMenu,
                                icons=icons,
                                menu_icon='house-door-fill',)
        
        logout = st.button('Logout')
        if logout:
            st.session_state.logado = False
            st.rerun()
            
    if menuSelecionado == 'Home':
        home()
        
    if menuSelecionado == 'Gestão de Usuários':
        viewUsuarios()
    
    elif menuSelecionado == 'Funcionários':
        viewFuncionarios()
        
    elif menuSelecionado == 'Caixa':
        viewCaixa()
        
    elif menuSelecionado == 'Contas a Pagar':
        viewContas()
        
    elif menuSelecionado == 'Recebimento':
        viewRecebimentos()
