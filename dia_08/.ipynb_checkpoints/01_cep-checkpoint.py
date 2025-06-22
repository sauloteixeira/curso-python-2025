# -*- coding: utf-8 -*-
# Exemplo de requisição HTTP para obter informações de um CEP usando a API ViaCEP

import requests
import json
from tqdm import tqdm
import pandas as pd

ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "54430160",
    "19060100",
    "58038200",
    "54420310",
]
# Exemplo de requisição HTTP para obter informações de um CEP específico
# A API ViaCEP retorna informações como logradouro, bairro, cidade, estado, etc.
# A URL da API ViaCEP é: https://viacep.com.br/ws/{cep}/json/
    
url = "https://viacep.com.br/ws/{cep}/json/"

dados = []
for cep in tqdm(ceps):
    resposta = requests.get(url.format(cep=cep))
    if resposta.status_code == 200:
        dados.append(resposta.json())
    else:
        print(f"Erro ao buscar o CEP {cep}: {resposta.status_code}")

#print(dados)

with open("cep.json", "w", encoding="utf-8") as arquivo:
    json.dump(dados, arquivo, ensure_ascii=False, indent=4)

dataset = pd.DataFrame(dados)
dataset.to_csv("cep.csv", index=False, encoding="utf-8-sig")
# Carregar o DataFrame do arquivo CSV
dataset = pd.read_csv("cep.csv", encoding="utf-8-sig")
# Exibir o DataFrame
# print(dataset)
