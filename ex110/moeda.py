def aumentar(num=0, taxa=0, formatacao=False):
    resultado = num + (num * taxa/ 100)
    return resultado if formatacao is False else moeda(resultado)

def diminuir(num=0,taxa=0, formatacao=False):
    resultado = num - (num * taxa/ 100)
    return resultado if formatacao is False else moeda(resultado)

def dobro(num=0, formatacao=False):
    resultado = num * 2
    return resultado if formatacao is False else moeda(resultado)

def metade(num=0, formatacao=False):
    resultado = num / 2
    return resultado if formatacao is False else moeda(resultado)

def moeda(num=0, moeda="R$"):
    return f"{moeda}{num:,.2f}".replace(".",",")

def resumo(num=0, taxaA=10, taxaD=5):
    print('-'*30)
    print('Resumo dos valores'.center(30))
    print('-'*30)
    print(f"Valor informado: {moeda(num)}")
    print(f"O aumento de 10% é {aumentar(num, taxaA, True)}")
    print(f"A diminuicao de 5% é {diminuir(num, taxaD, True)}")
    print(f"O dobro de R$ {num:.2f} é {dobro(num, True)}".replace(".", ","))
    print(f"A metade de R$ {num:.2f} é {metade(num, True)}".replace(".", ","))
    return resumo