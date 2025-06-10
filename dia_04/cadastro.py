#%%
# Programa que acumula nomes e idades digitadas pelo usuário, interrompendo quando o nome for em branco.

cadastros = []

while True:
    nome = input("Digite o nome (ou pressione Enter para finalizar): ")
    if nome == "":
        break
    idade = input("Digite a idade: ")
    cadastros.append((nome, idade))

print("\nCadastros realizados:")
for nome, idade in cadastros:
    print(f"Nome: {nome}, Idade: {idade}")


