import streamlit as st
import streamlit_shadcn_ui as ui

def consultaFuncionarios():
    funcionarios = st.session_state['funcionarios']
    
    ui.table(funcionarios[['Nome', 'Departamento', 'Cargo']])