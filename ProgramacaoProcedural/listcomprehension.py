'''
=>  é uma maneira compacta de criar listas
sintaxe:
        [expr for item in lista]
'''
minha_lista = [1, 2, 3, 4, 5]

sua_lista = [item ** 2 for item in minha_lista]

print(sua_lista)

uma_lista = [4,2,8,6,5]
outra_lista = [num*2 for num in uma_lista if num%2==1]
print(outra_lista)



lista = ["oi", 2.0, 5, [10, 20]]
lista_aninhada = lista[3]
print(lista_aninhada)
item = lista_aninhada[1]
print(item)

print(lista[3][1])
# => a expressão expr em cada item da lista.       
#       [expr for item in lista if cond]
# => Aplique a expressão expr em cada item da lista caso a condição cond seja satisfeita.

resultado = [numero for numero in range(20) if numero % 2 == 0]
print(resultado)

# Listas aninhadas => é uma lista que aparece como um elemento em uma outra lista.

# Utilizando múltiplos if's e list comprehensions

resultado = [numero for numero in range(100) if numero % 5 == 0 if numero % 6 == 0]

print(resultado)

 # utilizar expressões condicionais e list comprehension é usar o conjunto if + else.
# sintaxe: [resultado_if if expr else resultado_else for item in lista]

# para cada item da lista, aplique o resultado resultado_if se a expressão expr for verdadeira, caso contrário, aplique resultado_else.

resultado = ['1' if numero % 5 == 0 else '0' for numero in range(16)]
print(resultado)


# Múltiplas List Comprehensions (aninhadas)

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposta = [[linha[i] for linha in matriz] for i in range(4)]
print(transposta)

'''
No código acima:

=> No primeiro loop, i assume o valor de 0, portanto [linha[0] for linha in matriz] vai retornar o primeiro elemento de cada linha: [1, 4, 9]

=> No segundo loop, i assume o valor de 1, portanto [linha[1] for linha in matriz] vai retornar o segundo elemento de cada linha: [2, 5, 10]

=> No terceiro loop, i assume o valor de 2, portanto [linha[2] for linha in matriz] vai retornar o terceiro elemento de cada linha: [3, 6, 11]

=> No quarto loop, i assume o valor de 3, portanto [linha[3] for linha in matriz] vai retornar o quarto elemento de cada linha: [4, 8, 12]
'''