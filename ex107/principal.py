from ex107 import moeda

num = float(input("Digite um valor: R$ "))
print(f"O aumento de 10% é {moeda.aumentar(num, 10)}")
print(f"A diminuicao de 10% é {moeda.diminuir(num, 10)}")
print(f"O dobro de {num} é {moeda.dobro(num)}")
print(f"A metade de {num} é {moeda.metade(num)}")
