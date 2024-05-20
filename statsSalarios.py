import streamlit as st
import plotly_express as px

def statsSalarios():
    
    funcionarios = st.session_state['funcionarios']
    
    funcionarioDisplay = funcionarios
    funcionarioDisplay['Salário formatado'] = funcionarioDisplay['Salário'].apply(lambda x: F"R${x:,.2f}")
    
    figBar = px.bar(funcionarios, x='Nome', y='Salário', title='Salários funcionários', text='Salário formatado')
    st.plotly_chart(figBar, use_container_width=True)