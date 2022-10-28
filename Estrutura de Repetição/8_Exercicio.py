# coding: utf-8
'''

Faça um programa que leia 5 números e informe a soma e a média dos números.

'''

soma_de_numeros = sum([int(input('Informe um número:')) for x in range(5)])

lista_numeros = [i for i in range(5)]

print(f'Soma dos números:{soma_de_numeros}')
print(f'Média dos números: {soma_de_numeros / len(lista_numeros)}')

'''

#Outro modo de fazer usando lista
l = []

for i in range(5):
    numero = int(input('Informe um numero:'))
    l.append(numero)
print(f'A soma dos números é: {sum(l)}')
print(f'A média dos números é: {sum(l)/len(l)}')

'''
