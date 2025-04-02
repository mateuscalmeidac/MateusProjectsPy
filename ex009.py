largura = float(input('Digite a largura da parede que você deseja pintar: '))
altura = float(input('Digite a altura da parede que você deseja pintar: '))
area = largura * altura
print ('Sua parede tem a dimensão de {} x {} e a sua área é de {:.3f}m². '.format(largura,altura,area))
tinta = area / 2
print ('Para pintar a parede,será necessario {:.3f}L de tinta.'.format(tinta))