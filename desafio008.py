medida = float(input('Digite uma distancia em metros:'))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida /10
hm = medida /100
km = medida /1000
print('A conversão de {}m para centimetro é {:.0f}cm.'.format(medida, cm))
print('A conversão de {}m para milimetro é {:.0f}mm.'.format(medida, mm))
print('A conversão de {}m para decimetro é {:.0f}dm'.format(medida, dm))
print('A conversão de {}m para decametro é {}'.format(medida, dam))
print('A conversão de {}m para hectometro é {}'.format(medida, hm))
print('A conversão de {}m para kilometro é {}'.format(medida, km))

