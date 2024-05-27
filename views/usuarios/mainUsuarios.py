import streamlit as st
from streamlit_option_menu import option_menu
from .consultaUsuario import consulta
from .editarUsuario import editar
from .criarUsuario import create
from main import getRoles

def viewUsuarios():
    
    if 'roles' not in st.session_state:
        getRoles()
    
    view = option_menu(menu_title='Usuários',
                       options=['Usuários', 'Criar Usuário', 'Editar Usuários'],
                       icons=['person-fill', 'person-plus-fill', 'pencil-square'],
                       menu_icon='person-fill-gear',
                       orientation='horizontal')
    
    if view == 'Usuários':
        consulta()
        
    elif view == 'Criar Usuário':
        create()
        
    elif view == 'Editar Usuários':
        editar()