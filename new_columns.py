import pandas as pd

Clientes = pd.Series(["Jonathan", "Maikon", "Ronald"], name = "Clientes")
Contas = pd.Series([10, 20, 22.50], name = "Conta")

df = pd.DataFrame({Clientes.name: Clientes, Contas.name:Contas})
print(df)
print()

df["Total de Produtos"] = [1, 2, 2] #Adicionado tabelas no dataFrame
print(df)
print()

df = df.append({"Clientes":"Cristofer", "Conta":33, "Total de Produtos":3}, ignore_index = True) #Adiciona uma nova linha no DataFrame
print(df)
print()

print(df.loc[:, ["Clientes", "Conta"]]) #Seleciona usando loc