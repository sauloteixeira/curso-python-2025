#%%
# calculando a média de 4 alturas usando while
altura = 0
soma_alturas = 0
contador = 0
while contador < 4:
    altura = float(input("Digite a altura (em metros): "))
    soma_alturas += altura
    contador += 1
media_altura = soma_alturas / 4
print(f"A média das alturas é: {media_altura:.2f} metros")

