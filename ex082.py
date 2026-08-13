#Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
lista = []
lista_par = []
lista_impar = []
while True:
  num = int(input('Digite um numero: '))
  if num not in lista:
    lista.append(num)
    print('Valor adicionado com sucesso')
  if num % 2 ==0:
    lista_par.append(num)
  if num % 2==1:
    lista_impar.append(num)
  opcao = str(input('Quer continuar:')).upper()
  if opcao =='N':
    break
print(f'A lista completa é {lista}')
print(f'A lista de numeros pares é {sorted(lista_par)}')
print(f'A lista de numeros impares é {sorted(lista_impar)}')