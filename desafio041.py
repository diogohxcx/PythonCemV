from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano em que nasceu:'))
idade = atual - nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade <= 14:
    print('Sua categoria é INFANTIL!')
elif idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade <= 25:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MASTER!')


