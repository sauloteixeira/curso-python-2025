#%%
A = 1
B = 2
print(A, B)

#%%
A, B = B, A

print(A, B)

#%%

a, b = 1, 2

print(a, b)

#%%

a, b, c = 1, 2, 3

print(a, b, c)

#%%

a, b, *restante = 1, 2, 3, 4, 8, 49, 54, 7, 6

print(a, b, restante)

#%%

*restante, a, b = 1, 2, 3, 4, 8, 49, 54, 7, 6

print(a, b, restante)

#%%

a, *restante, b = 1, 2, 3, 4, 8, 49, 54, 7, 6

print(a, b, restante)

#%%

def soma(a, *args):
    total = a + sum(args)
    return total

soma(1, 2, 3, 4, 5, 6, 7)

#%%

values = [1, 2, 3, 4]

soma(*values)