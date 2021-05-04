'''
filter => cria uma lista de elementos para os quais uma função retorna verdadeiro. 
Em palavras simples, o filter() método filtra o iterável dado com a ajuda de uma função que testa cada elemento no iterável para ser verdadeiro ou não.
filter () Parâmetros
função - função que testa se os elementos de um iterável retornam verdadeiro ou falso.
iterável - iterável que deve ser filtrado, pode ser conjuntos , listas , tuplas ou contêineres de qualquer iterador

 filter() filtra os elementos de uma sequência. 
 O processo de filtragem é definido a partir de uma função que o programador passa como primeiro argumento da função.
 ilter() só “deixa passar” para a sequência resultante aqueles elementos para os quais a chamada da função que o usuário passou retornar True.
'''
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']

    if(letter in vowels):
        return True
    else:
        return False

filtered_vowels = filter(filter_vowels, letters)

print('As vogais filtrada são:')
for vowel in filtered_vowels:
    print(vowel)