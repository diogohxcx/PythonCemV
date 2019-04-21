print('-' *20)
print('CADASTRE UMA PESSOA')
print('-' * 20)
total18 = 0
totalH = 0
totalM = 0
while True:
    idade = int(input('Informe a idade:'))
    sexo = ' '
    resp = ' '
    if idade >= 18:
        total18 += 1
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]:')).upper().strip()[0]
    if sexo == 'M':
        totalH += 1
    elif sexo == 'F' and idade <= 20:
        totalM += 1
    while resp not in 'SN':
        resp = str(input('Deseja continuar cadastrando? [S/N]:')).upper().strip()[0]
    if resp == 'N':
        break
print(f'Maiores de idade cadastrados são:{total18}\nQuantidade de Homens cadastrados são:{totalH}\nQuantidade de Mulheres com menos de 20 anos são:{totalM} ')