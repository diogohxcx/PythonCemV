from random import randint
pc = randint(0, 10)
print('Acabei de pensar em um número entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
win = False
palpites = 0
while not win:
    player = int(input('Qual é o seu palpite:'))
    palpites += 1
    if player == pc:
        win = True
    else:
        if pc > player:
            print('Maior...Tente outra vez:')
        else:
            print('Menor...Tente outra vez:')
print('Você acertou e precisou de {} tentivas!'.format(palpites))


