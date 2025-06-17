#%%

#Escreva um programa que solicite ao usuário frases. Para parar de solicitar frases, ele pode apenas apertar o “enter”. Seu programa deve apresentar cada frase e quantas vezes ela foi repetida.
# Criação de um dicionário para armazenar as frases e suas contagens
frases = {}
# Loop para solicitar frases ao usuário
while True:
    frase_usuario = input("Digite uma frase (ou aperte 'enter' para sair): ").strip()
    # Verifica se o usuário apertou 'enter' para sair
    if frase_usuario == "":
        break
    # Incrementa a contagem da frase no dicionário
    if frase_usuario in frases:
        frases[frase_usuario] += 1
    else:
        frases[frase_usuario] = 1
# Exibe cada frase e quantas vezes ela foi repetida
for frase, contagem in frases.items():
    print(f"A frase '{frase}' foi repetida {contagem} vez(es).")
    
#%%
print(frases)  # Exibe o dicionário completo com as frases e suas contagens

#%%
#Imprime o dicionário de forma ordenada da frase mais repetida para a menos repetida
for frase, contagem in sorted(frases.items(), key=lambda item: item[1], reverse=True):
    print(f"A frase '{frase}' foi repetida {contagem} vez(es).")
    

# Fim do código
