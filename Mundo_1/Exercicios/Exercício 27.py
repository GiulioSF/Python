nome = str(input('Digite seu nome completo: ')).strip()
prim = nome.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(prim[0]))
print('Seu último nome é {}'.format(prim[len(prim)-1]))