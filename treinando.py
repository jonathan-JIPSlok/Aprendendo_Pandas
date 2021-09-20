import pandas as pd
import numpy as np

print(pd.DataFrame(np.random.randn(3, 3), index = range(0, 3), columns = [*"ABC"]))
print()

datas = pd.date_range("20/09/2021", periods = 30) #Gerador de Datas do pandas
print(datas)
print()

df = pd.DataFrame(np.random.randn(30, 3), index = datas, columns = [*"ABC"])
print(df)
print()

df.columns = ["Valor1", "Valor2", "Valor3"] #Substitui as colunas
print(df)
print()

df.index = range(1, 31) #Substitui os indices
print(df)
print()

print(df.sample(n= 5)) #Volta numeros aleatorios
print()

print(df.sample(n=5, random_state = 300)) #Volta valores aleatorios gerados pela semente 300 que serao sempre os mesnos valores
print()

print(df.Valor1.value_counts()) #Mostra quantos dados da coluna sao iguais
print()

#print(df.to_excel("New_xlsx_Data.xlsx", index = False)) #Exporta o arquivo xlsx
#print()

print(df.info()) #Mostra as informacoes da coluna
print()

print(df.describe().T) #Mostra uma descricao das colunas
print()

print(df.describe(percentiles = [0.25, 0.50, 0.75, 0.89]).T) #Mostra uma descricao das colunas com as porcentagens passadas aki
print()