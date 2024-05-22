import streamlit as st
import pandas as pd
from main import update, getTipoConta

def tipoConta():
    
    tipos = st.session_state['tipoConta']
    
    with st.form('formTipoConta'):
        tipo = st.text_input('Conta').rstrip().upper()
        
        btnCriar = st.form_submit_button('Criar')
        
        if btnCriar == True:
            if tipo:
                
                tipoExiste = tipos[tipos['tipo']== tipo]
                if len(tipoExiste) >= 1:
                    st.warning('Esse tipo já existe')
                    
                else:
                    
                    tipoCriar = pd.DataFrame([
                        {
                            'tipo': tipo
                        }
                    ])
                    
                    dfUpdate = pd.concat([tipos, tipoCriar], ignore_index=True)
                    
                    update(worksheet='tipoConta', data=dfUpdate)
                    st.success('Salvo com Sucesso')
                    getTipoConta()
                    tipos = dfUpdate
                    
            else:
                st.warning('Tipo inválido.')
                
    
    st.divider()
    st.subheader('Tipo cadastrados')
    st.table(tipos)
            