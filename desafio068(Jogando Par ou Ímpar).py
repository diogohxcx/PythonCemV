from random import randint
print('-=' * 16)
print('### VAMOS JOGAR PAR OU ÍMPAR ###')
print('-=' * 16)
vitória = 0
while True:
    jogador = int(input('Digite um valor:'))
    pi = str(input('Escolhe entre par ou ímpar [P/I]:')).upper().strip()[0]
    computador = randint(0, 10)
    rodada = (jogador + computador)% 2
    if pi == 'P' and rodada == 0:
        vitória += 1
        print(f'Você venceu!! O computador digitou {computador} e você digitou {jogador} e FOI PAR!')
        print('Vamos jogar novamente...')
    elif pi == 'I' and rodada != 0:
        vitória += 1
        print(f'Você venceu!! O computador digitou {computador} e você digitou {jogador} e FOI ÍMPAR!')
        print('Vamos jogar novamente...')
    elif pi == 'P' and rodada !=0:
        print(f'Você perdeu!! O computador digitou {computador} e você digitou {jogador} e FOI ÍMPAR!')
        break
    elif pi == 'I' and rodada ==0:
        print(f'Você Perdeu!! O computador digitou {computador} e você digitou {jogador} e FOI PAR!')
        break
print(f'GAME OVER, você venceu {vitória} vezes!' )
