r1 = float(input("Primeiro Segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(' Os segmentos podem formar um triângulo ', end = '' )
    if r1 == r2 == r3:
        print("EQUILÁTERO")
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos não podem formar um triângulo ')