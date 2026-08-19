#Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2
#c) uma contagem personalizada
def contador(inicio, fim, passo):
  if passo > 0:
     passo *=1
  if passo ==0:
      passo = 1
  print('-'*30)
  print(f"contagem de {inicio} a {fim} de {passo} em {passo}")
  if inicio < fim:
    conta = inicio
    while conta <= fim:
      conta +=passo
      print(f'{conta} ', end='')
      print()
    print("Fim")
    print('-'*30)
    print()
  else:
    conta = inicio
    while conta >= fim:
      conta -= passo
      print(f'{conta} ', end='')
      print()
    print("Fim")
    print()


contador(0, 9, 1)
contador(12, 1, 2)
print('-'*30)
print("Personalize a contagem:")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print(f"contagem de {inicio} a {fim} de {passo} em {passo}")
contador(inicio, fim, passo)
