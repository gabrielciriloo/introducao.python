import pandas as pd

# 1-Importando Dados
data = pd.read_excel("data/VendaCarros.xlsx")
print(data)

# 2-Listando os primeiros registros
print("\nRegistros Iniciais: \n", data.head())

# 3-Listando os ultimos registros
print("\nUltimos Registros: \n", data.tail())

# 4-Contando valores por fabricante
print("\nValores por fabricante: \n", data["Fabricante"].value_counts)
