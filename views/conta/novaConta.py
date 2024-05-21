import streamlit as st
import pandas as pd
from main import update, consultaContas

def create():
    
    with st.form('formCriarConta'):
        # CONTA	VENCIMENTO	PAGAMENTO EM	VALOR	TIPO
        conta = st.text_input('nome Conta')