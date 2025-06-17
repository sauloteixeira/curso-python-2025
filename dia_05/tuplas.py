#%%
dados_saulo = [52, 1, "casado", "dev python"]
print(dados_saulo)
dados_saulo.append("5500")
dados_saulo[0] = 52.5
print(dados_saulo)

#%%
# Tuplas são semelhantes às listas, mas são imutáveis (não podem ser alteradas após a criação)
tupla_saulo = (52, 1.68, "casado", "dev python", "5500", ["python", "java", "c++"])
print(tupla_saulo)
print(type(tupla_saulo))


# Tupla não pode ser alterada, mas podemos criar uma nova tupla com os valores alterados
tupla_saulo = (52, 1.68, "casado", "dev python", "5500", ["python", "java", "c++", "javascript"])
print(tupla_saulo)

tupla_saulo[-1].append("sql")  # Podemos alterar os elementos dentro de uma lista dentro da tupla
print(tupla_saulo)
