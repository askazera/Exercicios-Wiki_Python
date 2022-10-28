"""

Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os
números IMPARES no vetor impar. Imprima os três vetores.
"""

par = []
impar = []
list = []

for x in range(20):
    try:
     numero = int(input('Insira um número inteiro: '))
     list.append(numero)
     if numero % 2 == 0:
         par.append(numero)
     elif numero % 2 != 0:
         impar.append(numero)
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


print(f'Lista de vetores:{list}')
print(f'Lista de números pares:{par}')
print(f'Lista de números impares: {impar}')

