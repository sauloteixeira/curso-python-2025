#%%
x = []

#criar uma lista com 100 números inteiros aleatórios de 1 a 100 em ordem crescente

for i in range(1, 101):
    x.append(i)

print(x)

#%%

y = [i for i in range(1, 101)]
print(y)

def eh_par(n):
    return n % 2 == 0

z = [i for i in range(1, 101) if not eh_par(i)]
print(z)

w = [eh_par(i) for i in range(1, 101)]
print(w)