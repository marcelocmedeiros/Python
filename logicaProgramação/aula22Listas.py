"""
Lista em Python
Uma lista (list) em Python é uma sequência ou coleção ordenada de valores.
identificado por um índice. 
listas são mutáveis
Listas são similares a strings, que são uma sequência de caracteres, no entanto, diferentemente de strings, os itens de uma lista podem ser de tipos diferentes.

a função "LEN" retorna o comprimento de uma lista (o número de elementos na lista). 
cessar um elemento de uma lista é a mesma usada para acessar um caractere de um string. Nós usamos o operador de indexação ( [] – não confundir com a lista vazia).

"""
# Pertinência em uma Lista
# in e not in são operadores booleanos ou lógicos que testam a pertinência (membership) em uma sequência.
frutas = ["maca", "laranja", "banana", "cereja"]

print("maca" in frutas)
print("pera" not in frutas)

# Concatenação e repetição
# como com strings, o operador + concatena listas. Analogamente, o operador * repete os itens em uma lista um dado número de vezes.

frutas = ["maca", "laranja", "banana", "cereja"]
print([1, 2] + [3, 4])
print(frutas + [6, 7, 8, 9])

print([0] * 4) # operador * repete os itens em uma lista
print([1, 2, ["ola", "adeus"]]*2)

# Fatias de listas
# A operação de fatiar (slice) que vimos com strings também pode ser aplicada sobre listas. 
# Lembre que o primeiro índice indica o ponto do início da fatia e o segundo índice é um depois do final da fatia (o elemento com esse índice não faz parte da fatia).
uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:]) # copia rasa da lista

# Listas são mutáveis
# Diferentemente de strings, listas são mutáveis (mutable). Isto significa que podemos alterar um item em uma lista acessando-o diretamente como parte do comando de atribuição.

frutas = ["banana", "maca", "cereja"]
print(frutas)

frutas[0] = "pera"
frutas[-1] = "laranja"
print(frutas)

# Remoção em listas
# O comando del remove um elemento de uma lista usando a sua posição.

a = ['um', 'dois', 'três']
del a[1]
print(a)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
del lista[1:5]
print(lista)

# Clonando listas

a = [81, 82, 83]
b = a[:]       # cria um clone com fatia
print(a is b)
6	
b[0] = 5
print(a)
print(b)

# Métodos de listas
"""
Método      Parâmetros     Resultado   Descrição

append      item           mutador     Acrescenta um novo item no final da lista

insert    posição, item    mutador     Insere um novo item na posição dada

pop         nenhum         híbrido      Remove e returno o último item

pop         posição        híbrido      Remove e retorna o item da posição.

sort        nenhum         mutador      Ordena a lista

reverse     nenhum         mutador      Ordena a lista em ordem reversa

index       item           retorna idx  Retorna a posição da primeira ocorrência do item

count       item           retorna ct   Retorna o número de ocorrências do item

remove      item           mutador      Remove a primeira ocorrência do item
"""
# clear() Remove todos os itens de uma lista. Equivalente a del a[:].

# copy() Devolve uma cópia rasa da lista. Equivalente a a[:].



minha_lista = []
minha_lista.append(5)
minha_lista.append(27)
minha_lista.append(3)
minha_lista.append(12)
print(minha_lista)

minha_lista.insert(1, 12) 
print(minha_lista)
print(minha_lista.count(12))

print(minha_lista.index(3))
print(minha_lista.count(5))

minha_lista.reverse()
print(minha_lista)

minha_lista.sort()
print(minha_lista)

minha_lista.remove(5)
print(minha_lista)

ultimo_item = minha_lista.pop()
print(ultimo_item)
print(minha_lista)
