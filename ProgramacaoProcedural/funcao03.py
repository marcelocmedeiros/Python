'''
Escopo Global e Local
não se pode alterar a variavel global dentro de uma função
para uma variavel local ser alterado use a palavra global => NÃO É UMA BOA PRÁTICA NÃO DEVE-SE FAZER
'''
variavel = 'valor'


def func():
    print(variavel)


def func2():
    # global variavel
    variavel = 'Outro valor'
    print(variavel)


func()
func2()
print(variavel)
