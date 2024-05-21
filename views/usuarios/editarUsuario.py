import streamlit as st
from main import update, login

def editar():
    usuarios = st.session_state['usuarios']

    st.header('Editar Usuário')
    nome = st.text_input('Nome de usuário do usuário que deseja editar')
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
                
                usuarioEditar = col1.text_input('Usuário', value=usuarioUpdate.iloc[0]['usuario'], autocomplete='off')
                
                nomeEditar = col2.text_input('Idade', value=usuarioUpdate.iloc[0]['nome'], autocomplete='off')
                
                senha = col3.text_input('Senha', value=usuarioUpdate.iloc[0]['senha'], type='password')
                
                role = col4.selectbox('Role', options=['admin', 'user'], index=['admin', 'user'].index(usuarioUpdate.iloc[0]['role']))
                
                btnEditar = st.form_submit_button('Editar')
                
                if btnEditar == True:
                    usuarios.loc[usuarios['usuario'] == nome, 
                                     ['usuario', 'nome', 'senha', 'role']] = [usuarioEditar, nomeEditar, senha, role]
                    
                    update(worksheet='usuario', data=usuarios)
                    
                    st.success('Atualizado com sucesso.')
                    st.session_state.pop('usuarioUpdate')  # Limpa o estado após a atualização
    