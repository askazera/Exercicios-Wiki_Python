"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

a) o produto do dobro do primeiro com metade do segundo.
b) a soma do triplo do primeiro com o terceiro.
c) o terceiro elevado ao cubo.
"""

n1 = int(input('numero:'))
n2 = int(input('numero:'))
n3 = float(input('numero:'))

print('O produto do dobro do primeiro com metade do segundo:', (n1*2)+(n2/2))
print('A soma do triplo do primeiro com o terceiro:', (n1*3)+n3)
print('O terceiro elevado ao cubo:', n3**3)
