'''
strings são imutáveis (immutable)
listas são mutáveis (mutable)
Uma tupla (tuple), como uma lista, é um sequência de items de qualquer tipo. Entretanto, diferentemente de listas, tuples são imutáveis. 
Apesar de não ser necessário, há a convenção de se envolver uma tupla entre parêntese
Tuplas admitem a mesma sequência de operações que strings e listas.
Como strings, se tentarmos utilizar o operador de atribuição para modificarmos um elemento da tupla, obteremos um erro.
tupla[0] = 'X'
TypeError: 'tuple' object does not support item assignment
'''
# Frequentemente, é útil trocarmos os valores de duas variáveis. Com o comando de atribuição
# Atribuição entre tuplas faz o mesmo serviço de uma maneira muito elegante:
a = (1, 2, 3)
b = (9, 8, 7)
# Naturalmente, o número de variáveis a esquerda e o número de valores a direita devem ser o mesmo.
(a, b) = (b, a)
print(f'a = {a}')  # a = (9, 8, 7)
print(f'b = {b}')  # b = (1, 2, 3)

# convertendo tuplas em lista
b = list(b)
b[2] = 'marcelo'
b = tuple(b)
print(b) # (1, 2, 'marcelo')