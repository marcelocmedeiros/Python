#           índices
#           0123456789........33
frase = 'o rato roeu a roupa do rei de roma'
tamanho = len(frase)

contador = 0
nova_string = ''

while contador < tamanho:
    # print(frase[contador], contador)
    # nova_string += frase[contador]
    # print(nova_string)
    letra = frase[contador]
    if letra == 'r':
        nova_string += 'R'
    else:
        nova_string += letra
    contador +=1
print(nova_string)