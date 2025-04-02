from datetime import date
atual = date.today ().year
nasc = int(input('Digite a seu ano de nascimento: ' ))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {} '.format(nasc,idade,atual))

if idade == 18:
    print("Você tem que se alistar imediatamente")

elif idade < 18:
    saldo = 18 - idade
    print('Ainda Faltam {} anos para você se alistar'.format(saldo))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos '.format(saldo))

