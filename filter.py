import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

print(df.filter(items = ["Nome", "ID"])) #Seleciona colunas
print()

print(df.filter(like="me")) #Seleciona coluna baseada em algumas letras que tenha no nome da coluna
print()

print(df.filter(regex = "N..e")) #Seleciona coluna com o regex