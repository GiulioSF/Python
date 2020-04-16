valor = (float(input('Valor das compras? R$')))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] À vista dinheiro/cheque')
print('[ 2 ] À vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opc = int(input('Qual é a opção? '))

if opc == 1:
    novo_valor = (valor - (valor * 0.1))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, novo_valor))

elif opc == 2:
    novo_valor = (valor - (valor * 0.05))
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, novo_valor))

elif opc == 3:
    print('Sua compra vai custar R${:.2f} no final.'.format(valor))

else:
    parc = int(input('Deseja parcelar em quantas vezes?'))
    novo_valor = (valor + (valor * 0.2))
    novo_parc = novo_valor / parc
    print('Sua compra de R${:.2f} vai custar R${:.2f} no final, com {} parcelas de R${:.2f}.'.format(valor, novo_valor, parc, novo_parc))