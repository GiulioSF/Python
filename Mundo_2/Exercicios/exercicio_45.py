from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)


print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jogador = int(input('Qual é a sua jogada?'))
print('-' * 12)
print('Computador jogou {}'. format(itens[computador]))
print('Jogador jogou {}'. format(itens[jogador]))
print('-' * 12)

if computador == 0:
    if jogador ==  0:
       print('EMPATOU')

    elif jogador == 1:
       print('GANHOU')

    elif jogador == 2:
       print('PERDEU')

elif computador == 1:
    if jogador ==  0:
       print('PERDEU')

    elif jogador == 1:
       print('EMPATOU')

    elif jogador == 2:
       print('GANHOU')

elif computador == 2:
    if jogador ==  0:
       print('GANHOU')

    elif jogador == 1:
       print('PERDEU')

    elif jogador == 2:
       print('EMPATOU')