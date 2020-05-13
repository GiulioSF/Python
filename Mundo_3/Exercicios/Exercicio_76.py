palavras = ('aprender', 'programar', 'linguagem',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'futuro')
for p in palavras:
    print(f'\nNa palavra aprender {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')