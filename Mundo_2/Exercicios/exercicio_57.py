sexo = str(input('Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':  
    sexo = str(input('Selecione uma opção válida. Por favor, informe seu sexo: [M/F] ')).strip().upper()[0]
print('Você selecionou a opção {}.'.format(sexo))