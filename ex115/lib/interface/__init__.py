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

def linha(tamanho=30):
    return '-' * tamanho

def mensagem(texto):
    print(linha())
    print(texto.center(30))
    print(linha())

def menu(lista):
    mensagem('MENU PRINCIPAL')
    contador=1
    for escolha in lista:
        print(f'{contador} - {escolha}')
        contador += 1
    print(linha())
    opcao = leiaInt("Sua opção: ")
    return opcao