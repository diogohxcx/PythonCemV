cont = 0
soma = 0
while True:
    num = int(input('Digite um número, para parar digite [999]:'))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Você digitou {cont} números e a soma entre eles é {soma}!')

