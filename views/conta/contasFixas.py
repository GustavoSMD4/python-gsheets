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
    
    operacao = st.radio('Operação', options=['Editar', 'Pagar'])
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)    
    btnSalvarAlterações = st.button('Salvar')
    
    linhaSelecionada = AgGrid(data=contasFixasFormatado, gridOptions=go, fit_columns_on_grid_load=True, height=300,
                            header_checkbox_selection_filtered_only=True, update_mode=GridUpdateMode.SELECTION_CHANGED)
    
    if st.session_state['linhaSelecionada'] == False:
           try: 
                    
              linhaSelecionada = pd.DataFrame(linhaSelecionada['selected_rows'])
              
              if operacao == 'Pagar' and btnSalvarAlterações == True:
                     linhaSelecionada['vencimento'] = pd.to_datetime(linhaSelecionada['vencimento'])

                     contaAtualizada = linhaSelecionada[0:]

                     contaAtualizada['vencimento'] = contaAtualizada['vencimento'] + pd.DateOffset(months=1)
                     
                     # conta	vencimento	pago	valor	tipo
                     contaPaga = pd.DataFrame([
                            {
                                   'conta': linhaSelecionada['conta'],
                                   'vencimento': linhaSelecionada['vencimento'],
                                   'pago': 1,
                                   'valor': linhaSelecionada['valor'],
                                   'tipo': 'Fixa'
                            }
                     ])
                     
                     dfUpdateContas = pd.concat([contas, contaPaga])
                     update(worksheet='contas', data=dfUpdateContas)
                     
                     atualizarVencimento = pd.DataFrame([
                            # conta	vencimento	valor	tipo
                            {
                                   'conta': contaAtualizada['conta'],
                                   'vencimento': contaAtualizada['vencimento'],
                                   'valor': contaAtualizada['valor'],
                                   'tipo': 'Fixa'
                            }
                     ])
                     
                     contasFixas.loc[contasFixas['conta'] == linhaSelecionada['conta'],
                                     ['conta', 'vencimento', 'valor',' tipo']] = [contaAtualizada['conta'],
                                                                                  contaAtualizada['vencimento'],
                                                                                  contaAtualizada['valor'],
                                                                                  'Fixa']
                     update(worksheet='contaFixa', data=contasFixas)
                     st.rerun()
                     
              elif operacao == 'Editar':
                     st.write('editar')
       
                            
           except Exception:
              return
