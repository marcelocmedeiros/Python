"""
:s - Texto(strings)
:d - Inteiros(int)
:f - Num. ponto Flutuante (float)
:.(número)f - quantidade de casas decimais (float)
(caractere)(> ou < ou ^)(quantidade)(TIPO - s, d ou f)
> - esquerda
< - direita
^ - centro
"""

# num1 = 10
# num2 = 3

# div = num1/num2
# # print(f'{div:.2f}')
# print('{:.2f}'.format(div))

nome = 'Marcelo'
formatado = '{:@>50}'.format(nome)
print(formatado)

sobrenome = 'campos'
print(f'{sobrenome:@<50}')

ultimo = 'medeiros'
print(f'{ultimo:@^50}')

nome2 = 'Luiz'
nome2 = nome2.ljust(20, '$')
print(nome2)

nome3 = 'Luiz'
nome3 = nome3.rjust(20, '$')
print(nome3)
