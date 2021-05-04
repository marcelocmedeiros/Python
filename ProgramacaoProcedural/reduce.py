'''
reduce() => Sua utilidade está na aplicação de uma função a todos os valores do conjunto, de forma a agregá-los todos em um único valor.
é uma função realmente útil para realizar alguns cálculos em uma lista e retornar o resultado.
Ele aplica um cálculo contínuo a pares sequenciais de valores em uma lista. 
é outra função builtin do Python (deixou de ser builtin e passou a estar disponível no módulo functools a partir da versão 3000)
reduce() foi retirada do conjunto de builtins de Python, em parte devido à obscuridade que pode acabar gerando
'''
product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
print(product)
# foram reduzida
from functools import reduce
product1 = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(product1)