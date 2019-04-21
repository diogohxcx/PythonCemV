lista = []
listaPar = []
listaImpar = []
while True:
    valor = int(input('Digite um número:'))
    lista.append(valor)
    resp = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
    if valor % 2 == 0:
        listaPar.append(valor)
    else:
        listaImpar.append(valor)
    if resp == 'N':
        break
print(f'Sua lista completa é {lista}')
print(f'Sua lista apenas com números pares é {listaPar}')
print(f'Sua lista apenas com números impares é {listaImpar}')
