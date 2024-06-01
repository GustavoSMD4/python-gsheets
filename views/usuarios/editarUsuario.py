import streamlit as st
import pandas as pd
from main import update, login
from validacoes import validarInputs

def editar() -> None:
    usuarios: pd.DataFrame = st.session_state['usuarios']
    roles: pd.DataFrame = st.session_state['roles']

    st.header('Editar Usuário')
    nome = st.text_input('Nome de usuário do usuário que deseja editar').rstrip()
    btnLocalizarUsuario = st.button('localizar usuário')

    usuarioUpdate = None
    if btnLocalizarUsuario:
        usuarioUpdate = usuarios[usuarios['usuario'] == nome]
        
        if usuarioUpdate.empty:
            st.warning('Usuário não localizado.')
        else:
            st.session_state['usuarioUpdate'] = usuarioUpdate

    if 'usuarioUpdate' in st.session_state:
        usuarioUpdate = st.session_state['usuarioUpdate']
        
        if not usuarioUpdate.empty:
            with st.form('formEditarUsuário'):
                
                col1, col2= st.columns(2)
                col3, col4 = st.columns([2, 1])
                
                usuarioEditar = col1.text_input('Usuário', value=usuarioUpdate.iloc[0]['usuario'], autocomplete='off').rstrip()
                
                nomeEditar = col2.text_input('Nome', value=usuarioUpdate.iloc[0]['nome'], autocomplete='off').rstrip()
                
                senha = col3.text_input('Senha', value=usuarioUpdate.iloc[0]['senha'], type='password').rstrip()
                
                role = col4.selectbox('Role', options=roles['role'], index=['admin', 'financeiro', 'user'].index(usuarioUpdate.iloc[0]['role']))
                
                btnEditar = st.form_submit_button('Editar')
                
                if btnEditar == True:
                    try:
                        validarInputs((usuarioEditar, nomeEditar, senha, role), 
                                      (str, str, str, str),
                                      ('Usuário', 'Nome', 'Senha', 'Role'))
                        
                        usuarios.loc[usuarios['usuario'] == nome, 
                                         ['usuario', 'nome', 'senha', 'role']] = [usuarioEditar, nomeEditar, senha, role]

                        update(worksheet='usuario', data=usuarios)

                        st.success('Atualizado com sucesso.')
                        st.session_state.pop('usuarioUpdate')  # Limpa o estado após a atualização
                        
                    except ValueError as e:
                        st.warning(e)
    