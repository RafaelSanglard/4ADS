#Exercício 02: Escreva um programa que crie uma lista
#denominada estoque, que será composta por dicionários, que
#apresentam os seguintes itens: código, nome, marca,
#quantidade, preço. Então, seu programa deverá permitir ao
#usuário fornecer, via teclado (input), dez produtos que irão
#compor seu estoque.
#No final do processamento, imprimir todos os produtos do
#estoque.

estoque = list()
item=dict()
for i in range (0,10):
  print("\n item:",i+1)
  item['Codigo']      = input('Informe o codigo do item: ')
  item['Nome']        = input('Digite o nome do item: ')
  item['Marca']       = input('Marca: ')
  item['Quantidade']  = input('Quantidade: ')
  item['Preco']       = input('Preço: ')
  estoque.append(item.copy( ))
print(estoque)