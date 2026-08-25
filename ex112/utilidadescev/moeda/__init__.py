def aumentar(n=0, taxa=0, formatacao=False):
    '''
    Calcula o aumento de um determinado valor, retornando o resultado com ou sem formatação.
    :param n: o valor que sera reajustado.
    :param taxa: o valor que sera aumentado.
    :param formatacao: se o valor sera formatado ou não.
    :return: o valor reajustado, com ou sem a formatacao
    '''
    resultado = n + (n * taxa/ 100)
    return resultado if formatacao is False else moeda(resultado)

def diminuir(n=0,taxa=0, formatacao=False):
    '''
    Calcula a diminuicao de um determinado valor, retornando o resultado com ou sem formatação.
    :param n: o valor que sera reajustado.
    :param taxa: o valor que sera diminuido.
    :param formatacao: se o valor sera formatado ou não.
    :return: o valor reajustado, com ou sem a formatacao
    '''
    resultado = n - (n * taxa / 100)
    return resultado if formatacao is False else moeda(resultado)

def dobro(n=0, formatacao=False):
    '''
    Calcula o dobro de um determinado valor, retornando o resultado com ou sem formatação.
    :param n: o valor que sera reajustado.
    :param formatacao: se o valor sera formatado ou não.
    :return: o valor reajustado, com ou sem a formatacao
    '''
    resultado = n * 2
    return resultado if formatacao is False else moeda(resultado)

def metade(n=0, formatacao=False):
    '''
    Calcula a metade de um determinado valor, retornando o resultado com ou sem formatação.
    :param n: o valor que sera reajustado.
    :param formatacao: se o valor sera formatado ou não.
    :return: o valor reajustado, com ou sem a formatacao
    '''
    resultado = n / 2
    return resultado if formatacao is False else moeda(resultado)

def moeda(n=0, moeda="R$"):
    '''
    Realizara a conversao para o formato de real, com R$ e virgula.
    '''
    return f"{moeda}{n:.2f}".replace(".",",")

def resumo(n=0, taxaA=0, taxaD=0):
    '''
    Ira mostrar todos os resultados formatados.
    '''
    print('-'*30)
    print('Resumo dos valores'.center(30))
    print('-'*30)
    print(f"Valor informado: {moeda}")
    print(f"O aumento de 10% é {aumentar(n, taxaA, True)}")
    print(f"A diminuicao de 5% é {diminuir(n, taxaD, True)}")
    print(f"O dobro de R$ {n:.2f} é {dobro(n, True)}".replace(".", ","))
    print(f"A metade de R$ {n:.2f} é {metade(n, True)}".replace(".", ","))
    return resumo