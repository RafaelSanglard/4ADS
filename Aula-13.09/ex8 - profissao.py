#Exercício 08: Escreva um programa que leia nome e sua
#profissão, imprimindo, no final do processamento, o nome e
#seu respectivo salário, com base na seguinte regra:
#Profissão = “Programador”, o salário é 1500
#Profissão = “Analista”, o salário é 2800
#Profissão = “Operador”, o salário é 980
#Profissão = “Digitador”, o salário é 800
#Qualquer profissão diferente das anteriores, mostrar a
#seguinte mensagem: “Salário não informado!”.
nome = input("Digite o nome: ")
prof = input("Digite sua profissão: ")


if(prof.lower=='programador'):
    Salario = 1500
elif(prof.lower=='analista'):
    Salario = 2800
elif(prof.lower=='operador'):
    Salario = 980
elif(prof.lower=='digitador'):
    Salario = 800
else:
    print("Salario não informado.")
    Salario = 0

if(Salario!= 0):
    print("Profissão = ",prof," o salário é de: ", Salario)
