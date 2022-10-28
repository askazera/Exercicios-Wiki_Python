"""

1. Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

"""

lista = []

for _ in range(5):
    numero = int(input('insira o numero: '))
    lista.append(numero)

print(lista)