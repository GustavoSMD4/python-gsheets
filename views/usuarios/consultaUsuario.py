import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from main import update, login

def consulta():
    
    usuarios = st.session_state['usuarios']
    
    usuariosFiltrado = usuarios[['nome','usuario', 'role']]
    
    if 'linhaSelecionada' not in st.session_state:
        st.session_state['linhaSelecionada'] = False
        
    if 'selected_row' not in st.session_state:
        st.session_state['selected_row'] = pd.DataFrame()
    
    builder = GridOptionsBuilder.from_dataframe(usuariosFiltrado)
    builder.configure_selection(selection_mode='single', use_checkbox=True)
    go = builder.build()
    
    st.divider()
    
    col1, col2 = st.columns([1, 3])
    
    operacao = col1.radio('Operação', options=['Editar', 'Excluir'])
        
    if st.session_state['linhaSelecionada'] == False:
        try:
            linhaSelecionada = st.session_state['selected_row']

            with col2:
                linhaSelecionada = AgGrid(usuariosFiltrado, fit_columns_on_grid_load=True, height=200,
                                          header_checkbox_selection_filtered_only=True,
                                          gridOptions=go, update_mode=GridUpdateMode.SELECTION_CHANGED)
    
            if linhaSelecionada and 'selected_rows' in linhaSelecionada and len(linhaSelecionada['selected_rows']) > 0:
                nomeUsuarioAntigo = linhaSelecionada['selected_rows']['usuario'].iloc[0]
                st.session_state['selected_row'] = linhaSelecionada['selected_rows']
                st.session_state['linhaSelecionada'] = True
                st.rerun()
            
                
        except TypeError:
            st.warning('Selecione uma linha da tabela.')
            
    elif st.session_state.get('linhaSelecionada', True) is True:
        
        linhaSelecionada = st.session_state['selected_row']
        
        if operacao == 'Editar':
            with col2:
                
                btnVoltar = st.button('Voltar')
                
                with st.form(key='formEditar'):

                    st.header(F"Editar {linhaSelecionada['nome'].iloc[0]}")

                    nome = st.text_input('Nome', value=linhaSelecionada['nome'].iloc[0], autocomplete='off').rstrip()

                    col1, col2= st.columns([2, 1])

                    
                    usuarioEditar = col1.text_input('Nome de usuário', value=linhaSelecionada['usuario'].iloc[0], autocomplete='off').rstrip()
                    role = col2.selectbox('Role', options=['admin', 'user'], 
                                        index=['admin', 'user'].index(linhaSelecionada['role'].iloc[0]))

                    btnEditar = st.form_submit_button('Confirmar')
                    
                    if btnVoltar == True:
                        st.session_state.pop('linhaSelecionada')
                        st.session_state.pop('selected_row')
                        st.rerun()

                    if btnEditar == True and nome and usuarioEditar and role:

                        nomeUsuarioAntigo = linhaSelecionada['usuario'].iloc[0]
                        if usuarioEditar != nomeUsuarioAntigo:

                            usuarioExiste = usuarios[usuarios['usuario'] == usuarioEditar]

                            if len(usuarioExiste) >= 1:
                                st.warning('Nome de usuário já existe.')

                            else:

                                usuarios.loc[usuarios['usuario'] == nomeUsuarioAntigo, 
                                     ['usuario', 'nome', 'senha', 'role']] = [usuarioEditar, nome,
                                                                              usuarios[usuarios['usuario'] == nomeUsuarioAntigo]['senha'].iloc[0], role]

                            update(worksheet='usuario', data=usuarios)
                            usuariosFiltrado = usuarios[['nome','usuario', 'role']]
                            st.success('Salvo com sucesso.')
                            st.session_state.pop('linhaSelecionada')
                            st.session_state.pop('selected_row')
                            st.rerun()

                        elif usuarioEditar == nomeUsuarioAntigo:

                            usuarios.loc[usuarios['usuario'] == nomeUsuarioAntigo, 
                                     ['usuario', 'nome', 'senha', 'role']] = [usuarioEditar, nome,
                                                                              usuarios[usuarios['usuario'] == nomeUsuarioAntigo]['senha'].iloc[0], role]

                            update(worksheet='usuario', data=usuarios)
                            usuariosFiltrado = usuarios[['nome','usuario', 'role']]
                            st.success('Salvo com sucesso.')
                            st.session_state.pop('linhaSelecionada')
                            st.session_state.pop('selected_row')
                            st.rerun()
                    
        elif operacao == 'Excluir':
            with col2:
                btnCancelar = st.button('Cancelar')
                with st.form('formExcluir'):  
                    st.header(F"Excluir {linhaSelecionada['nome'].iloc[0]} ?")
                    ui.table(linhaSelecionada)
                    btnExcluir = st.form_submit_button('Excluir')
                    
                    if btnCancelar == True:
                        st.session_state.pop('linhaSelecionada')
                        st.session_state.pop('selected_row')
                        st.rerun()
                    
                    if btnExcluir:
                        
                        if st.session_state['usuarioLogado']['usuario'] == linhaSelecionada['usuario'].iloc[0]:
                            st.warning('O usuário que você tentou excluir é o que está sendo usado agora.')
                        else:
                        
                            usuarios = usuarios[usuarios['usuario'] != linhaSelecionada['usuario'].iloc[0]]
                    
                            update(worksheet='usuario', data=usuarios)
                            st.session_state.pop('linhaSelecionada')
                            st.session_state.pop('selected_row')
                            st.session_state['usuarios'] = usuarios
                            st.rerun()