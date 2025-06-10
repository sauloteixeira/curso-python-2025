#%%
# Cria uma lista de números inteiros com idades entre 18 e 65
idades = [18, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 65, 25, 19]
print(len(idades))  # Imprime o tamanho da lista
print(idades)

#%%
# Cria uma lista de strings com nomes de pessoas uma para cada idade
nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo", "Fernanda", "Gustavo", "Helena", "Igor", "Juliana", "Karina", "Lucas", "Mariana", "Nicolas"]
print(nomes)
print(len(nomes))
# Associa cada idade a um nome
pessoas = list(zip(nomes, idades)) 
print(pessoas)

#%%

# calcula a média das idades
media_idades = sum(idades) / len(idades)
print(f"Média das idades: {media_idades}")
# calcula a idade máxima
idade_maxima = max(idades)
print(f"Idade máxima: {idade_maxima}")
# calcula a idade mínima
idade_minima = min(idades)
print(f"Idade mínima: {idade_minima}")
# calcula a soma das idades
soma_idades = sum(idades)
print(f"Soma das idades: {soma_idades}")

#%%
# Cria uma lista de dicionários com informações de pessoas na seguinte ordem:
# nome, idade, profissão, empresas, estado civil, salários
Saulo = ["Saulo Teixeira", 
         52, 
         "Bacharel em Gestão da Informação", 
         ["HSBS", "PMJ", "SUAPE", "Intelivix", "Recursal"],
         "Casado", 
         [1500, 3500, 5000, 6500, 7500]]

print(Saulo)  # Imprime a lista completa
print(Saulo[0])  # Imprime o nome
print(Saulo[1])  # Imprime a idade
print(Saulo[2])  # Imprime a profissão
print(Saulo[3])  # Imprime a lista de empresas
print(Saulo[4])  # Imprime o estado civil
print(Saulo[5])  # Imprime a lista de salários

print(f"Nome: {Saulo[0]}, Idade: {Saulo[1]}, Profissão: {Saulo[2]}, Estado Civil: {Saulo[3]}, Salários: {Saulo[4]}")

print(Saulo[-1][0])  # Imprime o primeiro salário
print(Saulo[-1][1])  # Imprime o segundo salário
print(Saulo[-1][2])  # Imprime o terceiro salário
print(Saulo[-1][3])  # Imprime o quarto salário
print(Saulo[-1][4])  # Imprime o quinto salário

#imprime o último salário
print(f"Último Salário: {Saulo[-1][-1]}")  # Imprime o último salário
print(f"Penúltimo Salário: {Saulo[-1][-2]}")  # Imprime o penúltimo salário

#%%
#Imprimir os 4 primeiros elementos da lista de Saulo
print(Saulo[:4])  # Imprime os 4 primeiros elementos da lista de Saulo

#Imprimir as 3 últimas empresas
print(Saulo[3][-3:])  # Imprime as 3 últimas empresas da lista de Saulo

#%%
# criar e imprimir um dicionário com as informações de Saulo
saulo_dict = {
    "nome": Saulo[0],
    "idade": Saulo[1],
    "profissao": Saulo[2],
    "empresas": Saulo[3],
    "estado_civil": Saulo[4],
    "salarios": Saulo[5]
}
# Imprime o dicionário completo 1 dado por linha
for key, value in saulo_dict.items():
    print(f"{key}: {value}")