nota1 = float(input('Digite uma nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f} , a média do aluno é de {:.1f} '.format(nota1, nota2, media))
if 7 > media >= 5:
    print('O aluno está de RECUPERAÇÃO!!!!!!!!')
elif media < 5:
    print('Aluno REPROVADO!!!!!!!!!')
elif media >= 7:
    print('Aluno APROVADO!!!!!! ')