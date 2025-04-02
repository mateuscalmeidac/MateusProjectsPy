salario = float(input('Digite o seu salário para saber o seu aumento: '))
if salario <= 1250.00:
    novo = salario + (1250.00 * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. '.format(salario,novo))