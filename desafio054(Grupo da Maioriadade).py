from datetime import date
atual = date.today().year
cont = 0
cont2 = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu?'.format(c)))
    idade = atual - ano
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1
print('Maior de idade são {} e menores são {}'.format(cont, cont2))
