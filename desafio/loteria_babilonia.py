#%%

import random

# Loteria Babilônia
# O usuário deve tentar adivinhar um número sorteado entre 1 e 15.

#função para obter a entrada do usuário
def get_input():
	while True:
		try:
			numero_usuario = int(input("Entre com um número entre 1 e 15: "))

		except ValueError as err:
			print("Valor Inválido")
			continue

		if numero_usuario >= 1 and numero_usuario <= 15:
			return numero_usuario

#função para verificar se o número do usuário é igual ao número sorteado
def check_numbers(numero_usuario, numero_sorteio):
    if numero_usuario == numero_sorteio:
        print("Parabéns! Você acertou o número!")
        return True
    elif numero_usuario < numero_sorteio:
        print("O número sorteado é maior que o seu palpite.")
		
    else:
        print("O número sorteado é menor que o seu palpite.")
    return False

# Sorteia um número entre 1 e 15		
numero_sorteio = random.randint(1, 15)
print("Bem-vindo ao jogo da Loteria Babilônia!")

# O usuário tem 3 tentativas para adivinhar o número sorteado
print("Você tem 3 tentativas para adivinhar o número sorteado entre 1 e 15.")

# Loop para as tentativas
for i in range(3):
	numero_usuario = get_input()
	if check_numbers(numero_usuario, numero_sorteio):
		break
	print("Tentativas restantes: ", 2 - i)

else:
	print("Suas tentativas acabaram :'( - o número era", numero_sorteio)


# Fim do código