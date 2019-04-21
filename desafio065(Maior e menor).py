resp = 'S'
soma = 0
quantidade = 0
maior = 0
menor = 0
while resp in 's'.upper():
    num = int(input('Digite um número:'))
    soma += num
    quantidade += 1
    if quantidade == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Deseja continuar [S/N]:')).upper().strip()[0]
    while resp != 'S' and resp != 'N':
        resp = str(input('Opção invalida tente -> [S/N]:')).upper().strip()[0]
print(f'A soma dos valores digitados é {soma} e a média é {quantidade}')
print(f'O maior número informado é {maior} e o menor é {menor}')
print('Fim')

