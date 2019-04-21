km = float(input('Digite a quantidade de kilometros que será percorrido:'))
if km <= 200:
    print('O valor da passagem será de: R${:.2f}'.format(km * 0.50))
else:
    print('O valor da passagem será de: R${:.2f} valor promocional para viagens maiores que 200km!'.format(km * 0.45))