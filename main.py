#na parte prática usaremos apenas as 3 linhas em destaque, mas o programa completo usa todos


import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

import matplotlib.pyplot as plt
import mysql.connector
import openpyxl
import seaborn as sns

st.set_page_config(layout="wide")

st.title("Titulo")
st.write("Texto")


file_path = r"C:\Users\14670987607\Downloads\dados.xlsx"

df = pd.read_excel(file_path)

