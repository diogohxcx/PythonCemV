print('Gerador de PA!')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Informe a razão da PA:'))
termo = primeiro
cont = 1
while cont <10:
    termo += razão
    cont += 1
    print('{} - ' .format(termo), end='')
print('FIM!')
print('-=' * 10)
