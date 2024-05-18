import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def cadastroFuncionario(funcionarios):
    
    funcionarios()
    listaFuncionarios = st.session_state['funcionarios']

    st.title('Teste')

    st.divider()

    with st.form('formCadastroFuncionario', clear_on_submit=True):

        st.title('Cadastro funcionário')
        nome = st.text_input('Nome')

        col1, col2 = st.columns(2)

        idade = col1.text_input('idade')
        dataAdmissao = col2.date_input('data admissão', format="DD/MM/YYYY")

        col3, col4, col5 = st.columns(3)

        departamento = col3.selectbox('Departamento', options=listaFuncionarios['Departamento'].unique())
        cargo = col4.selectbox('cargo', options=listaFuncionarios['Cargo'].unique())
        salario = col5.number_input('Salário')

        btnAdicionar = st.form_submit_button('Adicionar')

    if btnAdicionar == True:

        funcionarioCadastrar = pd.DataFrame([
            {
                'Nome': nome,
                'Idade': idade,
                'Departamento': departamento,
                'Cargo': cargo,
                'Salário': salario,
                ##'Data de Admissão': dataAdmissao
            }
        ])

        updateSpread = pd.concat([listaFuncionarios, funcionarioCadastrar], ignore_index=True)

        conn = st.connection('gsheets', type=GSheetsConnection)
        
        conn.update(worksheet='teste', data=updateSpread)
        
        st.success('Cadastrado')
        funcionarios()

    st.table(listaFuncionarios)
