print('#' * 40)
print('Este programa faz conversões de números inteiros\npara binário, octal e  hexadecimal.')
print('#' * 40)
num = int(input('Digite um valor para ser convertido:'))
print('''Escolha uma das bases para conversão: 
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('O número {} em BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('O número {} em OCTAL é {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('O número {} em HEXADECIAL é {}'.format(num, hex(num)[2:]))
else:
    print('Você digitou uma opção invalida, tente novamente.')