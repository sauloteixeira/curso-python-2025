#%%
# Programa da sorveteria

print("Escolha o tipo de sorvete:")
print("1 - Casquinha (R$1,00)")
print("2 - Cascão (R$2,50)")
print("3 - Cestinha (R$4,00)")
tipo = input("Digite o número da opção desejada: ")

if tipo == "1":
    preco_tipo = 1.00
    nome_tipo = "casquinha"
elif tipo == "2":
    preco_tipo = 2.50
    nome_tipo = "cascão"
elif tipo == "3":
    preco_tipo = 4.00
    nome_tipo = "cestinha"
else:
    print("Tipo de sorvete inválido.")
    preco_tipo = None

if preco_tipo is not None:
    print("\nEscolha o sabor do sorvete:")
    print("1 - Morango")
    print("2 - Creme")
    print("3 - Chocolate")
    sabor = input("Digite o número da opção desejada: ")

    if sabor == "1":
        nome_sabor = "morango"
    elif sabor == "2":
        nome_sabor = "creme"
    elif sabor == "3":
        nome_sabor = "chocolate"
    else:
        print("Sabor inválido.")
        nome_sabor = None

    if nome_sabor is not None:
        print("\nEscolha a cobertura:")
        print("1 - Caramelo (R$1,50)")
        print("2 - Morango (R$1,50)")
        print("3 - Chocolate (R$1,50)")
        print("4 - Sem cobertura (R$0,00)")
        cobertura = input("Digite o número da opção desejada: ")

        if cobertura == "1":
            preco_cobertura = 1.50
            nome_cobertura = "caramelo"
        elif cobertura == "2":
            preco_cobertura = 1.50
            nome_cobertura = "morango"
        elif cobertura == "3":
            preco_cobertura = 1.50
            nome_cobertura = "chocolate"
        elif cobertura == "4":
            preco_cobertura = 0.00
            nome_cobertura = "sem cobertura"
        else:
            print("Cobertura inválida.")
            preco_cobertura = None

        if preco_cobertura is not None:
            total = preco_tipo + preco_cobertura
            print(f"\nVocê escolheu {nome_tipo} de {nome_sabor} com {nome_cobertura}.")
            print(f"Valor a ser pago: R${total:.2f}")
