num = 0
cont = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    soma = num + num
    cont += 1

print('Você digitou {} números e a soma entre eles é {}'.format(cont, soma))