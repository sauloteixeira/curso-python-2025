#%%
# Calculadora simples de soma

# Solicita ao usuário dois valores

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Realiza a soma
resultado = valor1 + valor2

# Exibe o resultado
print("A soma dos valores é:", resultado)

#%%
# Calculadora simples de subtração

# Solicita ao usuário dois valores

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Realiza a soma
resultado = valor1 - valor2

# Exibe o resultado
print("A subtração dos valores é:", resultado)

#%%
# Calculadora simples de multiplicação

# Solicita ao usuário dois valores

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Realiza a multiplicação
resultado = valor1 * valor2

# Exibe o resultado
print("A multiplicação dos valores é:", resultado)

# %%
# Calculadora simples de divisão

# Solicita ao usuário dois valores

valor1 = float(input("Digite o valor do numerador: "))
valor2 = float(input("Digite o segundo denominador: "))

# Realiza a divisão
if valor2 != 0:
    resultado = float(valor1 / valor2)
    print("A divisão dos valores é:", valor1 / valor2)
else:
    print("Não é possível dividir por zero.")

#%%
# Calculadora simples de potenciação

# Solicita ao usuário dois valores

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Realiza a potenciação
resultado = valor1 ** valor2

# Exibe o resultado
print(valor1, "elevado a", valor2, "é:", resultado)

#%%
# Calculadora simples de radiciação

# Solicita ao usuário dois valores

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Realiza a radiciação
resultado = valor1 ** (1/valor2)

# Exibe o resultado
print("A raiz", valor2, "de", valor1, "é:", resultado)
