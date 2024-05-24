import streamlit as st
import pandas as pd
from main import update, consultaContas

def create():

    contas = st.session_state['contas']
    tipos = st.session_state['tipoConta']
    contasFixas = st.session_state['contasFixas']
    
    with st.form('formCriarConta'):
        conta = st.selectbox('Conta', options=tipos)
        
        col1, col2, col3 = st.columns([2, 1, 1])
        
        vencimento = col1.date_input('Data vencimento', format='DD/MM/YYYY')
        valor = col2.number_input('Valor')
        tipo = col3.selectbox('Tipo', options=['Fixa', 'Variável'])
        
        btnCriar = st.form_submit_button('Confirmar')
        
        if btnCriar:
            if conta and vencimento and valor:
               if tipo == 'Variável':
                   
                    contaCriar = pd.DataFrame([
                        {
                            'conta': conta,
                            'vencimento': vencimento,
                            'pago': 0,
                            'valor': float(valor),
                            'tipo': tipo
                        }
                    ])
                    
                    dfUpdate = pd.concat([contas, contaCriar], ignore_index=True)
                    update(worksheet='contas', data=dfUpdate)
                    
                    st.success('Salvo com sucesso.')
                    
                    st.session_state['contas'] = dfUpdate
               
               if tipo == 'Fixa':
                   
                   contaExiste = contasFixas[contasFixas['conta'] == conta]
                   if len(contaExiste) > 1:
                       st.warning('Essa conta já existe')
                       
                   else:
                   
                        contaCriar = pd.DataFrame([
                             {
                                 'conta': conta,
                                 'vencimento': vencimento,
                                 'valor': float(valor),
                                 'tipo': tipo
                             }
                         ])

                        dfUpdateContasFixas = pd.concat([contasFixas, contaCriar], ignore_index=True)

                        update(worksheet='contaFixa', data=dfUpdateContasFixas)
                        st.session_state['contasFixas'] = dfUpdateContasFixas
               
               consultaContas()
                
                
            else:
                st.warning('Algum campo está vazio.')
        