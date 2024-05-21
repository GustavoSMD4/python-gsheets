from streamlit_option_menu import option_menu
from views.funcionario.cadastroFuncionario import cadastroFuncionario
from views.funcionario.consultaFuncionario import consulta
from views.funcionario.excluirFuncionario import deleteFuncionario
from views.funcionario.editarFuncionario import editar
from main import consultaFuncionarios, getDepartamentos, getCargos
 
def viewFuncionarios():
     
    tipoView = option_menu(menu_title='Funcionários',
                           options=['Consulta', 'Cadastro', 'Editar', 'Excluir'],
                           icons=['search', 'person-plus-fill', 'pencil-square', 'person-x-fill'],
                           menu_icon='person-vcard-fill', 
                           orientation='horizontal')
    
    if tipoView == 'Cadastro':
        cadastroFuncionario()
    elif tipoView == 'Consulta':
        consultaFuncionarios()
        consulta()
    elif tipoView == 'Excluir':
        deleteFuncionario()
    elif tipoView == 'Editar':
        editar()