#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print(f"Os numeros sorteados foram: {num}")
print(f"O maior numero foi: {max(num)}")
print(f"O menor numero foi: {min(num)}")