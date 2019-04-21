sal = float(input('Informe o salário:'))
if sal >= 1250:
    print('O aumento para este salário é de 10%, totalizando {:.2f}.'.format(sal + (sal * 10 / 100)))
else:
    print('O aumento para este salário é de 15%, totalizando {:.2f}'.format(sal +(sal * 15 / 100)))
