#Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
lista = []
while True:
  num = int(input("Digite um numero: "))
  if num not in lista:
    lista.append(num)
    print('Valor adicionado com sucesso!')
  else:
    print('Valor duplicado')
  opcao = str(input('Quer continuar [S/N]: ')).upper()
  if opcao in 'Nn':
    break
print(f'Você digitou os valores: {sorted(lista)}')