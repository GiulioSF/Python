contidade = contsexo = cont = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip()[0]
    if idade > 18:
        contidade += 1
    
    elif sexo in 'Mm':
        contsexo += 1
    
    elif sexo in 'Ff' and idade < 20:
        cont += 1
    
    opcao = str(input('Quer continuar? [S/N]'))
    if opcao in 'Nn':
        break
print(f'Total de pessoas com mais de 18 anos: {contidade}.')
print(f'Ao todo temos {contsexo} homens cadastrados.')
print(f'Temos {cont} mulher(es) com menos de 20 anos.')
    