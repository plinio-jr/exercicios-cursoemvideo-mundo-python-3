#Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas B) A média de idade C) Uma lista com as mulheres D) Uma lista de pessoas com idade acima da média
galera = list()
pessoa = dict()
soma = media = 0
while True:
  pessoa.clear()
  pessoa['nome'] = str(input("Nome: "))
  while True:
    pessoa['sexo'] = str(input("Sexo[M/F]: ")).upper()[0]
    if pessoa['sexo'] in 'MF':
      break
    print("Sexo invalido, responda apenas M ou F!")
  pessoa['idade'] = int(input("idade: "))
  galera.append(pessoa.copy())
  while True:
    resp = str(input("Quer continuar[S/N]: ")).upper()[0]
    if resp in "SN":
      break
    print("Opção invalida, digite apenas S ou N")
  if resp == "N":
    print("Programa encerrado")
    break
  print(f"Ao todos temos {len(galera)} pessoas cadastradas")
  media = soma/len(galera)
  print(f"A media é de {media:.2f}")
  for pes in galera:
    if pes['sexo'] =="F":
      print(f"{pes['nome']}", end=" ")
      print()
  for pes in galera:
    if pes['idade'] >= media:
      print("    ")
    for k, v in pes.items():
      print(f"{k} = {v}", end=" ")
    print()
    print("Fim")