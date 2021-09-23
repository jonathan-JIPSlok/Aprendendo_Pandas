import pandas as pd
import numpy as np
import openpyxl

Data = pd.date_range("09/01/2021", periods = 30)

Vendas = pd.Series(["R$700,00", "R$450,00", "R$1.345,00", "R$789,00", "R$809,00",
                                    "R$605,00", "R$2.034,00", "R$784,00", "R$600,00", "R$606,00",
                                    "R$809,00", "R$500,00", "R$550,00", "R$450,00", "R$1.507,00",
                                    "R$700,00", "R$450,00", "R$1.345,00", "R$789,00", "R$809,00",
                                    "R$605,00", "R$2.034,00", "R$784,00", "R$600,00", "R$606,00",
                                    "R$809,00", "R$500,00", "R$550,00", "R$450,00", "R$1.507,00"])

Vendas_Cartao = pd.Series(["R$350,00", "R$113,00", "R$587,00", "R$529,00", "R$598,00",
                                                   "R$401,00", "R$1.150,00", "R$578,00", "R$450,00", "R$236,00",
                                                   "R$307,00", "R$378,00", "R$230,00", "R$157,00", "R$890,00",
                                                   "R$376,00", "R$98,00", "R$693,00", "R$508,00", "R$600,00",
                                                   "R$205,00", "R$1.008,00", "R$597,00", "R$425,00", "R$159,00",
                                                   "R$589,00", "R$360,00", "R$160,00", "R$250,00", "R$1.000,00"])

def Rs(x):
    x = str(x)
    x1 = ""
    cont = 0
    for num in x:
        if len(x) >= 6:
            if cont == 1:
                x1 += "."
        if num == "." and cont > 2:
            x1 += ","
        else:
            x1 += num
        cont += 1
    return x1

Vendas_Dinheiro = Vendas.apply(lambda x: x.replace("R$", "").replace(".", "").replace(",", ".")).astype(np.float16) - Vendas_Cartao.apply(lambda x: x.replace("R$", "").replace(".", "").replace(",", ".")).astype(np.float16)
Vendas_Dinheiro = Vendas_Dinheiro.astype("object").apply(Rs).apply(lambda x: f"R${x}")

print(pd.DataFrame({"Data":Data, "Vendas":Vendas, "Vendas no Cartão":Vendas_Cartao, "Vendas no Dinheiro": Vendas_Dinheiro}))