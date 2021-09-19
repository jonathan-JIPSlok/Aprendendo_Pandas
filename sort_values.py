import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

print(df.sort_values("Nome")) #Ordena a tabela port ordem alfabetica ou numerica
print()
print(df.sort_values("Idade"))
print()

df.sort_values("Idade", inplace=True)#Modifica a tabela para ordenado.
print(df)
print()

print(df.sort_values(["ID", "Idade"])) #Ordena mais de uma coluna
print()

print(df.sort_values("Idade", ascending=True)) #True para odenar de menor para maior e False de maior para menor
print()

print(df.sort_values(["Nome", "ID"], ascending=[True, False]))#Ordena as tabelas cada uma de uma forma