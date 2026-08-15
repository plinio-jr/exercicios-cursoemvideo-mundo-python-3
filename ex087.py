#Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
somapar = terceiracoluna = segundacoluna= 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for num in range(0,3):
  for matrizes in range(0,3):
    matriz[num][matrizes] = int(input(f'Digite um valor para {num}, {matrizes}: '))
print('-='*15)
for num in range(0,3):
  for matrizes in range(0,3):
    print(f'[{matriz[num][matrizes]}]', end='')
    if matriz[num][matrizes] % 2 ==0:
      somapar += matriz[num][matrizes]
  print()
print(f'O valor da soma dos pares é {somapar}')
for num in range(0,3):
  terceiracoluna += matriz[num][2]
print(f'A soma da terceira coluna é: {terceiracoluna}')
for c in range(0,3):
  if c ==0:
    segundacoluna = matriz[1][c]
  elif matriz[1][c]> segundacoluna:
    segundacoluna = matriz[1][c]
print(f'O maior valor da segunda linha e: {segundacoluna}')