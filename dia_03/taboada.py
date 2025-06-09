#%%
# contatem de 1 a 10 usando while
count = 1

while count <= 10:
    print("Contagem", count)
    count += 1

#%%
# Tabuada do 2 de 1 até 100 usando while

multiplicador = 1

while multiplicador <= 100:
    resultado = 2 * multiplicador
    print(f"2 x {multiplicador} = {resultado}")
    multiplicador += 1

print("Tabuada do 2 concluída.")

#%%
# Tabuada do 2 de 1 até 100 usando for
for multiplicador in range(1, 101):
    resultado = 2 * multiplicador
    print(f"2 x {multiplicador} = {resultado}")

print("Tabuada do 2 concluída.")

#%%
# quais numero são divisíveis por 4 de 1 a 100 (laço for)	
for numero in range(1, 101):
    if numero % 4 == 0:
        print(f"{numero} é divisível por 4")
    else:
        print(f"{numero} não é divisível por 4")

#%%
# quais numero são divisíveis por 3 de 1 a 100 (laço while)
numero = 1
while numero <= 100:
    if numero % 3 == 0:
        print(f"{numero} é divisível por 3")
    else:
        print(f"{numero} não é divisível por 3")
    numero += 1