nome = "Marcelo"
idade = 43
altura = 1.73
peso = 75
imc = peso / (altura ** 2)
print(nome, 'tem', idade, 'anos de idade seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
