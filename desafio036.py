valor = float(input('Informe o valor do imovel R$:'))
sal = float(input('Informe o seu salário R$:'))
ano = int(input('Informe em quantos anos você deseja pagar R$:'))
ano2 = ano * 12
sal2 = sal * 30 / 100
valor2 = valor/ano2
if valor2 >= sal2:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} \nSeu empréstimo foi NEGADO!'.format(valor, ano, valor2))
else:
    print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f} \nSeu empréstimo foi APROVADO!'.format(valor, ano, valor2))


