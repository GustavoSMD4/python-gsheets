import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

conn = st.connection("gsheets", type=GSheetsConnection)

def login():
    dadosLogin = conn.read(worksheet='login', usecols=list(range(2)), ttl=0)
    st.session_state['usuarios'] = dadosLogin.dropna()

def funcionarios():
    funcionarios = conn.read(worksheet='teste', usecols=list(range(6)), ttl=0)
    st.session_state['funcionarios'] = funcionarios.dropna()

def update(data, worksheet, spread=None):
    conn.update(worksheet=worksheet, data=data)
