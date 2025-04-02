from random import randint
from time import sleep
computador = randint(0,5)
print('=====' * 5)
print('VAMOS BRINCAR??????')
print('=====' * 5)
jogador = int(input('Digite um número que vá de 0 a 5: '))
print('P R O C E S S A N D O...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!! Você advinhou o número ')
else:
    print('VOCÊ ERROU!! Tente novamente ')
print ('---FIM---')