"""
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada posição e no qual a
soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9:

8  3  4
1  5  9
6  7  2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as características acima. Dica:
produza todas as combinações possíveis e verifique a soma quando completar cada quadrado. Usar um vetor de 1 a 9 parece
ser mais simples que usar uma matriz 3x3.

"""

from itertools import permutations

cubo = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def validacao(cubo):
    if sum(cubo[:3]) == sum(cubo[3:6]) == sum(cubo[6:10]) == sum(cubo[::3]) == sum(cubo[1::3]) == sum(cubo[2::3]) \
            == sum(cubo[::4]) == sum(cubo[2:8:2]):
        print(f'+-----------+\n|{cubo[0]}    {cubo[1]}    {cubo[2]}|\n|{cubo[3]}    {cubo[4]}    {cubo[5]}|\n'
              f'|{cubo[6]}    {cubo[7]}    {cubo[8]}|\n+-----------+')
        return 1
    else:
        return 0


def gerar_cubo_magico(cubo):
    cont = 0
    valido = 0
    for i in permutations(cubo, 9):
        cont += 1
        valido += validacao(i)
    print(f'Foram gerados {cont} cubos. Cubos válidos de somas iguais: {valido}')


gerar_cubo_magico(cubo)
