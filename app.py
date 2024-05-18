import streamlit as st
import pandas as pd
from login import loginForm
from teste import cadastroFuncionario
import main

if 'bolean' not in st.session_state:
    st.session_state.bolean = False
    
if 'usuarios' not in st.session_state:
    st.session_state['usuarios'] = pd.DataFrame()
    
if 'funcionarios' not in st.session_state:
    st.session_state['funcionarios'] = pd.DataFrame()

if st.session_state.bolean == False:
    logado = loginForm(fetchUsuarios=main.login)
    if logado == True:
        st.session_state.bolean = True

btnLogar = st.button('Logar')

st.write(st.session_state.bolean)

if st.session_state.bolean == True and btnLogar == True:
    cadastroFuncionario(funcionarios=main.funcionarios)
