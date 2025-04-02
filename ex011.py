salario = float(input('Digite o seu salário para saber o aumento de 15%: '))
aumento = salario * 15 / 100
s = salario + aumento
print ('O seu salário é de {} e com o aumento de {},fica no total de {:.2f} '.format(salario,aumento,s))