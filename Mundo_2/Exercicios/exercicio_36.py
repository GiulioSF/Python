valor = int(input('Qual o valor da casa? R$ '))
sal = int(input('Qual o seu salário? R$ '))
anos = int(input('Quantos anos pretende pagar? '))

prest = int(valor / anos)

if prest > (sal * 0.3):
    print ('Empréstimo negado')

else:
    print ('O valor da prestação será de R$ {},00'.format(prest))