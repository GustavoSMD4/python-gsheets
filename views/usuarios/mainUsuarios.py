from streamlit_option_menu import option_menu
from .consultaUsuario import consulta
from .editarUsuario import editar

def viewUsuarios():
    
    view = option_menu(menu_title='Usuários',
                       options=['Usuários', 'Editar Usuários'],
                       icons=['person-fill', 'pencil-square'],
                       menu_icon='person-fill-gear',
                       orientation='horizontal')
    
    if view == 'Usuários':
        consulta()
        
    elif view == 'Editar Usuários':
        editar()