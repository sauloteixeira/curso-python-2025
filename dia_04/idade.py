#%%

# Construa um programa que acumule idades digitadas pelo usuários, interrompendo quando a idade for em branco.
idades = []
while True:
    idade = input("Digite uma idade (ou deixe em branco para sair): ")
    if idade == "":
        break
    try:
        idade = int(idade)
        idades.append(idade)
    except ValueError:
        print("Por favor, digite um número válido.")

print("Idades acumuladas:", idades)
# Exibir a média das idades acumuladas
if idades:
    media_idades = sum(idades) / len(idades)
    print("Média das idades:", media_idades)

# Exibir a quantidade de idades acumuladas
print("Quantidade de idades acumuladas:", len(idades))
# Exibir a maior idade acumulada
if idades:
    maior_idade = max(idades)
    print("Maior idade acumulada:", maior_idade)

# Exibir a menor idade acumulada
if idades:
    menor_idade = min(idades)
    print("Menor idade acumulada:", menor_idade)


# Exibir a soma das idades acumuladas
soma_idades = sum(idades)
print("Soma das idades acumuladas:", soma_idades)
