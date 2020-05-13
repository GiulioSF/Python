times = ('Corinthians', 'Palmeiras', 'Santos', 'Gremio',
        'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense',
        'Atlético-MG', 'Botafogo', 'Atlético -PR', 'Bahia',
        'São Paulo', 'Fluminense', 'Sport Recife',
        'EC Vitória', 'Coritiba', 'Avaí', 'Ponte Preta',
        'Atlético-GO')

print('-=' * 60)
print(f'Os primeiro 5 primeiros times da tabela são: {times[:5]}')
print('-=' * 60)
print(f'Os útlimos 4 últmos times da tabela são: {times[-4:]}')
print('-=' * 60)
print(f'Time em ordem alfabérica: {sorted(times)}')
print('-=' * 60)
print(f'A Chapecoense está na {times.index("Chapecoense")+1}ª posição.')