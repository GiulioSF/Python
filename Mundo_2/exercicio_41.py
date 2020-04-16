from datetime import date

nasc = int(input('Qual o seu ano de nascimento? '))
atual = date.today().year
idade = atual - nasc
print('Você possui {} anos'.format(idade))

if idade <= 9:
    print('Catergoria MIRIM')

elif 14 >= idade > 9:
    print('Catergoria INFANTIL')

elif 19 >= idade > 14:
    print('Catergoria JUNIOR')

elif 25 >= idade > 19:
    print('Catergoria SÊNIOR')

elif idade > 25:
    print('Catergoria MASTER')