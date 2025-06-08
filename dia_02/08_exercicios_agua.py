#%%
# Programa para vender garrafa de água considerando a quantidade

texto = """ 
Escolha o tipo de água:
1 - Água mineral natural (R$1,50)
2 - Água mineral com gás (R$2,50)
"""

opcao = input(texto)

if opcao == "1":
    preco = 1.50
    tipo = "água mineral natural"
elif opcao == "2":
    preco = 2.50
    tipo = "água mineral com gás"
else:
    print("Opção inválida.")
    preco = None

if preco is not None:
    quantidade = int(input("Digite a quantidade de garrafas: "))
    total = preco * quantidade
    print(f"Você escolheu {quantidade} garrafa(s) de {tipo}. Valor a pagar: R${total:.2f}")
