#%%

arquivo = "data.csv"

with open(arquivo, mode="r", encoding="utf-8") as open_file:
    lines = open_file.readlines()
    print(lines)

for l in lines:
    print(l.strip())

#%%  
dados = dict()

chaves = lines[0].strip("\n").split(";")

for c in chaves:
    dados[c] = []

dados
#%%

for l in lines[1:]:
    valores = l.strip("\n").split(";")
    for i, c in enumerate(chaves):
        dados[c].append(valores[i])

dados

#%%
idades = []
for i in dados["idade"]:
    idades.append(int(i))

media = sum(idades) / len(idades)
print(f"Idades: {idades}")
print(f"Média de idades: {media:.2f}")

