"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.

"""

n1 = float(input('Escreva um número: '))
n2 = float(input('Escreva um número: '))
n3 = float(input('Escreva um número: '))

lista = [n1, n2, n3]
lista2 = sorted(lista, reverse=True)

print('primeiro:', lista2[2])
print('segundo:', lista2[1])
print('terceiro:', lista2[0])




