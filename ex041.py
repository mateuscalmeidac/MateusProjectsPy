from datetime import date
atual = date.today().year #por algum motivo da erro(??)
idade = int(input('Digite o seu ano de nascimento: '))
soma = atual - idade
print('O atleta tem {} anos de idade '.format(soma))

if idade <= 9:
    print('Você está classificado na categoria MIRIM ')

elif idade <= 14:
    print('Você está classificado na categoria INFANTIL ')

elif idade <= 19:
    print('Você está na categoria JUNIOR ')

elif idade <= 25:
    print('Você está na categoria SÊNIOR ')

else:
    print('Você está na categoria MASTER ')