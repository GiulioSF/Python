print('-' * 30)
print('Sequência de Finobacci')
print('-' * 30)
n = int(input('Quantos termos você quer mostrar? '))
cont = 0
t1 = 0
t2 = 1
print('~' * 50)
print('{} -> {}'.format(t1, t2), end='')
con = 3
while cont <= n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
print('~' * 50)