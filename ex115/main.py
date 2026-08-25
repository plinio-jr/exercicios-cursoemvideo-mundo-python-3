from ex115.lib.interface import *
from ex115.lib.interface import mensagem
from ex115.lib.arquivo import *

arquivo = 'cursoemvideo.txt'

if not arquivoExiste(arquivo):
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa','Sair do sistema'])
    if resposta == 1:
        lerArquivo(arquivo)
    elif resposta == 2:
        mensagem('Novo Cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('idade: ')
        cadastro(arquivo, nome, idade)
    elif resposta == 3:
        print("Finalizando...")
        break
    else:
        print("Opção invalida!")
