import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

def login():
    dadosLogin = conn.read(worksheet='usuario', usecols=list(range(4)), ttl=0)
    st.session_state['usuarios'] = dadosLogin.dropna()
    
def logsLogin():
    logs = conn.read(worksheet='logsLogin', usecols=list(range(2)), ttl=0)
    st.session_state['logsLogin'] = logs.dropna()

def getRoles():
    roles = conn.read(worksheet='roleUsuario', usecols=list(range(1)), ttl=0)
    st.session_state['roles'] = roles.dropna()

def consultaFuncionarios():
    funcionarios = conn.read(worksheet='funcionario', usecols=list(range(5)), ttl=0)
    funcionarios['cpf'] = funcionarios['cpf'].apply(lambda x: str(x).replace(',', '').replace('.', ''))
    funcionarios['cpf'] = funcionarios['cpf'].apply(lambda x: x[:-1] if len(x) > 11 else x)
    
    st.session_state['funcionarios'] = funcionarios.dropna()
    
def getCargos():
    cargos = conn.read(worksheet='cargo', usecols=list(range(1)), ttl=0)
    st.session_state['cargos'] = cargos.dropna()
    
def getDepartamentos():
    departamentos = conn.read(worksheet='departamento', usecols=list(range(1)), ttl=0)
    st.session_state['departamentos'] = departamentos.dropna()
    
def consultaContas():
    contas = conn.read(worksheet='contas', usecols=list(range(5)), ttl=0)
    st.session_state['contas'] = contas.dropna()
    
def getContasFixas():
    contas = conn.read(worksheet='contaFixa', usecols=list(range(4)), ttl=0)
    st.session_state['contasFixas'] = contas.dropna()
    
def getTipoConta():
    tipoConta = conn.read(worksheet='tipoConta', usecols=list(range(1)), ttl=0)
    st.session_state['tipoConta'] = tipoConta.dropna()

def update(worksheet, data, spreadUrl=None):
    if spreadUrl != None:
        conn.update(worksheet=worksheet, data=data, spreadsheet=spreadUrl)
    else:
        conn.update(worksheet=worksheet, data=data)