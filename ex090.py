#Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.
aluno = {}
aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input("Media: "))
print("-="*30)
if aluno['media'] <= 5:
  aluno['situacao'] = 'Reprovado'
elif aluno['media'] <=6.9:
  aluno['situacao'] = 'Recuperação'
elif aluno['media']<=10:
  aluno['situacao'] = 'Aprovado'
print(aluno)