km = float(input('Qual a kilometragem percorrida? KM '))
dia = float(input('Quantos dias ele foi alugado? '))
kmtotal = (km* 0.15)
diatotal = (dia*60)
total = kmtotal + diatotal
print('O carro foi alugado por {:.2f} dias e percorreu {:.2f}KM. Total a pagar R$ {:.2f}'.format(dia, km, total))
