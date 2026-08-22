import moeda

num = float(input("Digite um valor: R$ "))
print(f"O aumento de 10% é {moeda.moeda(moeda.aumentar(num, 10))}")
print(f"A diminuicao de 10% é {moeda.moeda(moeda.diminuir(num, 10))}")
print(f"O dobro de R$ {num:,.2f} é {moeda.moeda(moeda.dobro(num))}".replace(".", ","))
print(f"A metade de R$ {num:,.2f} é {moeda.moeda(moeda.metade(num))}".replace(".", ","))
