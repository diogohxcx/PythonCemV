print('=== DADOS DO TRABALHADOR ===')
from _datetime import datetime
trabalhador = dict()
for c in range(0, 1):
    trabalhador['nome'] = str(input('Nome: '))
    ano = int(input('Ano de Nascimento: '))
    trabalhador['idade'] = datetime.now().year - ano
    trabalhador['CPTS'] = int(input('Carteira de trabalho(0 não tem): '))
    if trabalhador['CPTS'] == 0:
        break
    anocont = int(input('Ano de Contratação: '))
    trabalhador['contratação'] = anocont
    trabalhador['aposentadoria'] = trabalhador['idade'] + ((trabalhador['contratação'] +35) - datetime.now().year)
    trabalhador['salario'] = float(input('Salário: '))
print('-=' * 18)
print('== SEGUE OS DADOS DO TRABALHADO ==')
print('-=' * 18)
for i, v in trabalhador.items():
    print(f' - {i} tem o valor {v}')

