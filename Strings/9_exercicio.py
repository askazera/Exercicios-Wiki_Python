"""

Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx e
indique se é um número válido ou inválido através da validação dos dígitos verificadores edos caracteres de formatação.
"""


def validacao(cpf):  # validando um CPF
    if len(cpf) < 13 or cpf[3] != '.' or cpf[7] != '.' or cpf[11] != '-':  # posições fixas de caracteres no CPF
        return True  # fazendo a condição acima ser verdadeira


while True:
    cpf = input('Digite um cpf valido: ')

    if validacao(cpf):  # como a condição dentro da função é verdadeira, o cpf é inválido
        # poderia fazer sem a função, mas podemos reaproveita-la em outro código se necessário
        print('cpf invalido')
    else:
        print('cpf valido')
