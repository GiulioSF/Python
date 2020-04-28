num = int(input('Digite uma número para sua tabuada: '))
for cont in range(1, 11):
    print('{} x {:2} = {}'.format(num, cont, num*cont))