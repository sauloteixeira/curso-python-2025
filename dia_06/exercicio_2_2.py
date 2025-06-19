#%%
# criar uma função para ver se um número inteiro é par ou ímpar
def par_ou_impar(numero):
    """
    Função que verifica se um número é par ou ímpar.
    
    Args:
        numero (int): O número a ser verificado.
    
    Returns:
        str: 'Par' se o número for par, 'Ímpar' se for ímpar.
    """
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

#%%    
# Exemplo de uso onde o usuário pode inserir um número
if __name__ == "__main__":
    try:
        numero = int(input("Digite um número inteiro: "))
        resultado = par_ou_impar(numero)
        print(f"O número {numero} é {resultado}.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
