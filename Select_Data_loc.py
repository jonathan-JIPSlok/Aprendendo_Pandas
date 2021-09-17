import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

print(df.loc[0])#Seleciona a linha
print()

print(df.loc[0:4])#Seleciona mais de uma linha
print()

print(df.loc[[0, 3, 5]])#Seleciona apenas as linhas 0, 3 e 5
print()

print(df.loc[3:6, "Nome"])#Seleciona da 3 linha até a sexta linha da coluna "Nome"
print()

print(df.loc[3:6, ["Nome", "Idade"]])#Seleciona tantas linhas das dias colunas
print()

print(df.loc[4:5, "Nome":"ID"]) #Seleciona tantas linhas de uma coluna até outra coluna
print()
