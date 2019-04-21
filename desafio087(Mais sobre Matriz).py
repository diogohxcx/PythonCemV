matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = tercoluna = seglinha = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor par [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
#    if matriz[1][c] == 0:
#        seglinha = matriz[1][c] Minha solução, ficou enorme!
#    else:
#        if matriz[1][c] > seglinha:
#            seglinha = matriz[1][c]
#        if matriz[1][c] < seglinha:
#            seglinha = matriz[1][c]
    print()
print('-=' * 30)
print(f'A soma dos números pares é {par}')
for l in range(0, 3):
    tercoluna += matriz[l][2]
print(f'A soma da 3º coluna é {tercoluna}')
for c in range(0, 3):
    if c == 0:
        seglinha = matriz[1][c] # Solução do professor!
    elif matriz[1][c] > seglinha:
        seglinha = matriz[1][c]
print(f'O maior número da 2º linha é {seglinha}')


