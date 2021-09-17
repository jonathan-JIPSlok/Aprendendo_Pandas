import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

print(df["Nome"].head())#Seleciona como se fosse uma lista
print()

print(df[["Nome", "Idade"]].head())#Seleciona mais de uma coluna
print()

print(df.ID.head())#Seleção por notação de ponto
print()

df["RG"] = 7241555 #Cria uma nova coluna
print(df.head())
