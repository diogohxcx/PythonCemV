print('-='* 30)
print('Sequencia de Fibonacci!')
print('-=' * 30)
total = int(input('Informe a quantidade de termos: '))
t1 = 0
t2 = 1
cont = 3
print('~' * 30)
print('{} - {}'.format(t1, t2), end='')
while cont <= total:
    t3 = t1 + t2
    cont += 1
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
print(' - FIM')
print('~' * 30)


