'''
Python, map(), para aplicar uma função a cada item em um iterável (como uma lista ou um dicionário) e retornar um novo iterador para recuperar os resultados. map() retorna um objeto map (um iterador), que podemos usar em outras partes do nosso programa. 
'''
# sintaxe para a função map() é a seguinte:

# map(function, iterable, [iterable 2, iterable 3, ...])map(function, iterable, [iterable 2, iterable 3, ...])

def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))