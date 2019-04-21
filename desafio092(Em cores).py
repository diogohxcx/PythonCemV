# Exercício Python 092:
# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os, com idade,
# em um dicionário se por acaso a CTPS for diferente de zero,
# o dicionário também receberá o ano de contratação e o salário.
# Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'vermelho': '\033[1;31m',
         'sublinhado': '\033[4m',
         'bold': '\033[1;30m',
         'pretoBranco': '\033[7;30m'}
print(f'\n{cores["pretoBranco"]}{" Cadastro de Trabalhador em Python ".title().center(40)}{cores["limpa"]}\n')
contribuinte = dict()
for c in range(0, 1):                                                               # range([start], stop[, step])
    contribuinte['nome'] = str(input('Nome: ')).strip().title()
    ano = int(input('Ano de Nascimento: '))
    idade = datetime.now().year - ano
    contribuinte['idade'] = idade
    contribuinte['ctps'] = int(input('Carteira de Trabalho [0 se não tem]: '))
    if contribuinte['ctps'] == 0:
        break
    contribuinte['contratação'] = int(input('Ano de Contratação: '))
    contribuinte['salário'] = float(input('Salário: R$ '))
    contribuinte['aposentadoria'] = (contribuinte['contratação'] + 35) - ano
print('-' * 55)
print(contribuinte)
print('-' * 55)
for chave, valor in contribuinte.items():
    print(f'\t- {chave.title()} tem o valor {cores["amarelo"]}{valor}{cores["limpa"]}.')
print('-=' * 28)