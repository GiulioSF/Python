from random import randint

v = 0
print('=-' * 30)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 30)

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ''
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
    if tipo in 'Pp':
        if total % 2 == 0:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
            break
    elif tipo in 'Ii':
        if total % 2 == 1:
            print('Você VENCEU!!')
            v += 1
        else:
            print('Você PERDEU!!')
    print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes.')
