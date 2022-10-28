"""

Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de
arredondamento.

"""

numero = float(input('numero:'))

if numero != round(numero):
    print('decimal')

else:
    print('inteiro')