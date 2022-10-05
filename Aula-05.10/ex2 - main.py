#  Exercício 02: Escreva um programa qualquer (você dará as
# diretivas para este programa), que permita utilizar novas
# funções e módulos criados por você.
import ex2func

ex2func.linha()
print('Dobro ou Tríplo')
ex2func.linha()

num = int(input('\nDigite um número: '))

op = str(input('\n[D]obro ou [T]ríplo do Número?')).upper()

if op == 'D':
    print(f'O dobro de {num} é {ex2func.dobro(num)}')
elif op == 'T':
    print(f'O tríplo de {num} é {ex2func.triplo(num)}')
else:
    print('Opção Incorreta!')