#Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
#cont = 0
lista = []
while True:
  num = int(input('Digite um numero: '))
  if num not in lista:
    lista.append(num)
    #cont += 1
    print('Valor adicionado com sucesso!')
  opcao = str(input('Quer continuar [S/N]: ')).upper()
  if opcao == 'N':
    break
print(f"Voce digitou {len(lista)} elementos")
print(f'Os valores em ordem decrescente são: {sorted(lista, reverse = True)}')
if 5 in lista:
  print('O valor 5 faz parte da lista')
else:
  print('O valor 5 não faz parte da lista')