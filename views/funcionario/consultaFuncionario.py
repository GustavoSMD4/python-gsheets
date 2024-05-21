import streamlit as st
import streamlit_shadcn_ui as ui

def consulta():
    funcionarios = st.session_state['funcionarios']
    
    st.subheader('Consulta funcionários')
    
    funcionariosDisplay = funcionarios[0:]
    funcionariosDisplay['salario'] = funcionarios['salario'].apply(lambda x: F"R${x:,.2f}")
    
    ui.table(funcionariosDisplay)