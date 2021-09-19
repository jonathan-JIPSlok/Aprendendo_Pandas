import pandas as pd
import numpy as np

print(pd.Series([11, 20, 30, 20, 30, 30, 20])) #Cria uma coluna com os dados desta lista
print()

print(pd.Series([10, 20, 30, 33], index=["a", "b", "c", "d"])) #Cria uma tabela com a lista e os indices viram alfabeticos.
print()

print(pd.Series(np.random.randn(3), ["a", "b", "c"])) #Cria tez valores aleatoriod com numpy e torna os indices alfabeticos
print()

S = pd.Series({0: 10, 1: 20.3, 2: 30})#Cria uma coluna atravez de dicionario
print(S) 
print(S[0]) #Pega apenas a linha que o indice é 0
print(S[0:2]) #Pega as linhas de indice 0 até 2
print()

print(pd.Series([0, 10, 20], name="Num")) #Cria uma tabela com nome
print()

S = pd.Series([10, 20, 30], name="Num")
print(S.to_numpy()) #Tranforma em um array do numpy
print()

S1 = pd.Series([33, 1, 22])
print(S + S1) #Da para fazer qualquer operacao matematica
print()
