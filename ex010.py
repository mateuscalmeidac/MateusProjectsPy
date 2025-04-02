preco = float(input('Digite o preço do produto para saber o desconto de 5%: '))
desconto = preco * 5 / 100
s = preco - desconto
print ('O valor de {} com {} de desconto aplicado,fica no total de: {} '.format(preco,desconto,s))