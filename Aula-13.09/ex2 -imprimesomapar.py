#Exercício 02: Escreva um programa que leia um número inteiro
#imprimindo no final do processamento, a soma desse número
#por ele mesmo, caso ele seja um número par, ou, imprima a
#subtração desse número por ele mesmo, caso ele seja um
#número ímpar.
n = int(input("Digite um numero inteiro: "))
if(n%2==0):
    print("n+n = ", n+n)
else:
    print("n - n = ", n-n)