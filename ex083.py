#Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = []
exp = str(input('Digite uma expressão: '))
for simbolo in expressao:
    if simbolo == '(':
      expressao.append('(')
    elif simbolo == ')':
      if len(expressao) > 0:
        expressao.pop()
      else:
        expressao.append(')')
        break
if len(expressao) == 0:
  print('Sua expressão esta valida')
else:
  print('Sua expressão esta invalida')