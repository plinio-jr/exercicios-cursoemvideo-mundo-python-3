#Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogador = dict()
time = list()
partidas = list()
while True:
  jogador['nome'] = str(input('Nome do jogador: '))
  total = int(input(f'quantas partidas {jogador['nome']} jogou? '))
  partidas.clear()
  for contador in range(0, total):
    partidas.append(int(input(f"quantos gols na partida {contador + 1}:")))
  jogador['gols'] = partidas[:]
  jogador['total'] = sum(partidas)
  time.append(jogador.copy())
  while True:
    opcao = str(input("Quer continuar[S/N]? ")).upper()[0]
    if opcao in 'SN':
      break
      print("Digite apenas S ou N")
  if opcao == 'N':
    break
print('-' * 40)
for espaco, valor in enumerate(time):
    print(f"{espaco:>4}", end='')
    for distancia in valor.values():
      print(f'{str(distancia):>15}', end='')
      print()
    print('-'*40)