#Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
pessoa={'nome': str(input("nome: ")),
        'idade': int(input('idade: ')),
        'carteira': int(input('Carteira de trabalho (0 não tem): ')),
        'ano': int(input('Ano de contratação: ')),
        'salario':float(input("Salario: R$"))}
if pessoa['carteira'] == 0:
  print('A pessoa ainda não trabalha')
  print(f"nome: {pessoa['nome']}")
  print(f"idade: {pessoa['idade']}")
  print(f"ctps: {pessoa['carteira']}")
else:
  print(pessoa)
  print(f"nome: {pessoa['nome']}")
  print(f"idade: {pessoa['idade']}")
  print(f"ctps: {pessoa['carteira']}")
  print(f"ano de contratação: {pessoa['ano']}")
  print(f"Salario: {pessoa['salario']}")
  calculo = {pessoa['ano'] + 35}
  print(f"A aposentadoria tem um valor: {calculo}")