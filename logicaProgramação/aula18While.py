"""
A while é uma instrução usada para execução repetida, desde que uma expressão seja verdadeira:
break é uma instrução quando executada ela termina o loop sem executar as demais instruções
continue é uma instrução quando executada ela ignora o restante do código e volta a testar a expressão.
"""
x = 0
while x < 5:
    if x == 3:
        x = x + 1
        continue
        # break    
    print(x)
    x = x + 1
print('Acabou!')

