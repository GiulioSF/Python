import math
catop = float(input('Digite o comprimento do Cateto Oposto: '))
catad = float(input('Digite o comprimento do Cateto Adjacente: '))
hip = math.hypot(catop, catad)
print('A hipotenusa para {} e {} é igual a {:.2f}'.format(catop, catad, hip))