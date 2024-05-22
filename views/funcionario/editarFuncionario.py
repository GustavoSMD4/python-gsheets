import streamlit as st
from main import update, consultaFuncionarios, getDepartamentos, getCargos

def editar():
    funcionarios = st.session_state['funcionarios']
    
    if 'departamentos' not in st.session_state:
        getDepartamentos()
        
    if 'cargos' not in st.session_state:
        getCargos()
    
    departamentos = st.session_state['departamentos']
    cargos = st.session_state['cargos']

    st.header('Editar funcionário')
    cpf = st.text_input('CPF do funcionário que deseja editar', autocomplete='off').rstrip()
    btnLocalizarFuncionario = st.button('localizar funcionário')

    funcionarioUpdate = None
    if btnLocalizarFuncionario:
        cpf = cpf.replace('.', '').replace('-', '')
        if len(cpf) != 11:
            st.warning('CPF inválido.')
        else: 
            funcionarioUpdate = funcionarios[funcionarios['cpf'] == cpf]

            if funcionarioUpdate.empty:
                st.warning('Funcionário não localizado.')
            else:
                st.session_state['funcionarioUpdate'] = funcionarioUpdate

    if 'funcionarioUpdate' in st.session_state:
        funcionarioUpdate = st.session_state['funcionarioUpdate']
        
        if not funcionarioUpdate.empty and cpf:
            with st.form('formEditarFuncionario', clear_on_submit=True):
                col1, col2 = st.columns([2, 1])
                col3, col4, col5 = st.columns(3)
                
                nomeEditar = col1.text_input('Nome', value=funcionarioUpdate.iloc[0]['nome'], autocomplete='off')
                
                cpfEditar = col2.text_input('cpf', value=funcionarioUpdate.iloc[0]['cpf'], autocomplete='off')
                
                departamento = col3.selectbox('Departamento', options=departamentos['departamento'],
                                              index=list(departamentos['departamento']).index(funcionarioUpdate.iloc[0]['departamento']))
                
                cargo = col4.selectbox('Cargo', options=cargos['cargo'], 
                                       index=list(cargos['cargo']).index(funcionarioUpdate.iloc[0]['cargo']))
                
                salario = col5.number_input('Salário', value=float(funcionarioUpdate.iloc[0]['salario']))
                
                btnEditar = st.form_submit_button('Editar')
                
                if btnEditar == True:
                    cpfEditar = cpfEditar.replace('.', '').replace('-', '')
                    funcionarios.loc[funcionarios['cpf'] == cpf, 
                                     ['cpf', 'nome', 'departamento', 'cargo', 'salario']] = [cpfEditar, nomeEditar.upper(), departamento, cargo, float(salario)]
                    
                    update(worksheet='funcionario', data=funcionarios)
                    consultaFuncionarios()
                    
                    st.success('Atualizado com sucesso.')
                    st.session_state.pop('funcionarioUpdate')  # Limpa o estado após a atualização

