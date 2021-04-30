'''
1) O range(5) é um objeto iterável (que pode ser usado em uma estrutura de repetição) que provê, a cada iteração (ou ciclo do loop), um valor diferente à variável i.
 Iterator facilita muito a criação de um objeto iterável, 
 Para criá-locodificamos uma classe e basta que ela implemente os seguintes métodos:
    __iter__: Esse métodos deve retornar o próprio objeto (self) para ser utilizado em loops com for e in.

    __next__: Esse método deve retornar o próximo valor da iteração. Caso a condição de para seja satisfeita, ou seja, quando não houver mais objetos a iterar, ela deve lançar o erro StopIteration.
Para criar um Generator basta definir uma função e utilizar a palavra reservada yield, ao invés de return.
Um generator só pode ser consumido uma única vez.
Para utilizá-lo novamente, é necessário criá-lo ou instanciá-lo novamente.
generators otimizam a utilização de memória, pois não guardam grandes 
estruturas na memória da sua máquina.
'''
# Generators e Listas

# Listas podem ser criadas através de objetos iteravéis.

a = list(range(5))
print(a)

