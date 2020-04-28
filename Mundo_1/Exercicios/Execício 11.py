larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área de é de {}m²'.format(larg, alt, area))
tinta = area/2
print('Para pinta essa parede você vai precisar de {}L de tinta'.format(tinta))
