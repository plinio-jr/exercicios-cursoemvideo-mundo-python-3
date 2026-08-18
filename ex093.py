#Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
total = int(input(f'quantas partidas {jogador['nome']} jogou? '))
for contador in range(0, total):
  partidas.append(int(input(f"quantos gols na partida {contador + 1}:")))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print(jogador)
print('-='*30)
for campo, valor in jogador.items():
  print(f"O campo {campo} tem o valor {valor}")
print('-='*30)
print(f"O {jogador['nome']} jogou {len(jogador['gols'])} partidas.")
for partida, valor in enumerate(jogador['gols']):
  print(f'=> Na partida {partida}, fez {valor} gols.')
print(f"Foi um total de {jogador['total']} gols.")