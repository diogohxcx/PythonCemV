print('#' * 20)
print('Lojas Shopimtudo!')
print('#' * 20)
totcompra = mil = barato = cont = 0
menor = ''
while True:
    nome = str(input('Nome do produto:'))
    preço = float(input('Preço do produto R$:'))
    resp = ' '
    totcompra += preço
    cont += 1
    if preço >= 1000:
        mil += 1
    if cont == 1:
        barato = preço
        menor = nome
    else:
        if preço < barato:
            barato = preço
            menor = nome
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N] ?')).upper().strip()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'Total da compra foi: R${totcompra:.2f}.')
print(f'Podutos que custaram mais de R$1000,00 foram - {mil}.')
print(f'O produto mais barato foi {menor} e custou R${barato:.2f}!')