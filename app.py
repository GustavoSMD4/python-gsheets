import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from streamlit_option_menu import option_menu
from login import loginForm
from views.funcionario.mainFuncionarios import viewFuncionarios
from views.stats.salarios import statsSalarios
import main

# st.set_page_config(layout='wide')

if 'logado' not in st.session_state:
    st.session_state.logado = False
    
if 'usuarios' not in st.session_state:
    main.login()
 
if 'btnLogar' not in st.session_state:
    st.session_state.btnLogar = False
    
if 'logsLogin' not in st.session_state:
    main.logsLogin()
    
if 'usuarioLogado' not in st.session_state:
    st.session_state['usuarioLogado'] = pd.DataFrame()
    
if st.session_state.logado == False:
    logged = loginForm()
    if logged == True:
        st.session_state.logado = True

btnLogar = ''
if st.session_state.logado == True:
    if st.session_state.btnLogar == False:
        btnLogar = st.button('Logar')
        if btnLogar == True:
            st.session_state.btnLogar = True


usuarioLogado = st.session_state['usuarioLogado']

optionsMenu = []
icons = []


if st.session_state.logado == True and st.session_state.btnLogar == True and usuarioLogado['role'] == 'admin':
    optionsMenu = ['Funcionários', 'Stats Funcionários']
    icons = ['person-vcard-fill', 'bar-chart-line-fill']
    
        
elif st.session_state.logado == True and st.session_state.btnLogar == True and usuarioLogado['role'] != 'admin':
    st.header('Você não tem permissão para acessar todas as abas')
    optionsMenu = ['Stats Funcionários']
    icons = ['bar-chart-line-fill']
    

if st.session_state.logado == True and st.session_state.btnLogar == True:
    with st.sidebar:
        menuSelecionado = option_menu(menu_title='Menu',
                                options=optionsMenu,
                                icons=icons,
                                menu_icon='house-door-fill', 
                                orientation='horizontal')
        
        logout = st.button('Logout')
        if logout:
            st.session_state['logado'] = False
            st.session_state['btnLogar'] = False
            main.login()
            
    if menuSelecionado == 'Funcionários':
        st.header('Funcionários')
        viewFuncionarios()
                
    elif menuSelecionado == 'Stats Funcionários':
        main.consultaFuncionarios()
        statsSalarios()
    