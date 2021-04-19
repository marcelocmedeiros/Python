usuario = input('Digite seu nome: ')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))
print(len(usuario))
print(usuario.__len__()) # em Python tudo é um objeto no caso len é metodo que conta os caracteres do tipo strings