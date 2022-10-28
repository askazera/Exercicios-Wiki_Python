'''

Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
'''

tipo = str.upper(input('Tipo:\nA- Álcool\nG- Gasolina\n'))
litros = float(input('litros vendidos:'))

gl = 2.5
al = 1.9

if tipo == 'A':
    if litros <= 20:
        print('Preço:', litros*al)
        print('Desconto:', (litros * al) - ((litros * al) * (1-0.03)))
        print('Preço final:', (litros * al) * (1-0.03))
    else:
        print('Preço:', litros * al)
        print('Desconto:', (litros * al) - ((litros * al) * (1 - 0.05)))
        print('Preço final:', (litros * al) * (1 - 0.05))
if tipo == 'G':
    if litros <= 20:
        print('Preço:', litros * al)
        print('Desconto:', (litros * al) - ((litros * al) * (1 - 0.04)))
        print('Preço final:', (litros * al) * (1 - 0.04))
    else:
        print('Preço:', litros * al)
        print('Desconto:', (litros * al) - ((litros * al) * (1 - 0.06)))
        print('Preço final:', (litros * al) * (1 - 0.06))