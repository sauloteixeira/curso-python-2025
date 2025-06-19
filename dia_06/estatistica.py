#%%

# Este módulo contém funções para calcular diversas medidas estatísticas
def soma(a, b):
    """
    Função que recebe dois números e retorna a soma deles.
    
    Parâmetros:
    a (int ou float): Primeiro número.
    b (int ou float): Segundo número.
    
    Retorna:
    int ou float: A soma de a e b.
    """
    return a + b

def media(lista):
    """
    Função que recebe uma lista de números e retorna a média.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    float: A média dos números na lista.
    """
    if not lista:
        return 0
    return sum(lista) / len(lista)

def mediana(lista):
    """
    Função que recebe uma lista de números e retorna a mediana.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    float: A mediana dos números na lista.
    """
    if not lista:
        return 0
    sorted_list = sorted(lista)
    n = len(sorted_list)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2
    else:
        return sorted_list[mid]
    
def moda(lista):
    """
    Função que recebe uma lista de números e retorna a moda.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    int ou float: A moda dos números na lista.
    """
    if not lista:
        return None
    from collections import Counter
    count = Counter(lista)
    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]
    return modes[0] if len(modes) == 1 else modes

def variancia(lista):
    """
    Função que recebe uma lista de números e retorna a variância.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    float: A variância dos números na lista.
    """
    if not lista:
        return 0
    mean = media(lista)
    return sum((x - mean) ** 2 for x in lista) / len(lista)

def desvio_padrao(lista):
    """
    Função que recebe uma lista de números e retorna o desvio padrão.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    float: O desvio padrão dos números na lista.
    """
    if not lista:
        return 0
    return variancia(lista) ** 0.5

def coeficiente_variacao(lista):
    """
    Função que recebe uma lista de números e retorna o coeficiente de variação.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    float: O coeficiente de variação dos números na lista.
    """
    if not lista or media(lista) == 0:
        return 0
    return desvio_padrao(lista) / media(lista)

def quartis(lista):
    """
    Função que recebe uma lista de números e retorna os quartis.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    tuple: Os quartis Q1, Q2 (mediana) e Q3.
    """
    if not lista:
        return (0, 0, 0)
    sorted_list = sorted(lista)
    n = len(sorted_list)
    q2 = mediana(sorted_list)
    
    if n % 2 == 0:
        lower_half = sorted_list[:n // 2]
        upper_half = sorted_list[n // 2:]
    else:
        lower_half = sorted_list[:n // 2]
        upper_half = sorted_list[n // 2 + 1:]
    
    q1 = mediana(lower_half)
    q3 = mediana(upper_half)
    
    return (q1, q2, q3)

def amplitude(lista):
    """
    Função que recebe uma lista de números e retorna a amplitude.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    float: A amplitude dos números na lista.
    """
    if not lista:
        return 0
    return max(lista) - min(lista)

def coeficiente_assimetria(lista):
    """
    Função que recebe uma lista de números e retorna o coeficiente de assimetria.
    
    Parâmetros:
    lista (list): Lista de números (int ou float).
    
    Retorna:
    float: O coeficiente de assimetria dos números na lista.
    """
    if not lista or desvio_padrao(lista) == 0:
        return 0
    mean = media(lista)
    median = mediana(lista)
    std_dev = desvio_padrao(lista)
    return 3 * (mean - median) / std_dev

#%%
# ler uma lista de 10 números inteiros do usuário
if __name__ == "__main__":
    try:
        numeros = list(map(int, input("Digite 10 números inteiros separados por espaço: ").split()))
        if len(numeros) != 10:
            raise ValueError("Você deve inserir exatamente 10 números.")
        
        print(f"Soma: {soma(numeros[0], numeros[1])}")
        print(f"Média: {media(numeros)}")
        print(f"Mediana: {mediana(numeros)}")
        print(f"Moda: {moda(numeros)}")
        print(f"Variância: {variancia(numeros)}")
        print(f"Desvio Padrão: {desvio_padrao(numeros)}")
        print(f"Coeficiente de Variação: {coeficiente_variacao(numeros)}")
        print(f"Quartis: {quartis(numeros)}")
        print(f"Amplitude: {amplitude(numeros)}")
        print(f"Coeficiente de Assimetria: {coeficiente_assimetria(numeros)}")
        
    except ValueError as e:
        print(f"Erro: {e}")

#%%
# ler uma lista com um numero indefinido de números inteiros do usuário
if __name__ == "__main__":
    try:
        numeros = list(map(int, input("Digite números inteiros separados por espaço (pressione Enter para finalizar): ").split()))
        
        if not numeros:
            raise ValueError("Você deve inserir pelo menos um número.")
        
        print(f"Soma: {soma(numeros[0], numeros[1]) if len(numeros) > 1 else numeros[0]}")
        print(f"Média: {media(numeros)}")
        print(f"Mediana: {mediana(numeros)}")
        print(f"Moda: {moda(numeros)}")
        print(f"Variância: {variancia(numeros)}")
        print(f"Desvio Padrão: {desvio_padrao(numeros)}")
        print(f"Coeficiente de Variação: {coeficiente_variacao(numeros)}")
        print(f"Quartis: {quartis(numeros)}")
        print(f"Amplitude: {amplitude(numeros)}")
        print(f"Coeficiente de Assimetria: {coeficiente_assimetria(numeros)}")
        
    except ValueError as e:
        print(f"Erro: {e}")