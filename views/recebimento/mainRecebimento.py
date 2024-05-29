import streamlit as st

def viewRecebimentos() -> None:
    st.header('recebimento')
    
    st.tabs(['Pagamentos Clientes', 'Novo recebimento'])