#Exercício 01: Escreva um programa que crie uma lista
#denominada locadora, que será composta por dicionários, que
#apresentam os seguintes itens: titulo, ano e diretor. Então,
#seu programa deverá permitir ao usuário fornecer, via teclado
#(input), cinco filmes que irão compor sua locadora.
#No final do processamento, imprimir todos os filmes da
#locadora.

locadora = list()
item=dict()
for i in range (0,5):
  print("\n Filme:",i+1)
  item['titulo']  = input('Informe o titulo do filme: ')
  item['ano']     = input('Digite o ano do filme: ')
  item['diretor'] = input('Nome do diretor do filme: ')
  locadora.append(item.copy( ))

print(locadora)
  