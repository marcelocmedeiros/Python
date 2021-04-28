'''
Ele é um tipo de mapeamento nativo do Python
A associação, ou mapeamento, é feita a partir de uma chave, que pode ser qualquer tipo imutável, para um valor, que pode ser qualquer objeto de dados do Python.
Os valores em um dicionário são acessados com chaves, não com índices, por isso não há necessidade de se preocupar com a ordenação.
maneira de criar um dicionário é fornecer uma lista de pares chave-valor 
'''
# craindo dicionários
d1 = dict(chave1='a', chave2='b', chave3='c')
print(d1)

# Operações com dicionários

# O comando del=>remove um par chave-valor de um dicionário. 
inventario = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
del inventario['peras']
print(inventario)

#Dicionários também são mutáveis. Como vimos antes, com listas, isso significa que o dicionário pode ser modificado pela referência a uma associação no lado esquerdo de um comando de atribuição. 
inventario = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
inventario['peras'] = 0
print(inventario)

#

inventario = {'kiwis': 430, 'bananas': 312, 'laranjas': 525, 'peras': 217}
inventario['bananas'] += 200
print(inventario)
numItems = len(inventario)
print(numItems)
print(len(inventario))

# Métodos de dicionários
'''
Método      Parâmetros      Descrição

keys        nenhum      Retorna as chaves no dicionário

values      nenhum      Retorna os valores no dicionário

items       nenhum      Retorna os pares chave-valor no dicionário

get         key         Retorna o valor associado com a chave; ou None

get         key,alt     Retorna o valor associado com a chave; ou alt

'''
# iterar com for
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

for k in inventory:
   print("Chave obtida", k)

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(list(inventory.values()))
print(list(inventory.items()))

for (k,v) in inventory.items():
    print("Chave",k,"tem o valor de",v)

for k in inventory:
    print("Chave",k,"tem o valor de",inventory[k])

# Os operadores in e not in podem testar se uma chave está no dicionário:

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    print(inventory['bananas'])
else:
    print("Nós não temos bananas")

'''
O método get nos permite acessar o valor associado a uma chave, similar ao operador []. A diferença importante é que get não irá causar um erro de execução se a chave não está presente. Ao invés disso, retorna None. Existe uma variação de get que permite o retorno de um valor alternativo quando a chave não está presente.
'''

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}

print(inventory.get("apples"))
print(inventory.get("cherries"))

print(inventory.get("cherries",0))

# os dicionários são mutáveis.Sempre que duas variáveis se referem ao mesmo objeto no dicionário, a mudança de uma afeta a outra

opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}
alias = opposites

print(alias is opposites)

alias['right'] = 'left'
print(opposites['right'])

# Se você deseja modificar um dicionário e manter uma cópia do original, use o método copy de dicionários. 
opposites = {'up': 'down', 'right': 'wrong', 'true': 'false'}

acopy = opposites.copy()
print(acopy is opposites)   # False
acopy['right'] = 'left'
print(opposites['right'])   # wrong

