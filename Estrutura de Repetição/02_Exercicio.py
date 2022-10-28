'''

Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
mensagem de erro e voltando a pedir as informações.
'''

nome = input('nome de usuário:')
senha = input('senha:')

while nome == senha:
    print('Erro! senha igual ao nome')
    nome = str(input('nome de usuário:'))
    senha = int(input('senha:'))
else:
    print('Login válido!')