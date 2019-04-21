print('#' * 31)
print('***GERENCIADOR DE PAGAMENTOS***')
print('#' * 31)
valor = float(input('Informe o valor da compra:'))
print('''ESCOLHA A FORMA DE PAGAMENTO:
[ 1 ] PARA PAGAMENTO À VISTA DINHEIRO/CHEQUE
[ 2 ] PARA PAGAMENTO À VISTA NO CARTÃO
[ 3 ] PARA DIVIDIR EM 2X NO CARTÃO
[ 4 ] PARA DIVIDIR EM 3X OU MAIS''')
opção = int(input('Digite uma opção:'))
if opção == 1:
    print('O valor é R${:.2f} com o desconto fica em R${:.2f}'.format(valor, valor - (valor *10)/100))
elif opção == 2:
    print('O valor é R${:.2f} com o desconto fica em R${:.2f}'.format(valor, valor - (valor *5)/100))
elif opção == 3:
    total = valor
    parcela = total/2
    print('O valor é R${:.2f} dividido em 2x de R${:.2f} sem juros!.'.format(valor, parcela))
elif opção == 4:
    parcelas = int(input('Quantas parcelas?'))
    valor2 = valor + (valor * 20) / 100
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas, valor2/parcelas))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final.'.format(valor, valor + (valor * 20)/100))
else:
    print('Opção invalida, tente novamente!')


