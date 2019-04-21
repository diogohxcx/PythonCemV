nunex = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Quartoze', 'Quinze', 'Desesseis', 'Desesete', 'Desoito', 'Desenove', 'Vinte')
cont = 0
while True:
    num = int(input('Digite um número entre 0 e 20:'))
    if 0 < num > 20:
        cont += num
        cont + 1
        print('Tente novamente, Digite um número entre 0 e 20!')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]:')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Você o digitou {nunex[num]}')
print(f'Você digitou {cont} valores validos!')


