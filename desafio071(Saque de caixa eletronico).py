m = [100, 50, 20, 10, 5, 2]
valor = int(input('Quanto você deseja sacar? '))
for i in range(0, len(m)):
    n = 0
    while valor != m[i] + 1 and valor != m[i] + 3 and valor >= m[i]: #NÃO INTENDI ESSA LINHA!
        valor -= m[i]
        n += 1
    if n > 0:
        print(f'Cédulas de {m[i]}: {n}')
