palavras = ('Casa','Carro','Esposa','Filho','Feliz','Esforço',
            'Consigo','Vida','Melhor','Familia','Tenho','Tudo')
for v in palavras:
    print(f'\nNa palavra {v.upper()} temos ->', end='')
    for letra in v:
        if letra.upper() in 'AEIOU':
            print(letra, end=' ')
