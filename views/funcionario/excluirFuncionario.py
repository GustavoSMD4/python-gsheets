import streamlit as st
import pandas as pd
from main import update
import streamlit_shadcn_ui as ui

def deleteFuncionario():
    with st.form('formDeleteFuncionario'):
        st.header('Excluir Funcionário')
        nome = st.text_input('Nome', autocomplete='off')

        btnDelete = st.form_submit_button('Deletar')

    if btnDelete == True:
        funcionarios = st.session_state['funcionarios']
        
        funcionariosUpdate = funcionarios
        funcionariosUpdate['Nome'] = funcionariosUpdate['Nome'].str.upper()
        funcionariosUpdate = funcionariosUpdate[funcionariosUpdate['Nome'] != nome.upper()]
        st.write(nome)
        ui.table(funcionariosUpdate)
    
        update(worksheet='teste',data=funcionariosUpdate)
        st.success('Excluido')