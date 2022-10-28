"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o
preço total.

"""

tamanho_da_area = int(input('Tamanho da área em metros:'))
litros = tamanho_da_area / 3
latas = litros / 18
preco_da_lata = 80

# Uso do round para arredondar a quantidade da lata e nao aparecer numero decimal
# O valor de uma lata é R$80, por isso o "Preço total" está fixado em preco_da_lata
if latas < 1:
    print('Quantidade de latas a serem compradas:', round(latas))
    print('Preço total:', 'R$', preco_da_lata)

# Para arredondar um número para cima com o round, usa-se: round(num+0.5)
# condicional usada para tamanho da area que ultrapasse o total de uma lata (ex: 1.1111). Arredondamos para cima
else:
    if latas > 1:
        print('Quantidade de latas a serem compradas:', round(latas+0.5))
        print('Preço total:', 'R$', round(latas+0.5)*preco_da_lata)

