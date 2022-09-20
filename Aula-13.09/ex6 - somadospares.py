#Exercício 06: Escreva um programa que leia os 10 primeiros
#números naturais inteiros imprimindo, no final do
#processamento, a soma de todos os números pares.
i=0

somatorio = 0
while (i<=9):
    print(i)
    if(i%2==0):
        somatorio+=i
    i+=1

print(somatorio)