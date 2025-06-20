#%%

txt = "\nMais texto"


nome_arquivo = "historia2.txt"

with open(nome_arquivo, mode="a", encoding="utf-8") as open_file:
    open_file.write(txt)
    