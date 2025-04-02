distancia = float(input('Digite a distância da sua viajem em KM: '))
if distancia <=  200:
    soma = distancia * 0.50
    print('Você deverá pagar {:.2f}'.format(distancia))

else:
    soma = distancia * 0.45
    print('Você deverá pagar R$ {:.2f}'.format(soma))