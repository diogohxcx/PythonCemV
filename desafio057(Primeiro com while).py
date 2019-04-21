s = str(input('Iforme seu sexo [M/F]:')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Opção digitada é invalida, por favor informe seu sexo [M/F]:')).strip().upper()[0]
print('Sexo {} registrado com sucesso!'.format(s))
