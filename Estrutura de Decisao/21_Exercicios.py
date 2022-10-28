"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois
informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O
valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e
uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""
import math

saque = int(input('Valor do saque entre R$10 à R$600:'))

nota_100 = int(math.floor(saque/100))
nota_50 = int(math.floor(saque % 100) / 50)
nota_10 = int(math.floor(saque % 50)/10)
nota_5 = int(math.floor(saque % 10)/5)
nota_1 = int(math.floor(saque % 5)/1)


if saque < 10 or saque > 600:
    print('Saque inválido')
    exit()

else:
    print('Nota de R$100:', nota_100)
    print('Nota de R$50:', nota_50)
    print('Nota de R$10:', nota_10)
    print('Nota de R$5:', nota_5)
    print('Nota de R$1:', nota_1)
