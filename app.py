import streamlit as st
from login import loginForm
from teste import cadastroFuncionario
import main

if 'bolean' not in st.session_state:
    st.session_state.bolean = False

if st.session_state.bolean == False:
    logado = loginForm(main.login())
    if logado == True:
        st.session_state.bolean = True
        
btnLogar = st.button('Logar')

if st.session_state.bolean == True and btnLogar == True:
    cadastroFuncionario(funcionarios=main.funcionarios, update=main.update)
