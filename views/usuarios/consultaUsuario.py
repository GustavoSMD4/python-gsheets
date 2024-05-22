import streamlit as st
import streamlit_shadcn_ui as ui
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from main import update, login

def consulta():
    
    usuarios = st.session_state['usuarios']
    
    usuariosFiltrado = usuarios[['nome','usuario', 'role']]
    
    builder = GridOptionsBuilder.from_dataframe(usuariosFiltrado)
    builder.configure_selection(selection_mode='single', use_checkbox=True)
    go = builder.build()
    
    st.divider()
    
    col1, col2 = st.columns([1, 3])
    
    try:
    
        operacao = col1.radio('Operação', options=['Editar', 'Excluir'])

        linhaSelecionada = None
    
        with col2:
            linhaSelecionada = AgGrid(usuariosFiltrado, fit_columns_on_grid_load=True, height=200,
                                      header_checkbox_selection_filtered_only=True,
                                      gridOptions=go, update_mode=GridUpdateMode.SELECTION_CHANGED)
    
        if linhaSelecionada and 'selected_rows' in linhaSelecionada and len(linhaSelecionada['selected_rows']) > 0:
            nomeUsuarioAntigo = linhaSelecionada['selected_rows']['usuario'].iloc[0]
            
            if operacao == 'Editar':
                with st.form(key='formEditar'):
                    
                    st.header(F"Editar {linhaSelecionada['selected_rows']['nome'].iloc[0]}")
                    
                    col1, col2, col3 = st.columns([2, 2, 1])
                    
                    nome = col1.text_input('Nome', value=linhaSelecionada['selected_rows']['nome'].iloc[0], autocomplete='off').rstrip()
                    usuarioEditar = col2.text_input('Nome de usuário', value=linhaSelecionada['selected_rows']['usuario'].iloc[0], autocomplete='off').rstrip()
                    role = col3.selectbox('Role', options=['admin', 'user'], 
                                        index=['admin', 'user'].index(linhaSelecionada['selected_rows']['role'].iloc[0]))
                    
                    btnEditar = st.form_submit_button('Confirmar')
                    
                    if btnEditar == True and nome and usuarioEditar and role:
                        
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
                            st.rerun()
                    
                        elif usuarioEditar == nomeUsuarioAntigo:
                            
                            usuarios.loc[usuarios['usuario'] == nomeUsuarioAntigo, 
                                     ['usuario', 'nome', 'senha', 'role']] = [usuarioEditar, nome,
                                                                              usuarios[usuarios['usuario'] == nomeUsuarioAntigo]['senha'].iloc[0], role]
                            
                            update(worksheet='usuario', data=usuarios)
                            usuariosFiltrado = usuarios[['nome','usuario', 'role']]
                            st.rerun()
                    
            elif operacao == 'Excluir':
                st.header(F"Excluir {linhaSelecionada['selected_rows']['nome'].iloc[0]} ?")
                ui.table(linhaSelecionada['selected_rows'])
                
    except TypeError:
        st.warning('Selecione uma linha da tabela.')