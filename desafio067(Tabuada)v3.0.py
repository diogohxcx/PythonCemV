cont = 0
while True:
    num = int(input('Iforme um numero para saber sua Tabuada!:'))
    if num < 0:
        break
    for cont in range(1, 11):
        print(f'{cont} x {num} = {cont * num}')
print('Fim!')

