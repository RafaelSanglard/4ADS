#  Exercício 03: Escreva um programa qualquer (você dará as
# diretivas para este programa), que permita utilizar pacotes
# (bibliotecas) criadas por você mesmo.

import pacotes.numeros as numeros
# import pacotes.strings

numeros.linha()
print('Dobro ou Tríplo')
numeros.linha()

num = int(input('\nDigite um número: '))

op = str(input('\n[D]obro ou [T]ríplo do Número?')).upper()

if op == 'D':
    print(f'O dobro de {num} é {numeros.dobro(num)}')
elif op == 'T':
    print(f'O tríplo de {num} é {numeros.triplo(num)}')
else:
    print('Opção Incorreta!')