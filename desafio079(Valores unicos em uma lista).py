lista = []
while True:
    resp = ' '
    valor = (int(input('Digite um valor:')))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso!')
    else:
        print('Não podemos adicionar valores iguais, tente outro!')
    while resp not in 'SN':
        resp = str(input('Deseja continuar [S/N]:')).strip().upper()[0]
    if resp == 'N':
        break
lista.sort()
print(lista)

