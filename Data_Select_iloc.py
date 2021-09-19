import pandas as pd
import openpyxl

df = pd.read_excel("Arquivo.xlsx", engine="openpyxl")

print(df.iloc[2]) # Seleciona a 2 linha
print()

print(df.iloc[2:6]) #Seleciona da 2 linha até a 5
print()

print(df.iloc[2:6, 2]) #Seleciona da 2 linha até a 5 da coluna 2
print()

print(df.iloc[2:6, 1:3]) #Seleciona da 2 linha até a 5 e da 1 coluna até a 2
print()

print(df.iloc[[3, 5], [0, 2]]) #Seleciona a 3 e 5 linha da 1 e 3 coluna