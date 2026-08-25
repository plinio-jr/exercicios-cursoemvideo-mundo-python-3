#Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
import requests

try:
  site = 'https://www.pudim.com.br/'
  check = requests.get(site)
  print('Esta acessivel!')
except:
  print("site indisponivel")