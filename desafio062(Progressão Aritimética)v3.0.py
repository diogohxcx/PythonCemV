print('Gerador de PA!')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Informe a razão da PA:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        termo += razão
        cont += 1
        print('{} - ' .format(termo), end='')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
    print('PAUSA:')
print('Foram exibidos {} termos! '.format(total))
print('-=' * 10)
