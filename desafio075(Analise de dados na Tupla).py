num = (int(input('Digite um número:')), int(input('Digite outro número:')), int(input('Digite outro número:')), int(input('Digite mias um número:'))
       ,int(input('Digite agora outro número:')), int(input('Digite e o ultimo número:')))
print(f'Você digitou os seguintes valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 aparece a primeira vez na  {num.index(3)+1}º posição!')
else:
    print('O valor 3 não aparece na lista!')
print('Os números pares são: ', end='')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
