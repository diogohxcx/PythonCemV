t = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
     'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
     'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
     'Vasco', 'Sport Recife', 'América-MG', 'Vitória', 'Paraná')
print('='*138)
print(f'Times do Brasileirão -> {t}')
print('='*138)
print(f'Os primeiros cinco colocados -> {t[0:5]}')
print('='*138)
print(f'Os quatro últimos colocados -> {t[16:20]} ')
print('='*138)
print(f'Times em ordem alfabética -> {sorted(t)}')
print('='*138)
print(f'A Chapecoense está na {t.index("Chapecoense")}º posição!')