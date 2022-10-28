"""

Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e presentar:

a) A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
b) A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
c) A mensagem "Aprovado com Distinção", se a média for igual a 10.

"""
n1 = float(input('nota 1:'))
n2 = float(input('nota 2:'))
n3 = float(input('nota 3:'))
media = (n1+n2+n3) / 3

if 7 <= media < 10:
    print('Aprovado')
elif media == 10:
    print('Aprovado com Distinção')
else:
    print('Reprovado')
