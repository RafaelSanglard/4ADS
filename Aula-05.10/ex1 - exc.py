#  Exercício 01: Escreva um programa qualquer (você dará as
# diretivas para este programa), que obrigatoriamente, deverá
# apresentar tratamento de Erro e Exceção.
try:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    prod = n1*n2
    div = n1/n2
except:
    print('Houve uma falha na operação! ')
else:
    print(f'O produto de {n1} por {n2} é igual a {prod}')
    print(f'A divisão de {n1} por {n2} é igual a {div}')