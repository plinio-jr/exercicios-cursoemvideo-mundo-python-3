#Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.
matriz = []
num = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for num in range(0,3):
  for matrizes in range(0,3):
    matriz[num][matrizes] = int(input(f'Digite um valor para {num}, {matrizes}: '))
print('-='*15)
for num in range(0,3):
  for matrizes in range(0,3):
    print(f'[{matriz[num][matrizes]}]', end='')
  print()