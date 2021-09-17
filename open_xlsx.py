import pandas as pd
import openpyxl

"""
Pandas perdeu suporte para arquivos xlsx por isso usamos o openpyxl
engine -> motor de busca, usamos o openpyxl
sheet_name -> para especificar qual aba usaremos
"""
df = pd.read_excel("Excel/Arquivo.xlsx", engine="openpyxl", sheet_name=0)
print(df.head())