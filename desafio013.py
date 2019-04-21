print('Feito por mim')
sal = float(input('Qual o salario do funcionario? R$:'))
aumento = sal + (sal *15/100)
print('O funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(sal, aumento))
