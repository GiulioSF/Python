from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    atual = date.today().year
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pess)))
    idade = atual - nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} maior de idade'.format(totmaior))
print('Tabém tivemos {} menor de idade'.format(totmenor))