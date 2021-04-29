'''
Conjuntos (sets) em Python
=> é uma coleção de itens únicos (distintos).
Python permite criar sets de várias formas:
1- criar um set a partir de uma lista de elementos.
2- criar um conjunto vazio e inserir elementos nele à medida que desejarmos

'''
# Exemplo de criação de sets.
numeros = [1, 2, 2, 3, 3, 3]
numeros_distintos = set(numeros)
print("Números: ", numeros)
print("Números distintos: ", numeros_distintos)

# diferença de inserção de elementos em listas e conjuntos => em uma lista, podemos usar a função insert ou a função append | => para inserir um elemento em um set podemos usar somente a função add
# Exemplo de criação de sets.
numeros = [1, 2, 2, 3, 3, 3]
numeros_distintos = set() 
for num in numeros:
    numeros_distintos.add(num) 
print("Números: ", numeros)
print("Números distintos: ", numeros_distintos)
'''
diferença é que em uma lista temos um controle da posição dos elementos: insert nos permite inserir um elemento em uma posição específica da lista e append adiciona um elemento ao final da lista.
Já em um set não temos controle sobre a ordem na qual os elementos são armazenados.
única garantia que temos é que elementos duplicados não serão inseridos.
'''
# Outra diferença é ao percorrer uma lista, sabemos que os elementos serão percorridos na ordem em que foram armazenados nela, mas em um set não temos esse controle

# Como remover elementos de um conjunto => usar a função remove ou a função discard.
nums = set([1, 2, 2, 3, 3, 3])
nums.remove(2)
print("Números: ", nums)

# A função remove deve ser usada somente se tivermos certeza que o elemento está presente no conjunto, pois se o elemento não estiver presente, a função remove causa uma exceção

# a função discard, que remove um elemento do conjunto se o elemento estiver presente mas não faz nada caso contrário.

nums = set([1, 2, 2, 3, 3, 3])
nums.discard(4) 
nums.discard(2)
print(nums)
#  não estar presente no conjunto, nenhum erro é retornado ao tentarmos removê-lo.

# Python nos permite remover todos os elementos de um conjunto de uma vez. Para isso precisamos usar a função clear

nums = set([1, 2, 2, 3, 3, 3])
print("Números: ", nums) # Números: {1, 2, 3}
nums.clear()
print("Números: ", nums) # Números: set()

# 	Esta notação é a forma de Python indicar um conjunto vazio. Talvez você estivesse esperando ver {} impresso aqui, mas {} é a forma que Python usa para indicar um dicionário vazio. Por isso, para evitar confusão, quando imprimimos um conjunto vazio, Python imprime set() ao invés de {}


#  Operações matemáticas com sets

#Um set em Python é uma representação de um conjunto na matemática.
# Assim como na matemática temos: união, interseção e diferença de conjuntos, set realizar essas mesmas operações de forma muito eficiente.
# conjuntos união
A = {0, 1, 3, 5, 7, 9} 
B = {0, 2, 4, 6, 8}
C = A.union(B)
# C = A | B # forma mais concisa
print(C)

# conjuntos interseção

A = {0, 1, 3, 5, 7, 9}
B = {0, 2, 4, 6, 8}
C = A & B 
# C = A.intersect(B) # outra forma de fazer interseção
print(C)

'''
Python nos permite realizar muitas outras operações com conjuntos

Símbolo|matemático	    Operador Python	    Descrição
    e∈S                      in             elemento e é membro de S
    A⊆B                      <=             A é um subconjunto de B
    A⊂B                      <              A é um subconjunto próprio de B
    A∪B                      |              A união com B
    A∩B                      &              A interseção com B
    A∖B                      -              diferença entre A e B
'''

