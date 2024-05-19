import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from login import loginForm
from cadastroFuncionario import cadastroFuncionario
from consultaFuncionario import consultaFuncionarios
from excluirFuncionario import deleteFuncionario
import main

st.set_page_config(layout='wide')

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

if st.session_state.logado == True and st.session_state.btnLogar == True and usuarioLogado['role'] == 'admin':
    
    if 'funcionarios' not in st.session_state:
        main.funcionarios()

    tab = st.sidebar.radio('Teste', options=['Funcionário','teste2'])
    
    st.header(F"{tab}")
    
    if tab == 'Funcionário':
        tipoView = ui.tabs(options=['Consulta', 'Cadastro', 'Excluir'], default_value='Consulta')
        if tipoView == 'Cadastro':
            cadastroFuncionario()
        elif tipoView == 'Consulta':
            main.funcionarios()
            consultaFuncionarios()
        elif tipoView == 'Excluir':
            deleteFuncionario()
elif st.session_state.logado == True and st.session_state.btnLogar == True and usuarioLogado['role'] != 'admin':
    st.header('Você não tem permissão para acessar')