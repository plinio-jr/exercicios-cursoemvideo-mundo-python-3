#Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
def maior(*num):
  print(f"Os valores informados foram {num} ao todo")
  print(f"O maior valor informado foi {max(num)}")


maior(2,9,4,3)
maior(8,3,7,5,1)
maior(3, 2, 1)