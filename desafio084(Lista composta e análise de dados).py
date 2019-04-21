lista = []
dadostemp = []
maior = menor = 0
while True:
    nome = str(input('Nome: '))
    dadostemp.append(nome)
    peso = float(input('Peso: '))
    dadostemp.append(peso)
    if len(lista) == 0:
        maior = menor = dadostemp[1]
    else:
        if dadostemp[1] > maior:
            maior = dadostemp[1]
        if dadostemp[1] < menor:
            menor = dadostemp[1]
    lista.append(dadostemp[:])
    dadostemp.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
        break
print(lista)
print(f'Você cadastrou {len(lista)} pessoas!')
print(f'O maior peso foi {maior} de', end='')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'O menor peso foi {menor} de ', end='')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]!', end='')
