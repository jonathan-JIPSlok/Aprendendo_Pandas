import pandas as pd
"""
encoding -> como foi escrito o arquivo
sep -> separador de colunas
"""
df = pd.read_csv("CSV/Arquivo_csv.csv", encoding="UTF-8", sep=";")

"""
head() ->  le 5 linhas por padrao, pode set passado mais linhas como parametro
shape -> mostra o total de linhas e colunas do arquivo
"""
print(df.head())
print(f"Total de {df.shape[0]} linhas e {df.shape[1]} colunas")