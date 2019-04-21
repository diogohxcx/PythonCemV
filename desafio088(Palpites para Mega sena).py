from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
quant = int(input('Quantos jogos você quer que eu faça?: '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'***Sorteando {quant} jogos.***')
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('***Boa Sorte***')
