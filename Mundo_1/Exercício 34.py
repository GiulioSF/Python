sal = int(input('Informe seu salário: R$ '))
if sal <= 1250:
    novo = sal + (sal * 15 / 100)
else:
    novo = sal + (sal * 10 / 100)
print('Quem ganhava R${:.2f} agora vai ganhar R${:.2f}'.format(sal, novo))