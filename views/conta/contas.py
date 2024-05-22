import streamlit as st

def consulta():
    
    contas = st.session_state['contas']
    
    options = contas['vencimento'].unique().tolist()
    options.insert(0, 'Todos')
    
    with st.form('formConsulta'):
        
        col1, col2 = st.columns(2)
        mes = col1.selectbox('Mês', options=options)
        status = col2.selectbox('Situação', options=['Todos', 'Pago', 'Pendente'])
    
        btnFiltrar = st.form_submit_button('Filtrar')
        
        if btnFiltrar:
            
            contasFiltradas = contas[0:]
            if status != 'Todos':
                status = 0 if status == 'Pendente' else 1
                contasFiltradas = contasFiltradas[contasFiltradas['pago'] == status]
            
            if mes != 'Todos':
                contasFiltradas = contasFiltradas[contasFiltradas['vencimento'] == mes]
            
            st.table(contasFiltradas)
        if not btnFiltrar:
            st.table(contas)