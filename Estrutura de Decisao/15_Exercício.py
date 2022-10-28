"""

Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um
triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;


"""

l1 = int(input('lado 1:'))
l2 = int(input('lado 2:'))
l3 = int(input('lado 3:'))


if (l1+l2) > l3 or (l1+l3) > l2 or (l2+l3) > l1:
    print('A figura geométrica é um triângulo')


elif l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
    print('A figura geométrica não é um triângulo')


if l1 == l2 == l3:
    print('>Tipo do triângulo: Triângulo Equilátero')

elif l1 == l2 or l1 == l3 or l2 == l1 or l2 == l3 or l3 == l1 or l3 == l2:
    print('>Tipo do triângulo: Triângulo Isósceles')

else:
    print('>Tipo do triângulo: Triângulo Escaleno')
