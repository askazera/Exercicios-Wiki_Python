'''

Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto
de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças
 adquiridas e escreva o valor a ser pago pelo cliente.
'''

morango = float(input('Morango Kg:'))
maca = float(input('Maçã Kg:'))

mo = 2.5
ma = 1.8


if morango + maca > 8 or ((morango*mo) + (maca*ma)) > 25:
    if morango > 5:
        mo = 2.2
    if maca > 5:
        ma = 1.5
    print('Valor total à pagar:', ((morango*mo) + (maca*ma)) * (1-0.1))

else:
    if morango > 5:
        mo = 2.2
    if maca > 5:
        ma = 1.5
    print('Valor total à pagar:', (morango*mo) + (maca*ma))


