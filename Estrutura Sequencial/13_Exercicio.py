"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal.

Utilize as seguintes fórmulas:

a) Para homens: (72.7*h) - 58
b) Para mulheres: (62.1*h) - 44.7

"""

sexo = int(input('1- Homem\n2- Mulher\nEscolha o sexo:'))
h = float(input('altura:'))


if sexo == 1:
    print('O peso ideal é:', (72.7*h) - 58)
else:
    print('O peso ideal é:', (62.1*h) - 44.7)
