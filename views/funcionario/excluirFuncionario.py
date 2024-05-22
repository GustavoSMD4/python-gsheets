import streamlit as st
from main import update, consultaFuncionarios
import streamlit_shadcn_ui as ui

def deleteFuncionario():
    
    funcionarios = st.session_state['funcionarios']
    
    with st.form('formDeleteFuncionario'):
        st.header('Excluir Funcionário')
        cpf = st.text_input('CPF', autocomplete='off').rstrip()
        btnDelete = st.form_submit_button('Localizar funcionário')

    if btnDelete:
        cpf = cpf.replace('.', '').replace('-', '')
        funcionarios_localizados = funcionarios[funcionarios['cpf'] == cpf]
        
        if len(funcionarios_localizados) < 1:
            st.warning('Funcionário não localizado.')
        else:
            st.session_state['funcionario_para_excluir'] = funcionarios_localizados
            st.session_state['confirmacao_exclusao'] = False

    if 'funcionario_para_excluir' in st.session_state and not st.session_state['confirmacao_exclusao']:
        funcionarios_localizados = st.session_state['funcionario_para_excluir']
        ui.table(funcionarios_localizados)
        col1, col2, col3 = st.columns([2, 3, 5])
        btnConfirmar = col1.button(f"Excluir {funcionarios_localizados['nome'].iloc[0]}?")
        btnCancelar = col2.button('Cancelar')

        if btnConfirmar:
            st.session_state['confirmacao_exclusao'] = True

        if btnCancelar:
            st.session_state.pop('funcionario_para_excluir', None)
            st.session_state.pop('confirmacao_exclusao', None)
            st.warning('Operação cancelada.')

    if 'confirmacao_exclusao' in st.session_state and st.session_state['confirmacao_exclusao']:
        funcionarios_localizados = st.session_state['funcionario_para_excluir']
        update(worksheet='funcionario', data=funcionarios[funcionarios['cpf'] != cpf])
        consultaFuncionarios()
        st.success('Excluído com sucesso.')
        st.session_state.pop('funcionario_para_excluir', None)
        st.session_state.pop('confirmacao_exclusao', None)

