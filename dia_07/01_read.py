#%%

nome_arquivo = "historia.txt"

open_file = open(nome_arquivo, "r", encoding="utf-8")
texto = open_file.read()

#%%
print(open_file)
print(texto)

#%%
open_file.close()
