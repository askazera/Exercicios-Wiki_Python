"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:

a)A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
b)A mensagem "Reprovado", se a média for menor do que sete;
c)A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""
n1 = float(input('nota 1:'))
n2 = float(input('nota 2:'))
media = (n1+n2) / 2

if 7 <= media < 10:
    print('Aprovado')
elif media  == 10:
    print('Aprovado com Distinção')
else:
    print('Reprovado')