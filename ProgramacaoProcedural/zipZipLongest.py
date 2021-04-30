from itertools import zip_longest, count

indice = count() # só usar com zip

cidades = ['são paulo', 'salvador', 'natal', 'recife', 'cuiabá']

estados = ['sp', 'ba', 'rn', 'pe']

cidades_estados = zip(indice, estados, cidades)
print(list(cidades_estados))

cidades_estados2 = zip_longest(estados, cidades)
print(list(cidades_estados2))

cidades_estados3 = zip_longest(estados, cidades, fillvalue='Estado')
print(list(cidades_estados3))