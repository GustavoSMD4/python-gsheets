import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode
from dateutil.relativedelta import relativedelta

def contasFixas():
    
    contasFixas = st.session_state['contasFixas']
    
    contasFixasFormatado = contasFixas[0:]
    
    
    builder = GridOptionsBuilder.from_dataframe(contasFixas)
    builder.configure_selection(use_checkbox=True, selection_mode='multiple')
    go = builder.build()
    
    linhaSelecionada = AgGrid(data=contasFixas, gridOptions=go, fit_columns_on_grid_load=True, height=300,
           header_checkbox_selection_filtered_only=True, update_mode=GridUpdateMode.SELECTION_CHANGED)
    
    linhaSelecionada = pd.DataFrame(linhaSelecionada['selected_rows'])
    
    linhaSelecionada['vencimento'] = pd.to_datetime(linhaSelecionada['vencimento'])
    
    contaAtualizada = linhaSelecionada[0:]
    
    contaAtualizada['vencimento'] = contaAtualizada['vencimento'] + pd.DateOffset(months=1)

    st.write(contaAtualizada)
    
    # df['date_plus_one_month'] = df['date'] + pd.DateOffset(months=1)