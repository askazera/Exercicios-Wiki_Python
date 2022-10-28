"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.

"""

n1 = int(input('Informe um número: '))
n2 = int(input('Informe um número: '))
n3 = int(input('Informe um número: '))

def soma(n1,n2,n3):
    print(f'A soma dos números é: {n1+n2+n3}')

soma(n1,n2,n3)