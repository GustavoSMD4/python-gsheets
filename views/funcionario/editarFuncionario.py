import streamlit as st
from main import update, consultaFuncionarios

def editar():
    funcionarios = st.session_state['funcionarios']
    departamentos = st.session_state['departamentos']
    cargos = st.session_state['cargos']

    st.header('Editar funcionário')
    nome = st.text_input('Nome do funcionário que deseja editar')
    btnLocalizarFuncionario = st.button('localizar funcionário')

    funcionarioUpdate = None
    if btnLocalizarFuncionario:
        funcionarioUpdate = funcionarios[funcionarios['nome'] == nome.upper()]
        
        if funcionarioUpdate.empty:
            st.warning('Funcionário não localizado.')
        else:
            st.session_state['funcionarioUpdate'] = funcionarioUpdate

    if 'funcionarioUpdate' in st.session_state:
        funcionarioUpdate = st.session_state['funcionarioUpdate']
        
        if not funcionarioUpdate.empty:
            with st.form('formEditarFuncionario'):
                col1, col2 = st.columns([3, 1])
                col3, col4, col5 = st.columns(3)
                
                nomeEditar = col1.text_input('Nome', value=funcionarioUpdate.iloc[0]['nome'], autocomplete='off')
                
                idade = col2.text_input('Idade', value=int(funcionarioUpdate.iloc[0]['idade']), autocomplete='off')
                
                departamento = col3.selectbox('Departamento', options=departamentos['departamento'],
                                              index=list(departamentos['departamento']).index(funcionarioUpdate.iloc[0]['departamento']))
                
                cargo = col4.selectbox('Cargo', options=cargos['cargo'], 
                                       index=list(cargos['cargo']).index(funcionarioUpdate.iloc[0]['cargo']))
                
                salario = col5.number_input('Salário', value=float(funcionarioUpdate.iloc[0]['salario']))
                
                btnEditar = st.form_submit_button('Editar')
                
                if btnEditar == True:
                    funcionarios.loc[funcionarios['nome'] == nome.upper(), 
                                     ['nome', 'idade', 'departamento', 'cargo', 'salario']] = [nomeEditar.upper(), int(idade), departamento, cargo, float(salario)]
                    
                    update(worksheet='funcionario', data=funcionarios)
                    consultaFuncionarios()
                    
                    st.success('Atualizado com sucesso.')
                    st.session_state.pop('funcionarioUpdate')  # Limpa o estado após a atualização

