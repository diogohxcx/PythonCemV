# EXERCICIO EXECUTADO CRIANDOS LISTAS PARA OS NÚMEROS MAIORES E MENORES #
#maiorvalor= []
#menorvalor= []
#valores = []
#for cont in range(0, 5):
#    valores.append(int(input(f'Digite um valor para a Posição {cont}:')))
#for pos, v in enumerate(valores):
#    if v == max(valores):
#        maiorvalor.append(pos)
#    if v == min(valores):
#        menorvalor.append(pos)
#print(f'Os valores digitados foram {valores}')
#print(f'O maior valor da lista foi {max(valores)} na posição {maiorvalor}')
#print(f'O menor valor da lista foi {min(valores)} na posição {menorvalor}')



# EXERCICIO EXECUTADO PELO PROFESSOR USANDO A TECNICA PARA ENCONTRAR O MAIOR E O MENOR VALOR #


men = 0
mai = 0
valores = []
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('-=' * 30)
print(f'Os valores adicionados a lista foram {valores}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f'{i}...', end=' ')
print()
print(f'O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f'{i}...', end=' ')
