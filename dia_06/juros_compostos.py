#%%

def juros_compostos(capital_inicial:float, taxa_juros:float, tempo:int)->float:
    """
    Calcula o montante final de um investimento com juros compostos.

    Args:
        capital_inicial (float): Valor inicial investido.
        taxa_juros (float): Taxa de juros (em porcentagem).
        tempo (int): Tempo de investimento em anos.

    Returns:
        float: Montante final após o período de investimento.
    """
    montante = capital_inicial * (1 + taxa_juros / 100) ** tempo
    return montante
# Exemplo de uso
if __name__ == "__main__":
    capital_inicial = 1000.0  # Valor inicial investido
    taxa_juros = 5.0           # Taxa de juros em porcentagem
    tempo = 10                  # Tempo de investimento em anos

    montante_final = juros_compostos(capital_inicial, taxa_juros, tempo)
    print(f"Montante final após {tempo} anos: R$ {montante_final:.2f}")
#%%
# lendo os dados do usuário
    capital_inicial = float(input("Digite o capital inicial: "))
    taxa_juros = float(input("Digite a taxa de juros (em %): "))
    tempo = int(input("Digite o tempo de investimento (em anos): "))
    montante_final = juros_compostos(capital_inicial, taxa_juros, tempo)
    print(f"Montante final após {tempo} anos: R$ {montante_final:.2f}")

#%%
montante_final = juros_compostos(1000, 5, 1)
print(f"Montante final após 10 anos: R$ {montante_final:.2f}")
