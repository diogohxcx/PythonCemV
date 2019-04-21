frase = str(input('Digite uma frase:')).strip().lower()
frase = frase.replace('á', 'a')
frase = frase.replace('â', 'a')
frase = frase.replace('ã', 'a')
print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A letra A aparece a primeira vez na posição {}'.format(frase.find('a')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.rfind('a')+1))




