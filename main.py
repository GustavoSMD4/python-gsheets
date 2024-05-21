import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

def login():
    dadosLogin = conn.read(worksheet='login', usecols=list(range(4)), ttl=0)
    st.session_state['usuarios'] = dadosLogin.dropna()

def consultaFuncionarios():
    funcionarios = conn.read(worksheet='teste', usecols=list(range(5)), ttl=0)
    st.session_state['funcionarios'] = funcionarios.dropna()
    
def logsLogin():
    logs = conn.read(worksheet='logLogins', usecols=list(range(2)), ttl=0)
    st.session_state['logLogins'] = logs.dropna()

def update(worksheet, data, spreadUrl=None):
    if spreadUrl != None:
        conn.update(worksheet=worksheet, data=data, spreadsheet=spreadUrl)
    else:
        conn.update(worksheet=worksheet, data=data)