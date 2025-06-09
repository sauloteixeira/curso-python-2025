#%%
# Programa para somar saldos em conta até o usuário apertar enter sem digitar valor

soma_saldos = 0.0

while True:
    entrada = input("Digite o saldo em conta (ou pressione Enter para finalizar): ")
    #print(f"Entrada recebida: {entrada}")  # Debugging line to show input
    if entrada == "":
        break
    try:
        saldo = float(entrada)
        soma_saldos += saldo
    except ValueError:
        print("Valor inválido. Digite um número ou pressione Enter para sair.")

print(f"A soma dos saldos digitados é: R${soma_saldos:.2f}")
