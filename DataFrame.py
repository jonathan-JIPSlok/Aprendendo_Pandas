import pandas as pd

S1 = pd.Series([19, 20, 30], name="s1")
S2 = pd.Series([22, 17, 26], name="s2")

print(pd.DataFrame([S1, S2])) #Criando uma tabela com as Series
print()

print(pd.DataFrame({S1.name: S1, S2.name: S2})) #Criando uma tabela com as series e fazendo cada uma ser uma coluna
print()

p = pd.DataFrame({S1.name: S1, S2.name: S2})
p["S3"] = [20, 30, 20] #Adicionando uma nova tabela ao dataFrame
print(p)
print()

p["Soma"] = S1 + S2 #Adicionando uma nova tavela com a soma de outeas duas
print(p)
print()

p.insert(2, "invasor", [6, 7, 8]) #Insere uma nova coluna no 2 lugar como foi passado
print(p)
print()

del p["invasor"] #Apaga uma coluna pra sempre
print(p)
print()

p.insert(2, "invasor", [6, 7, 8])
a = p.pop("invasor") #Tira a coluna do dataframe e retorna para outro lugar que queira como esta variavel
print(p)
print()

print(a)
print()