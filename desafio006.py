#print('Progama realizado por mim para solução do 6 desafio')
#n1 = int(input('Digite um numero:'))
#n2 = n1 * 2
#n3 = n1 * 3
#n4 = n1 ** (1/2)
#print('O dobro do seu numero é {} , o triplo é {} e a raiz é {}'.format(n2, n3, n4))

print('\033[1;33mSolução do professor\033[m')
n = int(input('\033[1;34mDigite um numero:\033[m'))
#d = n * 2
#t = n * 3
#r = n ** (1/2)
#print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}'.format(n, d, n, t, n, r))
#Solução usando apenas uma variavel
print('\033[1;34mO dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}\033[m'.format(n, (n*2), n, (n*3), n, (n**(1/2))))
