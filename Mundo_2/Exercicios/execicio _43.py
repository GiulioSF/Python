peso = float(input('Qual o seu peso em kg? '))
alt = float(input('Qual sua altura em metros? '))

imc = peso / (alt ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

if imc < 18.5:
    print ('Abaixo do Peso')

elif 25 > imc >= 18.5:
    print ('Peso Ideal')

elif 30 > imc >= 25:
    print ('Sobrepeso')

elif 40 > imc >= 30:
    print ('Obesidade')

else:
    print ('Obesidade Mórbida')