#Exercício Python 096: Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
print("Controle de Terreno")
print("-"*30)
largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

def area(largura, comprimento):
  calculo = largura * comprimento
  print(f"A area de um terreno de {largura} m X {comprimento} m é {calculo}m²")


area(largura, comprimento)