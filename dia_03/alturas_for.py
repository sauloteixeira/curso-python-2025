#%%
# calculando a média de 4 alturas usando for
soma_alturas = 0

for contador in range(4):
    altura = float(input("Digite a altura (em metros): "))
    soma_alturas += altura

media_altura = soma_alturas / 4
print(f"A média das alturas é: {media_altura:.2f} metros")

