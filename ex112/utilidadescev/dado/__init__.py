def leiaDinheiro(txt):
    valid= False
    valor = str(input(txt)).replace('.', ',').strip()
    while not valid or valor == '':
        if valor.isalpha():
            print(f"Erro: {valor} é um preço invalido!")
        else:
            valid= True
            return float(valor)

