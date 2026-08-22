#Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
cor = {
    'reset': '\033[0m',
    'vermelho': '\033[91m',
    'verde': '\033[92m',
    'amarelo': '\033[93m',
    'azul': '\033[94m',
    'magenta': '\033[95m',
    'ciano': '\033[96m',
    'branco':'\033[37m',
}

print(f"{cor['verde']}~"*30)
print(f"{cor['verde']}Sistema de Ajuda Pyhelp")
print(f"{cor['verde']}~"*30)

while True:
  escolha = str(input(f'{cor['azul']}Biblioteca ou Função: ')).strip().lower()
  help(f'{escolha}')
  if escolha =='fim':
    break
print(f'{cor['vermelho']}Ate Logo')