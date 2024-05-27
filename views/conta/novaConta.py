import streamlit as st
import pandas as pd
from main import update, consultaContas

def create():

    contas = st.session_state['contas']
    tipos = st.session_state['tipoConta']
    contasFixas = st.session_state['contasFixas']
    
    with st.container(border=True):
        
        col1, col2 = st.columns([1, 3])
        
        tipo = col1.selectbox('Tipo', options=['Fixa', 'Variável'])
    
        with col2:
            if tipo == 'Fixa':
                conta = st.selectbox('Conta', options=tipos['tipo'])
            elif tipo == 'Variável':
                conta = st.text_input('Conta', autocomplete='off').rstrip().upper()
        
        col3, col4 = st.columns(2)
        
        vencimento = col3.date_input('Data vencimento', format='DD/MM/YYYY')
        valor = col4.number_input('Valor')
        
        
        btnCriar = st.button('Confirmar')
        
        if btnCriar:
            if conta and vencimento and valor:
                
               vencimento = vencimento.strftime('%d/%m/%Y')
                
               if tipo == 'Variável':
                   
                    contaCriar = pd.DataFrame([
                        {
                            'conta': conta,
                            'vencimento': vencimento,
                            'pago': 1,
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
                        st.success('Salvo com sucesso.')
                        st.session_state['contasFixas'] = dfUpdateContasFixas

                
                
            else:
                st.warning('Algum campo está vazio.')
        