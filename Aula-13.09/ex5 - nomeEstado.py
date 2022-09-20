#Exercício 05: escreva um programa que leia o nome e uma
#letra correspondente a um Estado Civil, conforme regra a
#seguir:
nome = input("Digite o nome: ")
IniEst = input("A inicial do estado civil: ")
if(IniEst[0]=='S'):
    Estado = "Solteiro"
if(IniEst[0]=='C'):
    Estado = "Casado"
if(IniEst[0]=='V'):
    Estado = "Viuvo"
if(IniEst[0]=='D'):
    Estado = "Divorciado"
if(IniEst[0]=='O'):
    Estado = "Outros"
print(nome)
print(Estado)