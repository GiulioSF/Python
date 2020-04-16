a = int(input('Digite primeiro número: '))
b = int(input('Digite segundo número: '))
c = int(input('Digite terceiro número: '))

menor = a
#Verificando menor número
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando maior número
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {}'.format(menor))
print('O menor número é {}'.format(maior))