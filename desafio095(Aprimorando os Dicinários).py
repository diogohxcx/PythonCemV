time = list()
jogadores = dict()
partidas = list()
while True:
    jogadores.clear()
    jogadores['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gols na partidas {c+1}? ')))
    jogadores['gols'] = partidas[:]
    jogadores['total'] = sum(partidas)
    time.append(jogadores.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]')).upper()[0]
        if resp in 'SN':
            break
        print('Erro! Digite S ou N para continuar!')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogadores.keys():
    print(f'{i:<13}', end=' ')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<14}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Informe o cod do jogador para visualizar suas informações: [999 para finalizar!]' ))
    if busca == 999:
        break
    elif busca >= len(time):
        print('Cod não encontrado, informe o cod correto: ')
    else:
        print(f' --LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f' Na partira {i+1} ele fez {g} gols')
