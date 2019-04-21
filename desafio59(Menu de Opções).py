from time import sleep
n1 = int(input('\033[1;33mDigite um valor:\033[m'))
n2 = int(input('\033[1;33mDigite outro valor:\033[m'))
print('**\033[1;34mEscolha o que fazer com os dois valores!\033[m**')
opção = 0
while opção != 7:
    print('''\033[1;35m[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] DIVIDIR
[ 4 ] SUBTRAIR
[ 5 ] MAIOR
[ 6 ] NOVOS NÚMEROS
[ 7 ] TERMINAR O PROGRAMA\033[m''')
    opção = int(input('\033[1;33mEscolha sua opção:\033[m'))
    if opção == 1:
        print('\033[1;31mA soma entre {} e {} é {}\033[m'.format(n1, n2, n1 + n2))
    elif opção== 3:
        divisão = n1 / n2
        print('\033[1;31m A divisão entre {} e {} é {:.2f}\033[m'.format(n1, n2, divisão))
    elif opção == 2:
        print('\033[1;31mA multiplicação entre {} e {} é {}\033[m'.format(n1, n2, n1 * n2))
    elif opção == 4:
        subtração = n1 - n2
        print('\033[1;31mA subtração entre {} e {} é {}\033[m'.format(n1, n2, subtração))
    elif opção == 5:
        if n1 > n2:
            print('\033[1;31mO maior valor digitado é {}\033[m'.format(n1))
        elif n2 > n1:
            print('\033[1;31mO maior valor digitado é {}\033[m'.format(n2))
        else:
            print('\033[1;31mOs valores são iguais.\033[m')
    elif opção == 6:
        print('\033[1;33mInforme novos números!\033[m')
        n1 = int(input('\033[1;33mDigite um valor:\033[m'))
        n2 = int(input('\033[1;33mDigite outro valor:\033[m'))
    elif opção == 7:
        print('\033[1;33mFinalizando...\033[m')
        sleep(3)
    else:
        print('\033[1;31mOpção invalida. Tente novamente!\033[m')
    print('\033[1;36m=*=\033[m'*10)
    sleep(1.5)
print('Fim do programa.')