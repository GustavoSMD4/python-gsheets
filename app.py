import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from login import loginForm
from views.funcionario.mainFuncionarios import viewFuncionarios
from views.usuarios.mainUsuarios import viewUsuarios
import main

st.set_page_config(layout='wide')

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
    optionsMenu = ['Home', 'Usuários', 'Funcionários']
    icons = ['house-door-fill', 'person-fill', 'person-vcard-fill', 'bar-chart-line-fill']
        
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
        st.header('Home')
        
    if menuSelecionado == 'Usuários':
        viewUsuarios()
    
    elif menuSelecionado == 'Funcionários':
        viewFuncionarios()
        
    
