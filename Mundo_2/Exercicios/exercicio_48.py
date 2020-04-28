soma = 0
contador = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        contador = contador +1
        soma = soma + cont
print('A soma de todos so {} valores solicitados é {}'.format(contador, soma))