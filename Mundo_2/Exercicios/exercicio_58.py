from random import randint
from time import sleep
computador = randint(0, 10)
tentativas = 0

print ('-=-'*20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*20)
jogador = int(input('Em que número eu pensei: '))

while jogador != computador:
    if jogador > computador:
        print('Menos... Tente novamente.')
        jogador = int(input('Qual é seu palpite? '))
        tentativas += 1

    if jogador < computador:
        print('Mais... Tente novamente.')
        jogador = int(input('Qual é seu palpite? '))
        tentativas += 1
print('Acertou com {} tentativas. Parabéns'.format(tentativas))