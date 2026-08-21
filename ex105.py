#Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
#– Quantidade de notas – A maior nota – A menor nota – A média da turma – A situação (opcional)
def notas(*num, situacao=False):
  """
  -> Função para analisar notas e situacao dos alunos.
  : para num: Uma ou mais notas(aceitam varias dentro do dicionario).
  : parametro situacao: (opcional) deve mostrar a situacao da turma.
  : return: retorna o dicionario com as informações da turma.
  """
  turma = {}
  turma['total'] = len(num)
  turma['maior'] = max(num)
  turma['menor'] = min(num)
  turma['media'] = sum(num) / len(num)
  if situacao:
    if turma['media'] >= 7:
      turma['situacao'] = 'Boa'
    elif turma['media'] >=5:
      turma['situacao'] = 'Razoavel'
    else:
      turma['situacao'] = 'Ruim'
  return turma

help(notas)
resposta1 = notas(2,2,2, situacao=True)
resposta2 = notas(5,6,6.5, situacao=True)
resposta3 = notas(7,7.5,8, situacao=True)
print(resposta1)
print(resposta2)
print(resposta3)