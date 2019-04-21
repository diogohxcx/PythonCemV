from random import randint
from time import sleep
from operator import itemgetter
print('Vamor rolas os dados!')
sleep(1)
jogadores = {}
jogadores['jogador1'] = randint(1, 6)
jogadores['jogador2'] = randint(1, 6)
jogadores['jogador3'] = randint(1, 6)
jogadores['jogador4'] = randint(1, 6)
for j, d in jogadores.items():
    print(f'O {j} tirou {d} no dado! ')
    sleep(0.5)
print('=-=' * 11)
print('   == RANKING DOS JOGADORES == ')
jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=(True))
for i, v in enumerate(jogadores):
    print(f'    {i+1}º lugar: {v[0]} com {v[1]}')
print('=-=' * 11)
