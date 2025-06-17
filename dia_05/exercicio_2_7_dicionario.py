#%%
# #faça um código que Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
#Maçã: R$1,50
#Banana: R$2,75
#Uva: R$1,90
#Pera: R$1,25
#Laranja: R$0,65
#Limão: R$1,25
#Goiaba: R$2,15
#Abacaxi: R$3,20
#Jaca: R$5,80

# Utilize dicionario para armazenar os nomes e preços das frutas.
# Criação de dicionário com os nomes e preços das frutas
frutas = {
    "Maçã": 1.50,
    "Banana": 2.75,
    "Uva": 1.90,
    "Pera": 1.25,
    "Laranja": 0.65,
    "Limão": 1.25,
    "Goiaba": 2.15,
    "Abacaxi": 3.20,
    "Jaca": 5.80
}

# Solicita ao usuário o nome da fruta
fruta_usuario = input("Digite o nome da fruta: ").strip().capitalize()


#print(frutas[fruta_usuario]) # forma simples de exibir o preço


# Exibe o preço correspondente ou uma mensagem de erro
preco = frutas.get(fruta_usuario)
if preco is not None:
    print(f"O preço da {fruta_usuario} é R${preco:.2f}")
else:
    print("Fruta não encontrada. Por favor, verifique o nome digitado.")

# Fim do código