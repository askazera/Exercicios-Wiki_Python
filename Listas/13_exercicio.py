"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a
média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

temp = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio','Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']


for x in range(12):
    temp.append(int(input(f'temperatura {meses[x]}: ')))

media_anual = sum(temp)/12
print(f'media das temperaturas: {media_anual}')
print('temperaturas acima da media: ')

for a in range(12):
    if temp[a] > media_anual:
        print(f'{a+1} - {meses[a]}: {temp[a]}')















