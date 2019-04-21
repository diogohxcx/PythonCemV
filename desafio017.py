#opst = float(input('Informa o valor do cateto oposto:'))
#adja = float(input('Informe o valor do cateto adjacente:'))
#hi = (opst ** 2 + adja ** 2) **(1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
co = float(input('Informe o comprimento do cateto oposto:'))
ca = float(input('Informe o comprimento do cateto adjacente'))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))




