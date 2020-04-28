num = int(input('Digite um número: '))
tot = 0
for cont in range (1, num+1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        tot +=1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(cont), end=' ')
print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))

if tot == 2:
    print('NÚMERO PRIMO!!')

else:
    print('NÚMERO NÃO É PRIMO')