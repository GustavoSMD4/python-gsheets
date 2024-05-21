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
        
        funcionariosUpdate = funcionarios
        funcionariosUpdate['Nome'] = funcionariosUpdate['nome'].str.upper()
        funcionariosUpdate = funcionariosUpdate[funcionariosUpdate['nome'] != nome.upper()]
        st.write(nome)
        ui.table(funcionariosUpdate)
    
        update(worksheet='funcionario', data=funcionariosUpdate)
        st.success('Excluido')