from datetime import date

atual = date.today().year
nasc = int(input("Qual a sua data de nascimento? "))
idade = atual - nasc

print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print ('Você tem que se alistar imediatamente')

elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(saldo))