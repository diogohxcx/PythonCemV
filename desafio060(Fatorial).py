n = int(input('Digite um número para saber o seu Fatorial: '))
m = 1
print('A operação de {}! igual A: \033[36m({} x '.format(n, n), end='')
while n >= 1:
    m *= n
    n = (n - 1)
    print('{}'.format(n)[::-1], end='')
    print(' x ' if n > 0 else ')', end='')
print('\n\033[35mResulta em um Fatorial de {}.\033[m'.format(m))