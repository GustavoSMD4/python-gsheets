import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from login import loginForm
from home import home
from views.funcionario.mainFuncionarios import viewFuncionarios
from views.usuarios.mainUsuarios import viewUsuarios
from views.conta.mainContas import viewContas
import main

# st.set_page_config(layout='wide')

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
    optionsMenu = ['Home', 'Gestão de usuários', 'Funcionários', 'Contas']
    icons = ['house-door-fill', 'person-fill-gear', 'person-vcard-fill', 'credit-card-2-back-fill']
        
elif st.session_state.logado == True and usuarioLogado['role'] != 'admin':
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
        
    if menuSelecionado == 'Gestão de usuários':
        viewUsuarios()
    
    elif menuSelecionado == 'Funcionários':
        viewFuncionarios()
        
    elif menuSelecionado == 'Contas':
        viewContas()
        
    
