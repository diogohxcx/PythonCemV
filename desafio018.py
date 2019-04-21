from math import sin, cos, radians,  tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))
