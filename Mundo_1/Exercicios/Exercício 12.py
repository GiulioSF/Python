prod = float(input('Qual o valor do produto? R$ '))
desc = ((prod*5)/100)
val = prod - desc
print('O valor do desconto é de R$ {:.2f} e seu novo preço é R$ {:.2f}'.format(desc, val))