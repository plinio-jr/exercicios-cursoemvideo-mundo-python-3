#Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
primeira = []
final = []

while True:
  primeira.append(str(input('Nome: ')))
  primeira.append(float(input('Peso: ')))
  final.append(primeira[:])
  primeira.clear()
  opcao = str(input('Quer continuar? [S/N] ')).upper()
  if opcao =='N':
    break
print(f'Ao todo, você cadastrou {len(final)} pessoas')
print(f'O maior peso foi de {max(final)} KG')
print(f'O menor peso foi de {min(final)} KG')