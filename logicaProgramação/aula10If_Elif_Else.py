"""
O comando if (que significa se em português) permite que uma parte do programa seja executada apenas quando uma condição for verdadeira. A sintaxe do comando If é a seguinte:
    if condição_do_if:
    # bloco executado se a condição for verdadeira
    Bloco de código 
comando_após_if
Comando if-else
Em várias ocasiões é necessário executar blocos de forma alternativa. Nesses casos, podemos utilizar o comando if-else (que significa se-senão em português), cuja sintaxe é a seguinte:
If condição:
    # bloco só será executado se a condição for verdadeira
    Bloco de código    
else:
    # senão será executado o bloco abaixo
    Bloco de código
comando_apos_if


Comando if-elif-else
Para simplificar ainda mais o código de programas com if-else aninhados, o Python oferece o comando if-elif-else.

Usando esse comando poderíamos escrever o programa para saber a condição de um aluno da seguinte forma:
"""
nota = int(input("Digite uma nota: "))

if nota < 4:
    print("Reprovado")
elif nota < 7:
    print("Recuperacao")
else:
    print("Aprovado")

print("fim.")