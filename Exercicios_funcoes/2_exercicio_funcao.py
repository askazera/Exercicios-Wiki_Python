"""
Faça um programa para imprimir:
    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha

"""

n = int(input('Insita um número: '))

def fun(n):
    for i in range(n):
        i += 1
        for x in range(i):
            x += 1
            print(x, end= ' ')
        print(' ')


fun(n)