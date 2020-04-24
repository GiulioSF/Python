somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulher = 0

for p in range (1,5):
    print('----- {}ª PESSOA -----'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

    if idade < 20 and sexo in 'Ff':
        mulher += 1

mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('Existem {} mulher com menos de 20 anos'.format(mulher))