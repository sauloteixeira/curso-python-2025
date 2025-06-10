#%%
# Escreva um programa que receba uma lista de números do usuário e conte quantas vezes um número específico aparece na lista. Solicite ao usuário um número e exiba a contagem.
# Solicita ao usuário uma lista de números
numeros = input("Digite uma lista de números separados por espaço: ").split()
print("Lista de números:", numeros)

# Converte a lista de strings para uma lista de inteiros
numeros = [int(num) for num in numeros]
print("Lista de números convertida:", numeros)

# Solicita ao usuário um número para contar
numero_especifico = int(input("Digite o número que deseja contar: "))

# Conta quantas vezes o número específico aparece na lista
contagem = numeros.count(numero_especifico)

# Exibe a contagem
print(f"O número {numero_especifico} aparece {contagem} vezes na lista.")

