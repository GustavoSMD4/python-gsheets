import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

def consulta():
    
    contas = st.session_state['contas']
    
    contasFormatadas = contas[0:]
    
    # meses_em_portugues = {
    #     1: 'Janeiro',
    #     2: 'Fevereiro',
    #     3: 'Março',
    #     4: 'Abril',
    #     5: 'Maio',
    #     6: 'Junho',
    #     7: 'Julho',
    #     8: 'Agosto',
    #     9: 'Setembro',
    #     10: 'Outubro',
    #     11: 'Novembro',
    #     12: 'Dezembro'
    # }

    
    contasFormatadas['vencimento'] = pd.to_datetime(contasFormatadas['vencimento'])
    
    contasFormatadas['mes_ano'] = contasFormatadas['vencimento'].dt.strftime('%Y-%m')
    
    contasFormatadas['mes'] = contasFormatadas['vencimento'].dt.strftime('%m/%Y')
    contasFormatadas['Vencimento'] = contasFormatadas['vencimento'].dt.strftime('%d/%m/%Y')
    
    options = contasFormatadas['mes'].unique().tolist()
    options.sort(key=lambda x: pd.to_datetime(x, format='%m/%Y')) 
    options.insert(0, 'Todos')
    with st.form('formConsulta'):
        
        mes = st.selectbox('Filtrar por mês', options=options)
    
        btnFiltrar = st.form_submit_button('Filtrar')
        
        if btnFiltrar:
            
            contasFormatadas = contasFormatadas[0:]
            
            if mes != 'Todos':
                contasFormatadas = contasFormatadas[contasFormatadas['mes'] == mes]
            
    
    contasFormatadas['Valor'] = contasFormatadas['valor'].apply(lambda x: F"R${x:,.2f}")
    AgGrid(contasFormatadas[['conta', 'Vencimento', 'Valor']], height=300, fit_columns_on_grid_load=True)