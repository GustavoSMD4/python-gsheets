import streamlit as st
from streamlit_option_menu import option_menu
from .contas import consulta
from .tipoConta import tipoConta
from .novaConta import create
from main import getTipoConta, consultaContas

def viewContas():
    
    if 'contas' not in st.session_state:
        consultaContas()
            
    if 'tipoConta' not in st.session_state:
        getTipoConta()
    
    view = option_menu(menu_title='Contas',
                       options=['Contas', 'Tipo Conta', 'Nova Conta'],
                       icons=['credit-card', 'plus-square', 'cash'],
                       menu_icon='credit-card-2-back-fill',
                       orientation='horizontal')
    
    if view == 'Contas':
        consulta()
        
    elif view == 'Tipo Conta':
        tipoConta()
        
    elif view == 'Nova Conta':
        create()