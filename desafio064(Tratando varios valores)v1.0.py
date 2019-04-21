n = 0
cont = 0
soma = 0
n = int(input('Digite um número ou \033[1;31m[999Para finalizar!]\033[m'))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número ou \033[1;31m[999Para finalizar!]\033[m'))
print(f'Você digitou {cont} valores e a soma deles é {soma}')
