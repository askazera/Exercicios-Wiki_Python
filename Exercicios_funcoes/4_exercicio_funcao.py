"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’,
se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.


"""

n = float(input('Insira um número: '))

def fun(n):
    if n <= 0:
        print('N. Número negativo!')
    else:
        print('P. Número positivo!')

fun(n)
