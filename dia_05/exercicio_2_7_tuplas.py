#%%
#faça um código que Solicite ao usuário o nome de uma fruta e exiba o preço correspondente.
#Maçã: R$1,50
#Banana: R$2,75
#Uva: R$1,90
#Pera: R$1,25
#Laranja: R$0,65
#Limão: R$1,25
#Goiaba: R$2,15
#Abacaxi: R$3,20
#Jaca: R$5,80
# Utilize tuplas para armazenar os nomes e preços das frutas.
# Criação de tuplas com os nomes e preços das frutas
frutas = (    ("Maçã", 1.50),
             ("Banana", 2.75), 
             ("Uva", 1.90), 
             ("Pera", 1.25), 
             ("Laranja", 0.65), 
             ("Limão", 1.25), 
             ("Goiaba", 2.15), 
             ("Abacaxi", 3.20), 
             ("Jaca", 5.80))
# Solicita ao usuário o nome da fruta
fruta_usuario = input("Digite o nome da fruta: ").strip().capitalize()
# Procura a fruta na tupla e exibe o preço correspondente
for fruta, preco in frutas:
    if fruta == fruta_usuario:
        print(f"O preço da {fruta} é R${preco:.2f}")
        break
else:
    print("Fruta não encontrada. Por favor, verifique o nome digitado.")
# Fim do código