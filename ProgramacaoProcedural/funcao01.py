"""
Função é uma sequência de comandos que executa alguma tarefa e que tem um nome.
principal finalidade é nos ajudar a organizar programas em pedaços que correspondam a como imaginamos uma solução do problema.
sintaxe:
def NOME( PARÂMETROS ):
    COMANDOS

A lista de parâmetros pode ser vazia ou conter qualquer número de parâmetros separados pos vírgulas. 

 função precisa de certas informações para poder executar a sua tarefa. Esses valores, frequentemente chamados de argumentos ou parâmetros reais, são passados à função pelo usuário.

Chamadas de função contém o nome da função a ser executada seguida por uma lista de valores, chamados argumentos, os quais são atribuídos aos parâmetros da definição da função.
"""


# def funcao(var):
#     print(var)  # geralmente não usa o print


# variavel = funcao('valor que eu quero')

# print(variavel)  # retorna um None um não valor

# Return 
'''
O comando return é seguido de uma expressão que é calculada. Seu valor é retornado a quem chama a função como o fruto da chamada da função. 
Todas as funções em Python retornam None
a menos que explicitamente exista um comando return com um valor diferente de None
'''

def funcao(var):
    return var  # sempre q a função enconrtar a return encerra a função 
    print('Isso não será executado!')

variavel = funcao('valor que eu quero')

print(variavel)  # retorna um None um não valor

"""
Var Um comando de atribuição em uma função cria uma variável local para a variável à esquerda do =. Esta variável existe somente dentro da função e não pode ser usada fora dela. 

Python procura para variáveis que são definidas localmente na função. Chamamos isso de escopo local. Se o nome da variável não é encontrado no escopo local, então Python procura nas variáveis globais, ou escopo global. Isto é exatamente o caso ilustrado no código acima. expoente não é encontrada localmente em
Quando uma variável local tem o mesmo nome de uma variável global, dizemos que a variável local esconde a global. Isso quer dizer que a variável global não pode ser acessada porque a variável local é encontrada primeiro.
"""
