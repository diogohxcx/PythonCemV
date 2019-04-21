jogador = dict()
gols = []
totgols = 0
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na {c+1}º partida?: ')))
jogador['gols'] = gols[:]
# Utilizei o for para realizar a soma dos gols no Python podemos usar o 'sum'
for g in gols:
    totgols += g
jogador['total'] = totgols
print('-=' * 25)
print(jogador)
print('-=' * 25)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 25)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i+1}, fez {v} gols.')
print(f'O total de gols foi {jogador["total"]}')




