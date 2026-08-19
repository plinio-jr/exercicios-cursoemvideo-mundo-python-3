#Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint

def sorteia(lista):
  for contador in range(0,5):
    num = randint(1, 10)
    lista.append(num)
    print(f"{num}")

def somaPar(lista):
  soma = 0
  for num in lista:
    if num % 2 == 0:
      soma += num
  print(f"Os valores pares de {lista}, temos: {soma}")


numeros = list()
sorteia(numeros)
somaPar(numeros)
