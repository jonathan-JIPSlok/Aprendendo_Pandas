import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

print(f"Soma:\t {df.Idade.sum()}") #Faz a soma dos valores desta tabela
print(f"Media:\t {df.Idade.mean()}") #Calcula a media dos valores
print(f"Menor:\t {df.Idade.min()}") #pega o Menor valor da tabela
print(f"Maior:\t {df.Idade.max()}") #Pega o maior valor da tabela
print()

print(df[["Nome", "Idade"]].groupby(["Idade"]).sum()) #Agrupa os valores exemplo, todos de 15 anos estarao juntos, todos de 30 anos estarao juntos etc...
print()
