

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

import matplotlib.pyplot as plt
import mysql.connector
import openpyxl
import seaborn as sns

st.set_page_config(layout="wide")


def main():

    ####Desabilitar tela de login
    #st.session_state['logged_in'] = True
    ####
    
    # Verificar se o usuário está logado
    if not is_user_logged_in():
        show_login_page()
    else:
        run_main_program()

def is_user_logged_in():
    # Verificar se o usuário está logado
    return st.session_state.get('logged_in', False)

def show_login_page():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    login_button = st.button("Login")

    if login_button:
        if username == "1234" and password == "1234":
            st.session_state['logged_in'] = True
            st.experimental_rerun()  # Re-executar o aplicativo para atualizar a tela
        else:
            st.error("Invalid username or password")

def run_main_program():
    st.title("Logado")

if __name__ == "__main__":
    main()


st.title("ola meu jovem")
st.write("ola meu jovem")


file_path = r"C:\Users\14670987607\Downloads\dados.xlsx"

df = pd.read_excel(file_path)

with st.sidebar:
	linhas = st.slider("Quantidade de linhas", 1, 20)

col1, col2 = st.columns(2)
with col1:
    st.write(df)
        
with col2:
    st.write(df.head(linhas))



