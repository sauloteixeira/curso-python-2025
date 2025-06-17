#%%
lista = [2, 132, "saulo", ["ds", "de", "da"], True]
lista[2]

#%%

dicionario = {
    "nome": "Saulo",
    "idade": 52,
    "altura": 1.68,
    "habilidades": ["Python", "JavaScript", "SQL"],
    "ativo": True,
    "endereco": {
        "rua": "Av. Bernando Vieira de Melo",
        "numero": 100,
        "cidade": "Jaboatão dos Guararapes",
        "estado": "PE"        
    },
    "cargos": [
        {"nome": "Analista de Sistemas", "nivel": "Júnior"},
        {"nome": "Desenvolvedor", "nivel": "Pleno"},
        {"nome": "Gerente de Projetos", "nivel": "Sênior"},
    ]
}

print(dicionario["cargos"][-1]["nivel"])
#%%
print(dicionario)
print(dicionario["nome"])
print(dicionario["habilidades"][-1])
print(dicionario["endereco"]["cidade"])
# Adicionando um novo item ao dicionário
dicionario["email"] = "saulo@gmail.com"
print(dicionario["email"])
# Atualizando um valor existente
dicionario["idade"] = 53
print(dicionario["idade"])
# Removendo um item do dicionário
del dicionario["ativo"]
print(dicionario)

#%%

dicionario["cargos"][0]["nivel"]

dicionario.keys()  # Retorna as chaves do dicionário
dicionario.values()  # Retorna os valores do dicionário
dicionario.items()  # Retorna os pares chave-valor do dicionário

#%%

for i in dicionario:
    print(i, ":", dicionario[i])

print()

for chave, valor in dicionario.items():
    print(chave, ":", valor)