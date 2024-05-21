import streamlit as st
import pandas as pd
from main import update, getTipoConta

def tipoConta():
    
    with st.form('formTipoConta'):
        tipo = st.text_input('Conta')
        
        btnCriar = st.form_submit_button('Criar')
        
        if btnCriar == True:
            if tipo:
                st.header('em construção')
            