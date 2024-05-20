import streamlit as st
import pandas as pd
from main import update, consultaFuncionarios

def cadastroFuncionario():
    
    listaFuncionarios = st.session_state['funcionarios']

    with st.form('formCadastroFuncionario', clear_on_submit=True):

        st.title('Cadastro funcionário')
        nome = st.text_input('Nome')

        col1, col2 = st.columns(2)

        idade = col1.text_input('idade')
        
        col3, col4, col5 = st.columns(3)

        departamento = col3.selectbox('Departamento', options=listaFuncionarios['Departamento'].unique())
        cargo = col4.selectbox('cargo', options=listaFuncionarios['Cargo'].unique())
        salario = col5.number_input('Salário')

        btnAdicionar = st.form_submit_button('Adicionar')

    if btnAdicionar == True:

        funcionarioCadastrar = pd.DataFrame([
            {
                'Nome': nome.upper().rstrip(),
                'Idade': int(idade),
                'Departamento': departamento,
                'Cargo': cargo,
                'Salário': float(salario),
            }
        ])

        updateSpread = pd.concat([listaFuncionarios, funcionarioCadastrar], ignore_index=True)
        
        update(worksheet='teste', data=updateSpread)
        consultaFuncionarios()
        
        st.success('Cadastrado')