import streamlit as st
import pandas as pd
import streamlit_shadcn_ui as ui
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from main import update, consultaFuncionarios
from validacoes import validarInputs

def consulta():
    
    funcionarios = st.session_state['funcionarios']
    departamentos = st.session_state['departamentos']
    cargos = st.session_state['cargos']
    
    if 'linhaSelecionada' not in st.session_state:
        st.session_state['linhaSelecionada'] = False
        
    if 'selected_row' not in st.session_state:
        st.session_state['selected_row'] = pd.DataFrame()
        
    if 'tipoOperacao' not in st.session_state:
        ## inicial, editar, excluir
        st.session_state['tipoOperacao'] = 'inicial'
    
    if st.session_state['tipoOperacao'] == 'inicial':

        funcionariosDisplay = funcionarios[0:]
        funcionariosDisplay['salario'] = funcionarios['salario'].apply(lambda x: F"R${x:,.2f}")

        builder = GridOptionsBuilder.from_dataframe(funcionariosDisplay[['cpf', 'nome', 'departamento']])
        builder.configure_selection(selection_mode='single', use_checkbox=True)
        go = builder.build()  

        with st.container(border=True):
            col1, col2 = st.columns([1, 3])

            operacao = col1.radio('Operação', options=['Editar', 'Excluir'])

            if st.session_state['linhaSelecionada'] == False:
                try:
                    linhaSelecionada = st.session_state['selected_row']

                    with col2:
                        linhaSelecionada = AgGrid(funcionariosDisplay, fit_columns_on_grid_load=True, height=200,
                                                  header_checkbox_selection_filtered_only=True,
                                                  gridOptions=go, update_mode=GridUpdateMode.SELECTION_CHANGED)  

                    if linhaSelecionada and 'selected_rows' in linhaSelecionada and len(linhaSelecionada['selected_rows']) > 0:
                        cpfAntigo = linhaSelecionada['selected_rows']['cpf'].iloc[0]
                        st.session_state['selected_row'] = funcionarios[funcionarios['cpf'] == cpfAntigo]
                        st.session_state['linhaSelecionada'] = True
                        st.session_state['tipoOperacao'] = operacao
                        st.rerun()


                except TypeError:
                    st.warning('Selecione uma linha da tabela.')
       
    elif st.session_state['tipoOperacao'] != 'inicial':  
              
        if st.session_state['linhaSelecionada'] == True:

            linhaSelecionada = st.session_state['selected_row']
            operacao = st.session_state['tipoOperacao']
            cpfAntigo = linhaSelecionada.iloc[0]['cpf']
            
            if operacao == 'Editar':
                
                with st.container(border=True):
                    btnVoltar = st.button('Voltar')

                    with st.form('formEditarFuncionario', clear_on_submit=True, border=False):

                        st.header(F"Editar {linhaSelecionada['nome'].iloc[0]}")

                        col1, col2 = st.columns([2, 1])
                        col3, col4, col5 = st.columns(3)

                        nomeEditar = col1.text_input('Nome', value=linhaSelecionada.iloc[0]['nome'], autocomplete='off')

                        cpfEditar = col2.text_input('CPF', value=linhaSelecionada.iloc[0]['cpf'], autocomplete='off')

                        departamento = col3.selectbox('Departamento', options=departamentos['departamento'],
                                                      index=list(departamentos['departamento']).index(linhaSelecionada.iloc[0]['departamento']))

                        cargo = col4.selectbox('Cargo', options=cargos['cargo'], 
                                               index=list(cargos['cargo']).index(linhaSelecionada.iloc[0]['cargo']))

                        salario = col5.number_input('Salário', value=float(linhaSelecionada.iloc[0]['salario']))

                        btnEditar = st.form_submit_button('Editar')

                        if btnVoltar == True:
                            st.session_state.pop('linhaSelecionada')
                            st.session_state.pop('selected_row')
                            st.session_state.pop('tipoOperacao')
                            st.rerun()

                        if btnEditar == True:
                            try:
                                validarInputs((nomeEditar, cpfEditar, departamento, cargo, salario),
                                              (str, str, str, str, float),
                                              ('Nome', 'CPF', 'Departamento', 'Cargo', 'Salário'))
                                
                                if cpfEditar != cpfAntigo:

                                    cpfExiste = funcionarios[funcionarios['cpf'] == cpfEditar]

                                    if len(cpfExiste) >= 1:
                                        st.warning('CPF já cadastrado.')

                                    else:

                                        funcionarios.loc[funcionarios['cpf'] == cpfAntigo, 
                                             ['cpf', 'nome', 'departamento', 'cargo', 'salario']] = [cpfEditar, nomeEditar.upper(), departamento, cargo, float(salario)]

                                    update(worksheet='funcionario', data=funcionarios)
                                    st.success('Salvo com sucesso.')
                                    st.session_state.pop('linhaSelecionada')
                                    st.session_state.pop('selected_row')
                                    st.session_state.pop('tipoOperacao')
                                    st.rerun()

                                elif cpfEditar == cpfAntigo:

                                    funcionarios.loc[funcionarios['cpf'] == cpfAntigo, 
                                             ['cpf', 'nome', 'departamento', 'cargo', 'salario']] = [cpfEditar, nomeEditar.upper(), departamento, cargo, float(salario)]

                                    update(worksheet='funcionario', data=funcionarios)
                                    st.success('Salvo com sucesso.')
                                    st.session_state.pop('linhaSelecionada')
                                    st.session_state.pop('selected_row')
                                    st.session_state.pop('tipoOperacao')
                                    st.rerun()
                                    
                            except ValueError as e:
                                st.warning(e)

            elif operacao == 'Excluir':
                with st.container(border=True):
                    
                     btnCancelar = st.button('Cancelar')
                     
                     with st.form('formExcluir', border=False): 
                          
                         st.header(F"Excluir {linhaSelecionada['nome'].iloc[0]} ?")
                         ui.table(linhaSelecionada)
                         btnExcluir = st.form_submit_button('Excluir')

                         if btnExcluir == True:
                             funcionarios = funcionarios[funcionarios['cpf'] != linhaSelecionada['cpf'].iloc[0]]

                             update(worksheet='funcionario', data=funcionarios)

                             st.session_state['funcionarios'] = funcionarios
                             st.session_state.pop('linhaSelecionada')
                             st.session_state.pop('selected_row')
                             st.session_state.pop('tipoOperacao')
                             st.rerun()

                         if btnCancelar == True:
                             st.session_state.pop('linhaSelecionada')
                             st.session_state.pop('selected_row')
                             st.session_state.pop('tipoOperacao')
                             st.rerun()