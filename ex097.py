#Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. Ex: escreva(‘Olá, Mundo!’) Saída:  ~~~~~~~~~
#                                                                                                                                                                                                           Olá Mundo! 
#                                                                                                                                                                                                           ~~~~~~~~~
def escreva(mensagem):
  tamanho = len(mensagem) + 4
  print('~'* tamanho)
  print(mensagem)
  print('~'* tamanho)



escreva('curso em video')
escreva('Python')