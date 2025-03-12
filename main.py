import pandas as pd

# selecionando os dados a partir do seu cabecalho
df = pd.read_excel("snx690_20250228132802.xls", header=7)

# convertendo a string em data e hora
df["Time"] = pd.to_datetime(df["Time"])

# separando a hora em uma nova coluna
df["Hour"] = df["Time"].dt.hour

# imprimindo apenas "Time" e "Hour"
print(df[["Time", "Hour"]].head())