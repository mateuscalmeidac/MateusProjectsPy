n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
print ('O seu primeiro nome é {} '.format (nome[0]))
print ('O seu úlyimo nome é {}' .format (nome[len(nome)-1]))