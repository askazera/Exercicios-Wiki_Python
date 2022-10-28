"""
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.


"""

def reverso(n):
    n = str(n)
    return n[::-1]

try:
    n = int(input('Informe um número inteiro: '))
    print(f'Reverso do número: {reverso(n)}')
except ValueError:
    print('Ooops! esse número não é inteiro!')