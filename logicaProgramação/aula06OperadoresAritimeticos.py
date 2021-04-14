"""
Operador	Descrição

+	        adição
–	        subtração
*	        multiplicação
/	        divisão
//	        Divisão trunca a parte fracionaria
%	        Produz o resto da divisão
**	        Exponenciação
abs(x)	    Retorna o valor absoluto de x
pow(x, y)	O mesmo x**y
round(x, n)	Retorna um int ou float arredondado para n casas decimais se n for dado
()          altera a precedência dos calculos

1-          ( n + n ) - Os parênteses têm a maior precedência, contas dentro deles são realizadas primeiro

2-          ** - Depois vem a exponenciação

3-          * / //  % - Na sequência multiplicação, divisão, divisão inteira e módulo

4-          +  - - Por fim, soma e subtração
"""
print('Adição +', 10 + 10)
#print('contatena strings =>', 'Marcelo' + 'Campos')
print('Subtração -', 10 - 10)
print('Multiplicação *', 10 * 10)
#print('Multilica strings =>' 'Marcelo ' * 3)
print('Divição /', 10 / 10)

print('Divição truncada //', 10 // 3)
print('Modulo(resto) %', 10 % 3)
print('Potência **', 10 ** 3)

print(abs(-3.567))
print(pow(10, 3))
print(round(10.45678, 2))
