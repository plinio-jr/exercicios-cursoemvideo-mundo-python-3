from ex115.lib.interface import mensagem, menu


def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    with open('cursoemvideo.txt', 'r', encoding='utf-8') as arq:
        for linha in arq:
            print(linha.strip())
    try:
        arq = open(nome, 'rt')
    except:
        print("Erro ao ler o arquivo!")
    else:
        mensagem('pessoas cadastradas')
        for row in arq:
            pessoa = row.split(';')
            pessoa[1] = pessoa[1].replace('\n', ' ')
            print(f'{pessoa[0]:<30} {pessoa[1]:>3} anos')
        print(arq.read())
    finally:
        arq.close()


def cadastro(arquivo, nome='desconhecido', idade=0):
    try:
        arq = open(arquivo, 'at')
    except:
        print("Erro ao ler o arquivo!")
    else:
        try:
            arq.write(f'<30{nome};{idade}3>')
        except:
            print("houve um erro ao salvar o usuario!")
        else:
            print("Usuario salvo com sucesso")
            arq.close()