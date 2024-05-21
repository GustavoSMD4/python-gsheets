import streamlit as st
import pandas as pd
from main import update, consultaFuncionarios, getDepartamentos, getCargos

def cadastroFuncionario():
    
    listaFuncionarios = st.session_state['funcionarios']
    
    if 'departamentos' not in st.session_state:
        getDepartamentos()
        
    if 'cargos' not in st.session_state:
        getCargos()
    
    departamentos = st.session_state['departamentos']
    cargos = st.session_state['cargos']

    with st.form('formCadastroFuncionario', clear_on_submit=True):

        st.title('Cadastro funcionário')
        
        col1, col2 = st.columns([3, 1])
        
        nome = col1.text_input('Nome', autocomplete='off')
        idade = col2.text_input('idade', autocomplete='off')
        
        col3, col4, col5 = st.columns(3)

        departamento = col3.selectbox('Departamento', options=departamentos['departamento'])
        cargo = col4.selectbox('Cargo', options=cargos['cargo'])
        salario = col5.number_input('Salário')

        btnAdicionar = st.form_submit_button('Adicionar')

    if btnAdicionar == True:

        funcionarioCadastrar = pd.DataFrame([
            {
                'nome': nome.upper().rstrip(),
                'idade': int(idade),
                'departamento': departamento,
                'cargo': cargo,
                'salario': float(salario),
            }
        ])

        funcionarios = pd.concat([listaFuncionarios, funcionarioCadastrar], ignore_index=True)
        
        update(worksheet='funcionario', data=funcionarios)
        consultaFuncionarios()
        
        st.success('Cadastrado')