import streamlit as st
from main import update
import streamlit_shadcn_ui as ui

def deleteFuncionario():
    with st.form('formDeleteFuncionario'):
        st.header('Excluir Funcionário')
        nome = st.text_input('Nome', autocomplete='off')

        btnDelete = st.form_submit_button('Deletar')

    if btnDelete == True:
        funcionarios = st.session_state['funcionarios']
        
        funcionarios['Nome'] = funcionarios['nome'].str.upper()
        funcionarios = funcionarios[funcionarios['nome'] != nome.upper()]
        st.write(nome)
        ui.table(funcionarios)
    
        update(worksheet='funcionario', data=funcionarios)
        st.success('Excluido')