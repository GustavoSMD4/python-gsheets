from streamlit_option_menu import option_menu

def viewContas():
    
    view = option_menu(menu_title='Contas',
                       options=['Contas', 'Nova conta'],
                       icons=['credit-card', 'plus-square'],
                       menu_icon='credit-card-2-back-fill',
                       orientation='horizontal')