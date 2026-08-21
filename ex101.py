#Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(ano):
  from datetime import date
  atual = date.today().year
  idade = atual- ano
  if idade <= 16:
    return f"Com {idade} anos: VOTO NEGADO"
  elif idade >= 16 and idade < 18:
    return f"Com {idade} anos: VOTO OPCIONAL"
  elif idade >= 18 and idade <= 65:
    return f"Com {idade} anos: VOTO OBRIGATORIO"
  else:
    return f"Com {idade} anos: VOTO OPCIONAL"


ano = int(input("Ano de nascimento: "))
print(voto(ano))