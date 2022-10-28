"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.

"""

def digito(n):
    return len(str(n))

try:
    n = int(input('Informe um número: '))
    print(f'Esse número tem {digito(n)} dígitos')
except ValueError:
    print('Número inválido!')
