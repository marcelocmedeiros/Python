# Input sempre retor uma string

nome = input('Qual seu nome? ')
idade = input('Qual a sua idade? ')

ano_nascimento = 2021 - int(idade)
print()
print(f'O usuário digitou {nome} e o tipo davariável é '
      f'{type(nome)}')
print()
print(f'{nome} tem {idade} anos.'
      f'E nasceu no {ano_nascimento}')
