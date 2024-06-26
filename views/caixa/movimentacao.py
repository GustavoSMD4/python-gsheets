import streamlit as st
import pandas as pd
from main import update
from datetime import datetime
from validacoes import validarInputs

def movimetacao():
    
    movimentacoes = st.session_state['movimentacoesCaixa']
    caixa = st.session_state['caixa']
    categorias = st.session_state['categoriasCaixa']
    
    with st.popover('Nova movimentação'):
        with st.container(border=False):
            st.subheader('Movimentação')
            
            col1, col2 = st.columns([3, 1])
            
            descricao = col1.text_input('Descrição', autocomplete='off').rstrip().upper()
            
            data = col2.date_input('Data', format='DD/MM/YYYY')
            
            col3, col4, col5 = st.columns([1, 1.5, 1.5])
            
            valor = col3.number_input('Valor')
                        
            tipo = col4.selectbox('Tipo', options=['Entrada', 'Saída'])
            
            categoria = col5.selectbox('Categoria', options=categorias['descricao'])

            btnSalvar = st.button('Salvar')
            
            if btnSalvar:
                try:
                    validarInputs((descricao, data, valor, tipo, categoria),
                                  (str, datetime.date, float, str, str),
                              ('Descrição', 'Data', 'Valor', 'Tipo', 'Categoria'))
                    
                    if tipo == 'Saída':
                        valor = valor * -1
                        
                    movimentacaoCriar = pd.DataFrame([
                        {
                            'descricao': descricao,
                            'data': data,
                            'valor': valor,
                            'tipo': tipo,
                            'categoria': 'ENTRADA' if tipo == 'Entrada' else categoria
                        }
                    ])
                    
                    dfUpdate = pd.concat([movimentacoes, movimentacaoCriar], ignore_index=True)
                    
                    update(worksheet='movimentacaoCaixa', data=dfUpdate)
                    st.session_state['movimentacoesCaixa'] = dfUpdate
                    
                    caixa['saldo'] = caixa['saldo'] + valor
                    
                    update(worksheet='caixa', data=caixa)
                    st.session_state['caixa'] = caixa
                    st.rerun()
                        
                except ValueError as e:
                    st.warning(e)
                
    