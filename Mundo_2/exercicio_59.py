from time import sleep
opcao = 0

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

while opcao != 5:
    sleep(1)
    opcao = int(input(
        '''[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa
>>>>> Qual é a sua opção? '''))

    if opcao == 1:
        soma = n1 + n2
        sleep(1)
        print('A soma dos números {} e {}, é igual a {}.'.format(n1, n2, soma))
        print ('-=-' * 20)

    if opcao == 2:
        mult = n1 * n2
        sleep(1)
        print('A multiplicação dos números {} e {}, é igual a {}'.format(n1, n2, mult))
        print ('-=-' * 20)
    
    if opcao == 3:
        if n1 > n2:
            sleep(1)
            print('O {} é maior que {}.'.format(n1, n2))
            print ('-=-' * 20)
        else:
            sleep(1)
            print('O {} é maior que {}.'.format(n2, n1))
            print ('-=-' * 20)

    if opcao == 4:
        sleep(1)
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print ('-=-' * 20)

sleep(1)
print('O programa foi finalizado!')