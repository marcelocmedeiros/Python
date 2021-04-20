contador = 1
acumulador = 1
while contador <= 8:
    print(contador, acumulador)
    acumulador = contador + acumulador
    contador += 1
else:
    print('Cheguei no else.')
