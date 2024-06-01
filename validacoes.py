import streamlit as st

def validarInputs(campos: tuple, tipos: tuple, nomesCampos: tuple[str]) -> None | ValueError:
    """Retornará ValueError se estiver algum campo inválido"""
    
    if not isinstance(campos, tuple) or not isinstance(tipos, tuple) or not isinstance(nomesCampos, tuple):
        raise ValueError('Todos os parâmetros precisam ser um tuple.')
    
    for i, campo in enumerate(campos):
        if not isinstance(campo, tipos[i]):
            raise ValueError(F"O campo {nomesCampos[i]} esperava o tipo {tipos[i]}, mas recebeu {type(campo)}.")

        elif campo == '':
            raise ValueError(F"O campo {nomesCampos[i]} está vazio.")