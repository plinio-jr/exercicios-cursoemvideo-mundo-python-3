#Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
def leiaInt(texto):
    while True:
        try:
            num = int(input(texto))
        except (ValueError, TypeError):
            print('ERRO! por favor digite um numero inteiro valido!')
            continue
        except (KeyboardInterrupt):
            print("O usuario não informou os dados!")
            break
        else:
          return num


def leiaFloat(txt):
    while True:
        try:
            texto = float(input(txt))
        except (ValueError, TypeError):
            print('ERRO! por favor digite um numero inteiro ou float valido!')
            continue
        except (KeyboardInterrupt):
            print("O usuario não informou os dados!")
            break
        else:
          return texto


int = leiaInt('Digite um numero inteiro: ')
flo = leiaFloat('Digite um numero float: ')
print(f"O numero informado foi {int}")
print(f"O numero informado foi {flo}")
