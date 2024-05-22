import streamlit as st
import streamlit_shadcn_ui as ui
from st_aggrid import AgGrid

def consulta():
    funcionarios = st.session_state['funcionarios']
    
    st.subheader('Consulta funcionários')
    
    funcionariosDisplay = funcionarios[0:]
    funcionariosDisplay['salario'] = funcionarios['salario'].apply(lambda x: F"R${x:,.2f}")
    
    AgGrid(funcionariosDisplay, height=300, fit_columns_on_grid_load=True)