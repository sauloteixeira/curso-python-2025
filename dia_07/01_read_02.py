#%%

nome_arquivo = "historia.txt"

with open(nome_arquivo, encoding="utf-8") as open_file:
    conteudo = open_file.read()

print(conteudo)