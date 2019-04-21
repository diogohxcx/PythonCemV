from random import randint
from time import sleep
l = list()
d = {1: randint(1, 6), 2: randint(1, 6), 3: randint(1, 6), 4: randint(1, 6)}
print('Valores sorteados:\n')
for a, b in d.items():
    print(f'O jogador {a} tirou {b}')
    l.append(b)
    sleep(1)
print('\nRanking dos jogadores: \n')
for c in range (1, 5):
    print(f'{c}º lugar: jogador {l.index(max(l)) + 1} com {max(l)}')
    l[l.index(max(l))] = 0