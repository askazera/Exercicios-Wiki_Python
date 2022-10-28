"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.


"""

n = int(input('Informe um número: '))


def funcao(n):
    for i in range(n):
        i += 1
        print('  '.join(i * str(i)))


funcao(n)
