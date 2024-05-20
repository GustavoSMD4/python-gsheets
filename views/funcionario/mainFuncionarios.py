import streamlit as st
import streamlit_shadcn_ui as ui
from views.funcionario.cadastroFuncionario import cadastroFuncionario
from views.funcionario.consultaFuncionario import consultaFuncionarios
from views.funcionario.excluirFuncionario import deleteFuncionario
from views.funcionario.editarFuncionario import editar
import main
 
def viewFuncionarios():
     
    tipoView = ui.tabs(options=['Consulta', 'Cadastro', 'Editar', 'Excluir'], default_value='Consulta')
    if tipoView == 'Cadastro':
        cadastroFuncionario()
    elif tipoView == 'Consulta':
        main.consultaFuncionarios()
        consultaFuncionarios()
    elif tipoView == 'Excluir':
        deleteFuncionario()
    elif tipoView == 'Editar':
        editar()