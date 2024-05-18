import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

def login():
    dadosLogin = conn.read(worksheet='login', usecols=list(range(2)))
    return dadosLogin.dropna()

def funcionarios():
    funcionarios = conn.read(worksheet='teste', usecols=list(range(6)))
    return funcionarios.dropna()

def update(data, worksheet, spread=None):
    conn.update(worksheet=worksheet, data=data)
