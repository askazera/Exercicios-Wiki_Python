'''

O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há
limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um
desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo
usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de
pagamento, valor do desconto e valor a pagar.
'''

tipo = int(input('Selecione o tipo da carne:\n1- Filé Duplo\n2- Alcatra\n3- Picanha\n:'))
kg = float(input('kg:'))
pag = str.upper(input('Pagamento com cartão tabajara?'))

p = None

if tipo == 1:
    print('Tipo: Filé Duplo')
    print('Quantidade (Kg):', kg)
    if kg <= 5:
        p = 4.90
        print('Preço Total:', kg * p)
    if kg > 5:
        p = 5.80
        print('Preço Total:', kg * p)
if tipo == 2:
    print('Tipo: Alcatra')
    print('Quantidade (Kg):', kg)
    if kg <= 5:
        p = 5.90
        print('Preço Total:', kg * p)
    if kg > 5:
        p = 6.8
        print('Preço Total:', kg * p)
if tipo == 3:
    print('Tipo: Picanha')
    print('Quantidade (Kg):', kg)
    if kg <= 5:
        p = 6.90
        print('Preço Total:', kg * p)
    if kg > 5:
        p = 7.8
        print('Preço Total:', kg * p)

if pag == 'SIM':
    print('Pagamento com cartão tabajara: SIM')
    print('Desconto:', (kg * p) - (kg * p) * (1 - 0.05))
    print('Valor a pagar:', (kg * p) * (1 - 0.05))
elif pag == 'NAO':
    print('Pagamento com cartão tabajara: NÃO')
