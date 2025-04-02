data = int(input('Em que ano você está agora? Vamos descobrir se ele é um ano BISSEXTO: '))
ano = data % 4
if ano == 0:
    print('Sim,o ano {} é um ano Bissexto'.format(data))

else:
    print('Não,o ano {} não é um ano Bissexto! '.format(data))