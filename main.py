import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

def login() -> None:
    dadosLogin = conn.read(worksheet='usuario', usecols=list(range(4)), ttl=0)
    st.session_state['usuarios'] = dadosLogin.dropna()
    
def logsLogin() -> None:
    logs = conn.read(worksheet='logsLogin', usecols=list(range(2)), ttl=0)
    st.session_state['logsLogin'] = logs.dropna()

def getRoles() -> None:
    roles = conn.read(worksheet='roleUsuario', usecols=list(range(1)), ttl=0)
    st.session_state['roles'] = roles.dropna()

def consultaFuncionarios() -> None:
    funcionarios = conn.read(worksheet='funcionario', usecols=list(range(5)), ttl=0)
    funcionarios['cpf'] = funcionarios['cpf'].apply(lambda x: str(x).replace(',', '').replace('.', ''))
    funcionarios['cpf'] = funcionarios['cpf'].apply(lambda x: x[:-1] if len(x) > 11 else x)
    
    st.session_state['funcionarios'] = funcionarios.dropna()
    
def getCargos() -> None:
    cargos = conn.read(worksheet='cargo', usecols=list(range(1)), ttl=0)
    st.session_state['cargos'] = cargos.dropna()
    
def getDepartamentos() -> None:
    departamentos = conn.read(worksheet='departamento', usecols=list(range(1)), ttl=0)
    st.session_state['departamentos'] = departamentos.dropna()
    
def consultaContas() -> None:
    contas = conn.read(worksheet='contas', usecols=list(range(5)), ttl=0)
    st.session_state['contas'] = contas.dropna()
    
def getContasFixas() -> None:
    contas = conn.read(worksheet='contaFixa', usecols=list(range(4)), ttl=0)
    st.session_state['contasFixas'] = contas.dropna()
    
def getTipoConta() -> None:
    tipoConta = conn.read(worksheet='tipoConta', usecols=list(range(1)), ttl=0)
    st.session_state['tipoConta'] = tipoConta.dropna()

def getCaixa() -> None:
    caixa = conn.read(worksheet='caixa', usecols=list(range(2)), ttl=0)
    st.session_state['caixa'] = caixa.dropna()
    
def getMovimentacoesCaixa() -> None:
    movimentacoes = conn.read(worksheet='movimentacaoCaixa', usecols=list(range(4)), ttl=0)
    st.session_state['movimentacoesCaixa'] = movimentacoes.dropna()

def getCategoriasCaixa() -> None:
    categorias = conn.read(worksheet='categoriaMovCaixa', usecols=list(range(1)), ttl=0)
    st.session_state['categoriasCaixa'] = categorias.dropna()

def update(worksheet: str, data: pd.DataFrame, spreadUrl: str | None = None) -> None:
    """
       Função para fazer qualquer alteração nos dados da planilha.
    """
    
    if spreadUrl != None:
        conn.update(worksheet=worksheet, data=data, spreadsheet=spreadUrl)
    else:
        conn.update(worksheet=worksheet, data=data)