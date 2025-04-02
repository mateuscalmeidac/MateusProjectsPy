from random import randint
from time import sleep
import sys
import rand

#início
print('=-=-=-=-==-=-=' * 10)
resposta = input('Vamos jogar Jogo da Forca? (sim/não): ')
letra1 = 'p'
letra2 = 'y'
letra3 = 't'
letra4 = 'h'
letra5 = 'o'
letra6 = 'n'
palavra = (letra1,letra2,letra3,letra4,letra5,letra6)
chances = 7
letras_usuario = []
print('=-=-=-=-==-=-=' * 10)

if resposta == 'sim':
    print('Vamos começar então...')
    #Continuar programa
else:
    resposta  == 'não'
    print('Finalizando o programa...')
    sys.exit()

iniciar = sleep(2)
#"delay" de 2 Segundos

palavra = random.randint
letra = str(input('Digita a primeira letra: '))

if letra in 'palavra':
    print(letra1)

else:
    print('_')

palavra = random.randint
letra = str(input('Digita a segunda letra: '))

if letra in 'palavra':
    print(letra2)

else:
    print('_')

palavra = random.randint
letra = str(input('Digita a terceira letra: '))

if letra in 'palavra':
    print(letra3)

else:
    print('_')

