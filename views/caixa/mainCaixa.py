import streamlit as st
from streamlit_option_menu import option_menu
from .movimentacao import movimetacao
from .historico import historico
from main import getCaixa, getMovimentacoesCaixa

def viewCaixa():
    
    if 'caixa' not in st.session_state:
        getCaixa()
    
    if 'movimentacoesCaixa' not in st.session_state:
        getMovimentacoesCaixa()
        
    caixa = st.session_state['caixa']
    caixa = caixa.iloc[0]
    
    col1, col2 = st.columns(2)
    col1.header(F"{caixa['caixa']}")
    col2.header(F"Saldo R${caixa['saldo']:,.2f}")
    
    st.write('')
    
    movimetacao()
    
    st.subheader('Histórico')
    historico()
    
