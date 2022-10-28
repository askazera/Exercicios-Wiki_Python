"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre,
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito
for A, B ou C ou “REPROVADO” se o conceito for D ou E.

"""

n1 = float(input('nota 1:'))
n2 = float(input('nota 2:'))

media = (n1+n2)/2

print('Média:', media)

if media >= 9:
    print('Conceito: A')
    print('Aprovado')
elif 7.5 <= media < 9:
    print('Conceito: B')
    print('Aprovado')
elif 6 <= media < 7.5:
    print('Conceito: C')
    print('Aprovado')
elif 4 <= media < 6:
    print('Conceito: D')
    print('Reprovado')
elif 4 > media > 0:
    print('Conceito: E')
    print('Reprovado')
