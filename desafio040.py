print('*' * 30)
print('### VAMOS CALCULAR SUA MÉDIA ###')
print('*' * 30)
n1 = float(input('Informe a primeira nota:'))
n2 = float(input('Informe a segunda nota:'))
media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, media))
if media >= 7:
    print("Parabéns está APROVADO!")
elif media >= 5 and media < 7:
    print('Precisa estudar mais, você está de RECUPERAÇÃO!')
else:
    print('Infelizmente você foi REPROVADO!')

