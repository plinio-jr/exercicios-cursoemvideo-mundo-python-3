#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
maior = 0
menor = 0
valores = []
for contador in range(0,5):
  valores.append(int(input(f'Digite um numero para a posicao {contador}: ')))
  if contador ==0:
    maior = menor = valores[contador]
  else:
    if valores[contador]> maior:
      maior = valores[contador]
    if valores[contador] < menor:
      menor = valores[contador]
print(f'Voce digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posição ', end='')
for inicio, valor in enumerate(valores):
  if valor == maior:
    print(f'{inicio}...', end='')
    print()
print(f"O menor valor digitado foi {menor} nas posição ", end='')
for inicio, valor in enumerate(valores):
  if valor == menor:
    print(f'{inicio}...', end='')
print('Fim do programa!')