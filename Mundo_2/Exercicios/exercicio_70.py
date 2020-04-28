total = contmenor = cont = 0
barato = ' '

while True:
    produto = str(input('Nome do Produto: '))
    valor = int(input('Preço: R$ '))
    contmenor += 1
    total += valor
    if valor > 1000:
        cont += 1
    if contmenor == 1 or valor < menor:
        menor = valor
        barato = produto

    opcao = ' '
    while opcao not in 'SsNn':
        opcao = str(input('Quer continuar? [S/N]')).strip()[0]
    if opcao in 'Nn':
        break           
print(f'O total da compra foi R$ {total:.2f}.')
print(f'Temos {cont} produto(s) custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} e custa R$ {menor:.2f}')