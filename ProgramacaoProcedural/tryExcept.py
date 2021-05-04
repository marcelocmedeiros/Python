'''
Primeiramente, a cláusula try (o conjunto de instruções entre as palavras reservadas try e except ) é executada.
Se nenhuma exceção ocorrer, a cláusula except é ignorada e a execução da instrução try é finalizada.
Se ocorrer uma execução durante a execução da cláusula try, as instruções remanescentes na cláusula são ignoradas.
Se o tipo da exceção ocorrida tiver sido previsto em algum except, então essa cláusula será executada.
 Depois disso, a execução continua após a instrução try.
 Se a exceção levantada não foi corresponder a nenhuma exceção listada na cláusula de exceção, então ela é entregue a uma instrução try mais externa. 
 Se não existir nenhum tratador previsto para tal exceção, trata-se de uma exceção não tratada e a execução do programa termina com uma mensagem de erro.
A instrução try pode ter uma ou mais cláusula de exceção, para especificar múltiplos tratadores para diferentes exceções. 
Tratadores só são sensíveis às exceções levantadas no interior da cláusula de tentativa, e não às que tenham ocorrido no interior de outro tratador numa mesma instrução try.
Um tratador pode ser sensível a múltiplas exceções, desde que as especifique em uma tupla:
'''
from os import sysconf_names


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# A construção try … except possui uma cláusula else opcional, que quando presente, deve ser colocada depois de todas as outras cláusulas. É útil para um código que precisa ser executado se nenhuma exceção foi levantada.
