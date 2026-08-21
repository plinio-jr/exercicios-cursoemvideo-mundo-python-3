#Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(num, show=True):
  """
  -> Calcula o fatorial de um numero.
  : para num: Numero a ser calculado.
  : parametro show: (opcional) mostra ou nao mostra a conta.
  : return: retorna o valor do fatorial do numero informado(num).
  """
  fat = 1
  for cont in range(num, 0, -1):
    if show:
      print(f"{cont}", end='')
      if cont > 1:
        print(" X ", end='')
      else:
        print(" = ", end='')
    fat *= cont
  return fat


help(fatorial)
num = int(input("Digite um numero: "))
print(fatorial(num, show=True))
