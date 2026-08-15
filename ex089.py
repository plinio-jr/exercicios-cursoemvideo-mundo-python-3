#Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
boletim = []
while True:
  nome = str(input('Digite um nome: '))
  nota_1 = float(input('Digite a primeira nota: '))
  nota_2 = float(input('Digite a segunda nota: '))
  media = ((nota_1 + nota_2) / 2)
  boletim.append([nome, [nota_1, nota_2], media])
  opcao = str(input('Quer continuar [S/N]: ')).upper()
  if opcao == 'N':
      break
print(f'{boletim}')