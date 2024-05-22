import streamlit as st
import streamlit_shadcn_ui as ui
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode

def consulta():
    
    usuarios = st.session_state['usuarios']
    
    usuariosFiltrado = usuarios[['nome','usuario', 'role']]
    builder = GridOptionsBuilder.from_dataframe(usuariosFiltrado)
    builder.configure_selection(selection_mode='single', use_checkbox=True)
    go = builder.build()
    
    linhaSelecionada = AgGrid(usuariosFiltrado, fit_columns_on_grid_load=True, height=200,
                              gridOptions=go, update_mode=GridUpdateMode.SELECTION_CHANGED)
    
    st.write(linhaSelecionada['selected_rows'])