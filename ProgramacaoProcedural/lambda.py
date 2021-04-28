'''
Expressões => funções anônimas podem ser criadas com a palavra-chave lambda. 
funções lambda podem ser usadas sempre que objetos função forem necessários
são sintaticamente restritos a uma única expressão
'''
# sintaxe
a = lambda x,y: x*y
print(a(3,4))

lista = [
    ['p1', 13], 
    ['p2', 6], 
    ['p3', 7], 
    ['p4', 50], 
    ['p5',8],
]


lista.sort(key=lambda item: item[1], reverse=True)
print(sorted(lista, key=lambda item: item[1], reverse=False))# ordenado pela [1]
print(sorted(lista, key=lambda item: item[0], reverse=False))# ordenado pela [0]
print(lista)
