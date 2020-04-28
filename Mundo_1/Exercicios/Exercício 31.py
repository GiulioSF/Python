dist = int(input('Qual a distância da viagem que você deseja: '))
perto = (dist * 0.50)
longe = (dist * 0.45)
if dist <= 200:
    print('Você deseja viajar {}Km, portanto o valor da passagem será de R${:.2f}'.format(dist, perto))
else:
    print('Você deseja viajar {}Km, portanto o valor da passagem será de R${:.2f}'.format(dist, longe))