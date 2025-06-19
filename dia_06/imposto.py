# *args - se comporta como uma tupla
# **kwargs - se comporta como um dicionário

#%%
# Função para calcular imposto sobre um produto
def calc_imposto(preco: float, tx_base: float, **kwargs) -> float:
    """
    Função que calcula o imposto sobre um preço dado uma taxa de imposto.

    Parâmetros:
    preco (float): Preço do produto.
    tx_base (float): Taxa de imposto em porcentagem.
    kwargs: Argumentos adicionais (não utilizados).

    Retorna:
    float: O valor do imposto calculado.
    """
    imposto = preco * tx_base
    
    for i in kwargs:
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto

#%%
# Exemplo de uso da função calc_imposto
calc_imposto(1000, 0.2, tx_adicional=0.05, tx_extra=0.03)

#%%
# Exemplo de uso da função calc_imposto com argumentos adicionais     
impostos_gerais = {
    'tx_adicional': 0.05,
    'tx_extra': 0.03,
    'tx_especial': 0.1
}
# Chamada da função com argumentos adicionais
imposto_calculado = calc_imposto(1000, 0.2, **impostos_gerais)
print(f"Imposto calculado: {imposto_calculado}")

