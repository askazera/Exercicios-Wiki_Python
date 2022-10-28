"""
Faça um Programa que leia três números e mostre o maior e o menor deles.

"""

n1 = float(input('numero 1:'))
n2 = float(input('numero 2:'))
n3 = float(input('numero 3:'))

maior = n1


if maior < n2:
    maior = n2

if maior < n3:
    maior = n3


menor = n1

if menor > n2:
    menor = n2
if menor > n3:
    menor = n3

print('O maior número é:', maior)
print('O menor número é:', menor)
