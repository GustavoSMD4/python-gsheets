import streamlit as st
from main import update, consultaFuncionarios

def editar():

    st.header('Editar funcionário')
    nome = st.text_input('Nome do funcionário que deseja editar')
    btnLocalizarFuncionario = st.button('localizar funcionário')

    if btnLocalizarFuncionario == True or btnLocalizarFuncionario == False:
        funcionarios = st.session_state['funcionarios']

        funcionarioUpdate = funcionarios[funcionarios['Nome'] == nome.upper()]

        if len(funcionarioUpdate) != 1:
            st.warning('Funcionário não localizado')
            
        else:
            with st.form('formEditarFuncionario'):
                col1, col2 = st.columns([3, 1])
                col3, col4, col5 = st.columns(3)
                
                nomeEditar = col1.text_input('Nome', value=funcionarioUpdate.iloc[0]['Nome'])
                
                idade = col2.text_input('Idade', value=int(funcionarioUpdate.iloc[0]['Idade']))
                
                departamento = col3.selectbox('Departamento', options=funcionarios['Departamento'].unique(),
                                            index=list(funcionarios['Departamento'].unique()).index(funcionarioUpdate.iloc[0]['Departamento']))
                
                cargo = col4.selectbox('Cargo', options=funcionarios['Cargo'].unique(), 
                                     index=list(funcionarios['Cargo'].unique()).index(funcionarioUpdate.iloc[0]['Cargo']))
                
                salario = col5.number_input('Salário', value=float(funcionarioUpdate.iloc[0]['Salário']))
                
                btnEditar = st.form_submit_button('Editar')
                
                if btnEditar == True or btnEditar == False:
                    funcionarios.loc[funcionarios['Nome'] == nome.upper(),
                                     ['Nome', 'Idade', 'Departamento', 'Cargo', 'Salário']] = [nomeEditar.upper(), int(idade), departamento, cargo, float(salario)]
                    
                    st.table(funcionarios)
                    # update(data=funcionarios, worksheet='teste')
                    # consultaFuncionarios()
                
                    st.success('Atualizado com sucesso.')