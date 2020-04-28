media = cont = soma = 0
opcao = ''

while opcao in 'Ss':
    num = int(input('Digite um número: '))
    soma += num
    cont += 1
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    opcao = str(input('Quer continuar [S/N]? ')).strip()[0]
media = soma / cont
print('Você digitou {} número e a média foi {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))

