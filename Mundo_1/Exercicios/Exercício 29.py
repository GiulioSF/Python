velo = float(input('Qual a velocidade do carro? '))
multa = ((velo - 80)*7)
if velo > 80:
    print('Você está acima da velocidade permitida e terá uma multa de R${:.2f}'.format(multa).upper())
else:
    print('Muito bem, dirija com cuidado.')