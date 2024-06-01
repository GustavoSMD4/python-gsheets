import streamlit as st
from streamlit_option_menu import option_menu
from views.funcionario.cadastroFuncionario import cadastroFuncionario
from views.funcionario.consultaFuncionario import consulta
from main import consultaFuncionarios, getDepartamentos, getCargos
 
def viewFuncionarios():
        
    if 'funcionarios' not in st.session_state or len(st.session_state['funcionarios']) == 0:
        consultaFuncionarios()
    
    if 'departamentos' not in st.session_state:
        getDepartamentos()
        
    if 'cargos' not in st.session_state:
        getCargos()
     
    tipoView = option_menu(menu_title='Funcionários',
                           options=['Consulta', 'Cadastro'],
                           icons=['search', 'person-plus-fill'],
                           menu_icon='person-vcard-fill', 
                           orientation='horizontal')
    
    if tipoView == 'Cadastro':
        cadastroFuncionario()
        
    elif tipoView == 'Consulta':
        consulta()