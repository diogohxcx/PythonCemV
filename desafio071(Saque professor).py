print('=' * 20)
print('{: ^20}'.format('BANCO CEV'))
print('=' * 20)
valor = int(input('Qual valor você gostaria de sacar? R$:'))
total = valor
cédula = 100
totalCédula = 0
while True:
    if total >= cédula:
        total -= cédula
        totalCédula += 1
    else:
        if totalCédula > 0:
            print(f'Total de {totalCédula} cédulas de R${cédula}')
        if cédula == 100:
            cédula = 50
        elif cédula == 50:
            cédula = 20
        elif cédula == 20:
            cédula = 10
        elif cédula == 10:
            cédula = 1
        totalCédula = 0
        if total == 0:
            break
print('=' * 20)
print('Obrigado e volte sempre!')
