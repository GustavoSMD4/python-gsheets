import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from login import loginForm
from cadastroFuncionario import cadastroFuncionario
from consultaFuncionario import consultaFuncionarios
from excluirFuncionario import deleteFuncionario
import main

st.set_page_config(layout='wide')

if 'bolean' not in st.session_state:
    st.session_state.bolean = False
    
if 'usuarios' not in st.session_state:
    main.login()
    
if 'funcionarios' not in st.session_state:
    main.funcionarios()
    
if 'btnLogar' not in st.session_state:
    st.session_state.btnLogar = False

if st.session_state.bolean == False:
    logado = loginForm()
    if logado == True:
        st.session_state.bolean = True

btnLogar = ''
if st.session_state.bolean == True:
    if st.session_state.btnLogar == False:
        btnLogar = st.button('Logar')
        if btnLogar == True:
            st.session_state.btnLogar = True

if st.session_state.bolean == True and st.session_state.btnLogar == True:
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