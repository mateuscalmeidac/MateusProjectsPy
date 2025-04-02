nome = str(input('Qual é o seu nome? '))
valor = float(input('Qual é o valor da casa que você deseja financiar? '))
salario = float(input('Qual é o seu salário {}? '.format(nome)))
tempo = int(input('{},você pretende pagar essa casa em quantos anos? '.format(nome)))
conta = valor / (tempo * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa no valor de R${:.2f} em {} anos'.format(valor,tempo), end='')
print(' a prestação será de {} '.format(conta))

if conta <= minimo:
    print('O impréstimo pode ser concedido')
else:
    print('O financiamento foi NEGADO!!!')
    print ('O valor de cada parcela sera de: R${:.2f} '.format(conta))