#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da Chapecoense.
tabela = ('Palmeiras', 'Atletico Paranaense','São Paulo', 'Fluminense', 'Flamengo','Bahia','Coritiba','Grêmio','Vasco da Gama','EC Vitória','Corinthians','Internacional','Atletico-MG','Bragantino','Chapecoense','Santos','Botafogo','Mirassol','Remo','Cruzeiro')
print('-='*15)
print(f'Ordem de classificação do Brasileirao serie A: {tabela}')
print('-='*15)
print(f'Os cinco primeiros colocados são: {tabela[0:5]}')
print('-='*15)
print(f'Os times que estão na zona do rebaixamento(quatro ultimos colocados): {tabela[-4:]}')
print('-='*15)
print(f'Times em ordem alfabetica: {sorted(tabela)}')
print('-='*15)
print(f"A chapecoense na {tabela.index('Chapecoense')+1}ª posição")
print('-='*15)