#Exercício 01: A prefeitura do Rio de Janeiro está em ritmo de
#eleições. Apresentaram-se três candidatos: Antonio com o
#número 1; José com o número 2 e Maria com o número 3.
#
#Cada eleitor marca uma cédula com sua opinião (opção), que
#pode ser:
#[1] Antonio
#[2] José
#[3] Maria
#[4] BRANCO
#[*] NULO
#Elabore um programa que receba e processe os dados de cada
#cédula, emitindo um relatório informativo com as seguintes
#informações:
#- Número de votos de cada uma dos três candidatos;
#- O nome do candidato vitorioso;
#- O número total de eleitores que compareceram às urnas.
#
#Observações:
#(1) A votação só será encerrada quando foi digitado o n
#o 0
#
#(zero) para encerrar o processo de votação;
#(2) Em caso de empate imprima a seguinte mensagem:
#“VOTAÇÃO EM SEGUNDO TURNO”.
urna = list()
votacao = list()
candidato=dict()
candidato = {'nome':'Antonio', 'numero':1, 'votos':0}
votacao.append(candidato)
candidato = {'nome':'Jose', 'numero':2, 'votos':0}
votacao.append(candidato)
candidato = {'nome':'Maria', 'numero':3, 'votos':0}
votacao.append(candidato)
candidato = {'nome':'BRANCO', 'numero':4, 'votos':0}
votacao.append(candidato)

numero=1
while(numero!=0):
  print("\n Eleitor:",numero-1)
  
  numero=int(input('Digite o numero do candidato: '))
  for candidato in votacao:
      if candidato["numero"] == numero:
          print("Confirma o voto no candidato",candidato["nome"],'?')
          conf = int(input("0 - sim | 1 - Não:"))
          if(conf==0):
              candidato['votos']+=1
              urna.append(candidato.copy( ))
          else:
              print("Retornando a tela inicial")
              
print("leitura da urna")
print(urna)
print("Resumo")
print(votacao)