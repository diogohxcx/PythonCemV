print('#-#' * 20)
print('***ANALISANDO TRIANGULOS V2***')
print('#-#' * 20)
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMA um triângulo!', end = '')
    if r1 == r2 == r3:
        print('ÉQUILATERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Ós segmentos acima NÃO PODEM FORMAR triângulo')
    