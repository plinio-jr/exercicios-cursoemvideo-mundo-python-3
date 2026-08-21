#Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: num = leiaInt(‘Digite um n: ‘)
def leiaInt(texto):
  ok = False
  valor = 0
  while True:
    num = str(input("Digite um numero inteiro: "))
    if num.isnumeric():
      valor = int(num)
      ok = True
    else:
      print("ERRO! Digite um numero valido!")
    if ok:
      break
  return valor

num = leiaInt("Digite um numero inteiro: ")
print(f"O numero digitado foi {num}")