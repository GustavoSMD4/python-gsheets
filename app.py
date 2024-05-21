import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
from login import loginForm
from views.funcionario.mainFuncionarios import viewFuncionarios
from views.stats.salarios import statsSalarios
import main

st.set_page_config(layout='wide')

if 'logado' not in st.session_state:
    st.session_state.logado = False
    
if 'usuarios' not in st.session_state:
    main.login()
    
if 'logLogins' not in st.session_state:
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
    optionsMenu = ['Funcionários', 'Stats Funcionários']
    icons = ['person-vcard-fill', 'bar-chart-line-fill']
    
        
elif st.session_state.logado == True and usuarioLogado['role'] != 'admin':
    st.header('Você não tem permissão para acessar todas as abas')
    optionsMenu = ['Stats Funcionários']
    icons = ['bar-chart-line-fill']
    

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
            
    if menuSelecionado == 'Funcionários':
        viewFuncionarios()
                
    elif menuSelecionado == 'Stats Funcionários':
        main.consultaFuncionarios()
        statsSalarios()
    
