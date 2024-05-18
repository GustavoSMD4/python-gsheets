import streamlit as st

def consultaFuncionarios():
    funcionarios = st.session_state['funcionarios']
    
    st.table(funcionarios)