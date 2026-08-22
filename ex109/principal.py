import moeda

num = float(input("Digite um valor: R$ "))
print(f"O aumento de 10% é {moeda.aumentar(num, 10, formatacao=True)}")
print(f"A diminuicao de 10% é {moeda.diminuir(num, 10, formatacao=True)}")
print(f"O dobro de R$ {num:,.2f} é {moeda.dobro(num, formatacao=True)}".replace(".", ","))
print(f"A metade de R$ {num:,.2f} é {moeda.metade(num, formatacao=True)}".replace(".", ","))
