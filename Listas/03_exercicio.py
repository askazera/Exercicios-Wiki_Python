"""
3. Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

"""


#coding: utf-8
lista = []

for _ in range(4):
    numero = int(input('Insira a nota: '))
    lista.append(numero)

print(f'Notas: {lista}')

soma = sum(lista)

print(f'Média das notas: {soma/4}')