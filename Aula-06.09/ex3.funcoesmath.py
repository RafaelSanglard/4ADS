import math
n1=float(input("Digite o primeiro numero: "))

op=int(input("O que deseja fazer com ele? 1- Raiz quadrada, 2 - exponenciação, 3 arredondar para cima, 4 - arredondar para baixo: "))

match op:
    case 1:
        print(math.sqrt(n1))
    case 2:
        n2=int(input("Digite o segundo numero: "))
        print(pow(n1,n2))
    case 3:
        print(math.ceil(n1))
    case 4:
        print(math.floor(n1))