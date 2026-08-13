#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares
num =(int(input('Digite um numero: ')),
      int(input('Digite outro numero: ')),
      int(input('Digite mais um numero: ')),
      int(input('Digite o ultimo numero: ')))
print(f'Voce digitou os valores {num}')
print(f"O numero 9 apareceu {num.count(9)} vezes")
if 3 in num:
  print(f'O numero 3 apareceu na posição {num.index(3)}')
else:
  print(f"O valor 3 nao foi digitado em nenhuma posição")
print(f'Os numeros pares digitador foram:', end='')
for n in num:
  if n % 2 ==0:
    print(n, end =' ')