velocidade= float(input('Digite a velocidade que o carro estava andando para saber se vocÊ foi multado: '))
if velocidade > 80:
    print('Você foi multado! Pois execedeu o limite da rodovia. ')
    multa = (velocidade - 80) * 7
    print('Você deve pagar o total de R${} de multa  '.format(multa))
print('Tenha um Bom- Dia! Dirija com segurança! ')