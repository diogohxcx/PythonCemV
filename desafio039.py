from datetime import date
print('*' * 30)
print("***PROGRAMA PARA ALISTAMENTO MILITAR***")
print('*' * 30)
nasc = int(input('Ano de nascimento: '))
print(''''Informe o sexo para continuar
Digite [ 1 ] para Feminino:
Digite [ 2 ] para Masculino:''')
opção = int(input('Sua opção:'))
atual = date.today().year
idade = atual - nasc
if opção == 1:
    print('Mulheres não tem obrigação de alistamento Militar.')
    print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
elif idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))



