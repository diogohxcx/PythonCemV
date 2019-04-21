print('Feito por mim.')
km = float(input('Quantos kilometros foram rodados?:'))
dias = int(input('Quantos dias de alguel?:'))
total = km * 0.15 + dias * 60
print('Total a pagar é: R${:.2f}'.format(total))

