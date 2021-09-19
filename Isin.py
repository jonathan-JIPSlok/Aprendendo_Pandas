import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

filtro = df.Nome.isin(["Jonathan", "Lucas"]) #Retorna uma lista logica com True nas linhas que tem os dados correspondentes
print(filtro)
print()

print(df.isin({"Nome":["Jonathan"], "Idade":[19, 20]})) #Faz a mesma coisa porem com mais dados
print()

print(df[(filtro)]) #Pegando valores da tablea usando a lista filtrada pelo isin de valores logicos
print()