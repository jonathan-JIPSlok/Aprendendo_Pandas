import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

print(df.loc[[True, False, False, True, True, True, False], [True, False, False]]) #Mostra apenas linhas e colunas que estão True na lista passada
print()

print(df.Nome == "Jonathan") #Retorna uma lista de True e False com True apenas nas linhas que correspondem ao que foi passado
print()

print(df[df.Idade == 19]) #Retorna as linhas em que o valor foi igual ao valor passado
print()

print(df[(df.Nome == "Lucas") | (df.Idade == 19)]) #Retorna as linhas em que Nome for igual a lucas ou idade for igual a 19
print()

