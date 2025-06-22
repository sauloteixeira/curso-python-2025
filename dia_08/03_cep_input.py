#%%
import requests

cep = input("Digite o CEP: ")
url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url.format(cep=cep))

if resposta.status_code == 200:
    dados = resposta.json()
 
    for chave, valor in dados.items():
        print(f"{chave.capitalize()}: {valor}")
else:
    print("Erro ao consultar o CEP. Verifique se o CEP está correto.")

# %%
    

# if resposta.status_code == 200:
#     dados = resposta.json()
#     if "erro" not in dados:
#         print(f"CEP: {dados['cep']}")
#         print(f"Logradouro: {dados['logradouro']}")
#         print(f"Bairro: {dados['bairro']}")
#         print(f"Cidade: {dados['localidade']}")
#         print(f"Estado: {dados['uf']}")
#     else:
#         print("CEP não encontrado.")

