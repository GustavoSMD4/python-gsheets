import streamlit as st
from st_aggrid import AgGrid


def historico():
    
    movimentacoes = st.session_state['movimentacoesCaixa']
    
    AgGrid(movimentacoes, fit_columns_on_grid_load=True, height=350)