lista = []
while True:
    resp = ' '
    valor = int(input('Digite um valor:'))
    lista.append(valor)
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
if 5 in lista:
    print('O 5 está na lista!')
else:
    print('O 5 não está na lista!')
print(f'Você digitou {len(lista)} elementos.')
lista.sort(reverse=True)
print(f'Os valores em ordem decrescentes são {lista}')
