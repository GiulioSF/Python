num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))

print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es).')

if 3 in num:
    print(f'O primeiro valor 3 foi digitado na posição {num.index(3) + 1}.')
else:
    print(f'O número 3 não foi digitado.')

print('Os número pares foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n , end=' ')

