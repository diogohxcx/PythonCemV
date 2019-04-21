listatemp = []
lista = []
while True:
    aluno = str(input('Informe o nome do Aluno: '))
    listatemp.append(aluno)
    nota1 = float(input('Digite a 1º nota: '))
    listatemp.append(nota1)
    nota2 = float(input('Digite a 2º nota: '))
    listatemp.append(nota2)
    lista.append(listatemp[:])
    listatemp.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'N':
       break
print('-=' * 30)
print(f'{"Nº":<4}{"Nome":<8}{"Média":>8}')
print('-' * 22)
for c, n in enumerate(lista):
    print(f'{c:<4}{n[0]:<8}{(n[1]+n[2])/2:>8.1f}')
print('-' * 22)
while True:
    num = int(input('Informe o número do aluno para saber suas notas, ou [999 para finalizar]:  '))
    if num == 999:
        break
    if num <= len(lista) - 1:
        print(f'As notas do {lista[num][0]} são {lista[num][1]}, {lista[num][2]}')
print(len(lista))
