#Exercício 02: Você foi contratado pelo posto de gasolina
#RENALF para elaborar um programa que:
#- Ao abastecer, o controlador da bomba de Álcool, Diesel,
#Gasolina ou GNV fornecerá ao seu programa a quantidade de
#litros que foi consumida por cada cliente;
#
#Ao final do dia, quando não houverem mais clientes a
#consumirem Álcool, Diesel, Gasolina ou GNV, o programa
#deverá gerar um relatório para informar:
#- a quantidade de litros consumidos de Álcool, Diesel,
#Gasolina e GNV;
#- quantos clientes consumiram Álcool, Diesel, Gasolina e
#GNV;
#
#- o valor total arrecadado para cada tipo de combustível
#consumido (Álcool, Diesel, Gasolina e GNV) durante o dia.
#
#Observação: Tomar como base a tabela de preços por litro de
#combustível praticado no posto.
#
#Tabela de Preços por Litro de Combustível
#
# Álcool: R$ 5,69
# Diesel: R$ 2,96
# Gasolina: R$ 6,07
# GNV: R$ 4,15

total = list()
combustivel=dict()
combustivel = {'nome':'Gasolina', 'preço':1.67, 'Total':0}
total.append(combustivel)
combustivel = {'nome':'Alcool', 'preço':5.69, 'Total':0}
total.append(combustivel)
combustivel = {'nome':'GNV', 'preço':4.15, 'Total':0}
total.append(combustivel)
combustivel = {'nome':'Diesel', 'preço':2.69, 'Total':0}
total.append(combustivel)

qtd=1
i=0
while(qtd!=0):
  print("\n item:",i)
  nomeitem      = input('Nome do combustivel: ')
  qtd = int(input('Quantidade: '))
  for combustivel in total:
      if (combustivel["nome"] is nomeitem):
          combustivel["Total"]+=combustivel["preço"]*qtd
print(total)