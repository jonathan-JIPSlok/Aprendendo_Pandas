import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

a = df.Idade.apply(lambda x: str(x).replace("1", "2")) #Aplica funcoes dentro do dataFrame pode passar uma funcao ou fazer um lambda, retorna um novo objeto com o resultado da funcao
print(a)
print()

a = df[["Idade", "ID"]].applymap(lambda x: str(x).replace("1", "2")) #Faz a mesma coisa porem serve para mais de uma coluna
print(a)
print()