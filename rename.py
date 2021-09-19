import pandas as pd

s1 = pd.Series([10, 20, 30], name="Total")
s2 = pd.Series(["Jonathan", "Maikao", "Ronald"], name="Clientes")

df = pd.DataFrame({s2.name: s2, s1.name: s1})
print(df)
print()

df = df.rename(columns = {"Total": "Conta"}) #Renomeia colunas do dataframe e retorna outro dataFrame
print(df)
print()

print(df.columns) #Retorna as colunas do DataFrame
print()

print(df.columns.to_list()) #Retorna as colunas em uma lista
print()