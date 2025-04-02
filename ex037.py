num = int(input('Digite um número para converter em Binário,Octal ou Hexadecimal: '))
print ('''Escolha uma das bases para conversão: 
[ 1 ] Binário
[ 2 ] Octal
[ 3 ] Hexadecimal ''')
opcao = int(input('Digite a sua opção: '))
if opcao == 1:
    print('{} Convertido para Binário é igual á {} '.format(num,bin(num)[2:]))

elif opcao == 2:
    print('{} Convertido para Octal é {} '.format(num,oct(num)[2:]))

elif opcao == 3:
    print('{} Convertido para Hexadecimal é {} '.format(num,hex(num)[2:]))

else:
    print('Opção inválida')
