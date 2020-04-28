sal = float(input('Qual o salário do funcionário? R$ '))
aum = ((sal*15)/100)
total= sal + aum
print('O salário do funcionário com o aumento de R$ {:.2f} terá um total de R$ {:.2f}'.format(aum, total))