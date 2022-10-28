#coding: utf-8
'''

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os
valores para cima, isto é, considere latas cheias.
'''
import math

area = int(input('Tamanho da área a ser pintada (m²):'))
area_com_folga = area*1.1

litros_lata = 18
valor_lata = 80
litros_galao = 3.6
valor_galao = 25

quantidade_tinta_necessaria = round(area_com_folga/6)

quant_latas = math.ceil(quantidade_tinta_necessaria/litros_lata)
quant_galoes = math.ceil(quantidade_tinta_necessaria/litros_galao)


print(f'\nTamanho da área a ser pintada: {area}m²')
print(f'Precisará de: {quantidade_tinta_necessaria}L de tinta')
print(f'Serão necessárias: {quant_latas} latas. Valor: R${quant_latas*valor_lata}')
print(f'Seão necessários: {quant_galoes} galões. Valor: R${quant_galoes*valor_galao}')

#otimizando a quantidade necessária de tinta misturando latas e galões

litros_que_faltam = quantidade_tinta_necessaria % litros_lata
latas_necessarias = math.floor(quantidade_tinta_necessaria/litros_lata)
galoes_necessarios = math.ceil(litros_que_faltam/litros_galao)


print('\nCompra de latas e galões:')
print(f'Latas: {latas_necessarias}, Galões: {galoes_necessarios}')
print(f'Valor: {(latas_necessarias*valor_lata)+(galoes_necessarios*valor_galao)}')

