import streamlit as st
import pandas as pd
from main import update, consultaContas

def create():

    contas = st.session_state['contas']
    tipos = st.session_state['tipoConta']
    
    with st.form('formCriarConta'):
        conta = st.selectbox('Conta', options=tipos)
        
        col1, col2 = st.columns([2, 1])
        
        vencimento = col1.date_input('Data vencimento', format='DD/MM/YYYY')
        valor = col2.number_input('Valor')
        
        btnCriar = st.form_submit_button('Confirmar')
        
        if btnCriar:
            if conta and vencimento and valor:
               
               contaCriar = pd.DataFrame([
                   {
                       'conta': conta,
                       'vencimento': vencimento,
                       'pago': 0,
                       'valor': float(valor)
                   }
               ])
               
               dfUpdate = pd.concat([contas, contaCriar], ignore_index=True)
               update(worksheet='contas', data=dfUpdate)
               
               st.success('Salvo com sucesso.')
               
               st.session_state['contas'] = dfUpdate
               consultaContas()
                
                
            else:
                st.warning('Algum campo está vazio.')
        