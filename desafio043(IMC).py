print('#' * 30)
print('***CALCULADORA DE IMC***')
print('#' * 30)
peso = float(input('Informe seu peso? (Kg):'))
altura = float(input('Informe seu altura? (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é {:.1f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso, Se alimente melhor!')
elif imc <= 25:
    print('Parabéns você esta no seu peso ideal!')
elif imc <= 30:
    print('Se cuide, você está com sobrepeso!')
elif imc <= 40:
    print('Precisa imagrecer você está com obesidade!')
else:
    print('Procure um médico você está com Obesidade mórbida!')


