import streamlit as st
import pandas as pd
from main import update, consultaFuncionarios, getDepartamentos, getCargos
from validacoes import validarInputs

def cadastroFuncionario():
    
    listaFuncionarios = st.session_state['funcionarios']
    
    if 'departamentos' not in st.session_state:
        getDepartamentos()
        
    if 'cargos' not in st.session_state:
        getCargos()
    
    departamentos = st.session_state['departamentos']
    cargos = st.session_state['cargos']

    with st.form('formCadastroFuncionario'):

        st.title('Cadastro funcionário')
        
        col1, col2 = st.columns([2, 1])
        
        nome = col1.text_input('Nome', autocomplete='off')
        cpf = col2.text_input('CPF', autocomplete='off')
        
        col3, col4, col5 = st.columns(3)

        departamento = col3.selectbox('Departamento', options=departamentos['departamento'])
        cargo = col4.selectbox('Cargo', options=cargos['cargo'])
        salario = col5.number_input('Salário')

        btnAdicionar = st.form_submit_button('Adicionar')

        if btnAdicionar == True:
           try:
                validarInputs((nome, cpf, departamento, cargo, salario),
                              (str, str, str, str, float),
                              ('Nome', 'CPF', 'Departamento', 'Cargo', 'Salário'))
                cpf = cpf.replace('.', '').replace('-', '')
                
                if len(cpf) != 11:
                    st.warning('CPF inválido')

                else:
                    
                    cpfExiste = listaFuncionarios[listaFuncionarios['cpf'] == cpf]
                    if len(cpfExiste) >= 1:
                        st.warning('CPF já cadastrado')
                        
                    else:
                        
                        funcionarioCadastrar = pd.DataFrame([
                            {
                                'cpf': cpf,
                                'nome': nome.upper().rstrip(),
                                'departamento': departamento,
                                'cargo': cargo,
                                'salario': float(salario),
                            }
                        ])

                        funcionarios = pd.concat([listaFuncionarios, funcionarioCadastrar], ignore_index=True)

                        update(worksheet='funcionario', data=funcionarios)
                        consultaFuncionarios()

                        st.success('Cadastrado')

           except ValueError as e:
               st.warning(e)