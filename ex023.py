num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print ('Análisando o número {} '.format(num))
print ('A unidade é {}'.format(u))
print ('A dezena é {}'.format(d))
print ('A centena é {}'.format(c))
print ('A milhar é de {}'.format(m))
