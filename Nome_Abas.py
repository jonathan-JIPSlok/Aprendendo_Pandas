import pandas as pd
import openpyxl

df = pd.ExcelFile("Excel/Arquivo.xlsx", engine="openpyxl")
#sheet_names -> mostra o nome das abas
print(df.sheet_names)

#parse() -> seleciona a aba da planilah que ira usar
df = df.parse("Planilha1")
print(df.head())