#Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import sample
from time import sleep
jogos=list()
num=int(input('Quantos jogos?: '))
for contador in range(num):
  quantidade=sorted(sample(range(1, 61), 6))
  jogos.append(quantidade[:])
  print(f'Jogo {contador+1}: {quantidade}')