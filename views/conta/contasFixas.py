import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from dateutil.relativedelta import relativedelta
from main import update

def contasFixas():
    
    contasFixas = st.session_state['contasFixas']
    contas = st.session_state['contas']
    
    contasFixasFormatado = contasFixas[0:]
    
    if 'linhaSelecionada' not in st.session_state:
           st.session_state['linhaSelecionada'] = False
    
    contasFixasFormatado.drop(columns=['tipo'], inplace=True)
    
    builder = GridOptionsBuilder.from_dataframe(contasFixasFormatado)
    builder.configure_selection(use_checkbox=True, selection_mode='multiple')
    builder.configure_column('valor', editable=True)
    go = builder.build()
    
    with st.container(border=True):
       col1, col2 = st.columns([1, 3])
       
       operacao = col1.radio('Operação', options=['Editar', 'Pagar'])
       btnSalvarAlterações = st.button('Salvar')
       
       with col2:
                 linhaSelecionada = AgGrid(data=contasFixasFormatado, gridOptions=go, fit_columns_on_grid_load=True, height=300,
                               header_checkbox_selection_filtered_only=True, update_mode=GridUpdateMode.SELECTION_CHANGED)
       
       if st.session_state['linhaSelecionada'] == False:
              try: 
                       
                 linhaSelecionada = pd.DataFrame(linhaSelecionada['selected_rows'])
                 
                 if operacao == 'Pagar' and btnSalvarAlterações == True:
                        linhaSelecionada['vencimento'] = pd.to_datetime(linhaSelecionada['vencimento'])
       
                        contaAtualizada = linhaSelecionada[0:]
       
                        contaAtualizada['vencimento'] = contaAtualizada['vencimento'] + pd.DateOffset(months=1)
                        contaAtualizada['vencimento'] = contaAtualizada['vencimento'].dt.strftime('%Y/%m/%d')
                        
                        contaPaga = linhaSelecionada.copy()
                        contaPaga['pago'] = 1
                        contaPaga['tipo'] = 'Fixa'
                        
                        dfUpdateContas = pd.concat([contas, contaPaga])
                        contas = dfUpdateContas
                        update(worksheet='contas', data=dfUpdateContas)
                        
                        for index, row in linhaSelecionada.iterrows():
                               contasFixas.loc[contasFixas['conta'] == row['conta'], ['vencimento', 'valor', 'tipo']] = [
                               contaAtualizada.loc[index, 'vencimento'],
                               contaAtualizada.loc[index, 'valor'],
                               'Fixa' ]
                               
                        update(worksheet='contaFixa', data=contasFixas)
                        st.rerun()
                        
                 elif operacao == 'Editar' and btnSalvarAlterações == True:
                     
                        for index, row in linhaSelecionada.iterrows():
                               contasFixas.loc[contasFixas['conta'] == row['conta'], 
                                               ['valor']] = [linhaSelecionada.loc[index, 'valor']]
                        
                        
                        update(worksheet='contaFixa', data=contasFixas)
                        
                               
              except Exception:
                 return
       