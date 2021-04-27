"""
O método split quebra um string em uma lista de palavras.
"""
musica = "Eduardo e Monica um dia se encontraram sem querer..."
lista_palavras = musica.split()
print(lista_palavras)

"""
Um argumento opcional chamado de delimitador (delimiter) pode ser usado para especificar quais caracteres serão usados como fronteira de palavras. No exemplo a seguir usamos o string “se”
"""
musica = "Eduardo e Monica um dia se encontraram sem querer..."
lista_palavras = musica.split("se")
print(lista_palavras)

"""
O método join faz o trabalho inverso do método split. Determinamos um string separador (separator), frequentemente chamado de cola (glue) e juntamos os elementos na lista utilizando a cola entre cada par de elemento.
"""
lista = ["vermelho", "azul", "verde"]
cola = ';'
s = cola.join(lista)
print(s)
print(lista)

print("***".join(lista))
print("".join(lista))

# A lista que estamos grudando (lista no exemplo) não é modificada. É possível utilizar qualquer string como cola, inclusive o string vazio.

'''
A função enumarate() retorna um objeto iterável.
'''
for key, value in enumerate(["p", "y", "t", "h", "o", "n"]):
    print(key, value)
