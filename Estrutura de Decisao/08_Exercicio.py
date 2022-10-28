"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a
decisão é sempre pelo mais barato.

"""

n1 = float(input('preço do produto 1:'))
n2 = float(input('preço do produto 2:'))
n3 = float(input('preço do produto 3:'))

mais_barato = n1

if mais_barato > n2:
    mais_barato = n2
if mais_barato > n3:
    mais_barato = n3

print('O produto mais barato custa:', mais_barato)