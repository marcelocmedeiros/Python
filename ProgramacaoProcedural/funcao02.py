'''
Parâmetros: são os nomes dados aos atributos que uma função pode receber. Definem quais argumentos são aceitos por uma função, podendo ou não ter um valor padrão (default).

Argumentos: são os valores que realmente são passados para uma função.

'''
def calculadora_salario(valor, horas=220):
    return horas * valor

valor_total = calculadora_salario(299.25)

print(valor_total)
'''
os parâmetros obrigatórios devem ser colocados antes de qualquer parâmetro default (da esquerda para direita), para que não ocorra uma confusão no interpretador e ocorra o erro
'''
'''
*args
É usado para passar um lista de argumentos variável sem palavras-chave em forma de tupla, pois a função que o recebe não necessariamente saberá quantos argumentos serão passados.
'''
def func_args(*args):
    print(f'tipo: {type(args)} conteúdo: {args}')
    for arg in args:
        print(f'tipo: {type(arg)} conteúdo: {arg}')


func_args(1, 'A', {'valor': 10})

'''
**kwargs
Como a abreviação sugere, kwargs significa keyword arguments (argumentos de palavras chave). Ele permite passar um dicionário com inúmeras keys para a função.
'''
def func_kwargs(**kwargs):
    print(f'tipo: {type(kwargs)} contuedo: {kwargs}')
    for key, value in kwargs.items():
        print(f'atributo: {key}, valor: {value}')

func_kwargs(nome='James', sobrenome='Bond', cargo='Agente 007')

# um função usando todos os parâmetros que vimos.

def func_missao_dificil(nome, *args, funcao='agente', **kwargs):
    print(f'Nome do agente: {nome}')
    print(f'Função: {funcao}')
    print(args)
    print(kwargs)

params = {
            'id_agente': '007',
            'proxima_missao': 'Impossível'
         }

func_missao_dificil(
    'James Bond',
    'Missao 1',
    'Missão 2',
    **params
)