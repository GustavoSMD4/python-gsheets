import streamlit as st
import pandas as pd
from main import update

def movimetacao():
    
    movimentacoes = st.session_state['movimentacoesCaixa']
    caixa = st.session_state['caixa']
    categorias = st.session_state['categoriasCaixa']
    
    with st.popover('Nova movimentação'):
        with st.form('formMovimentacao', border=False, clear_on_submit=True):
            st.subheader('Movimentação')
            
            col1, col2 = st.columns([3, 1])
            
            descricao = col1.text_input('Descrição', autocomplete='off').rstrip().upper()
            
            data = col2.date_input('Data', format='DD/MM/YYYY')
            
            col3, col4, col5 = st.columns([1, 1, 2])
            
            valor = col3.number_input('Valor')
                        
            tipo = col4.selectbox('Tipo', options=['Entrada', 'Saída'])
            
            categoria = col5.selectbox('Categoria', options=categorias['descricao'])

            btnSalvar = st.form_submit_button('Salvar')
            
            if btnSalvar:
                try:
                    if descricao and data and valor and tipo:
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
                        
                except Exception as e:
                    st.warning(e)
                
    