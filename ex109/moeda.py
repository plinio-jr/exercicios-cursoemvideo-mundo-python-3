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