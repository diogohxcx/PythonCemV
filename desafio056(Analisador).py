somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('---{}ºPESSOA---'.format(p))
    nome = str(input('Nome:')).strip().upper()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip()
    somaidade += idade  # (é igual a isso "somaidade = somaidade + idade"
    if p == 1 and sexo in 'Mm':  # 1 equivale ao primeiro laço!
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mn' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos.'.format(mediaidade))
print('O homem mais velho é o {} e sua idade é {} anos.'.format(nomevelho, maioridadehomem))
print('São {} do sexo feminino abaixo de 20 anos.'.format(totmulher20))
