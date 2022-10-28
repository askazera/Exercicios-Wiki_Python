"""

Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

tipoCombustivel.
valorLitro
quantidadeCombustivel
Possua no mínimo esses métodos:
abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada
 no veículo
abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo
cliente.
alterarValor( ) – altera o valor do litro do combustível.
alterarCombustivel( ) – altera o tipo do combustível.
alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
"""


class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quant_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quant_combustivel = quant_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        self._informar_abastecimento(litros_abastecidos, valor)

    def abastecer_por_litro(self, litros_abastecidos):
        valor = litros_abastecidos * self.valor_litro
        self._informar_abastecimento(litros_abastecidos, valor)

    # esse é um metodo que começa com _, significa que: somente essa classe pode usa-lo
    def _informar_abastecimento(self, litros_abastecidos, valor):
        if litros_abastecidos > self.quant_combustivel:
            print(f'Não é possivel abastecer, faltam {litros_abastecidos - self.quant_combustivel:.2f} litros na bomba')
        else:
            self.quant_combustivel -= litros_abastecidos
            print(f'Foram abastecidos: {litros_abastecidos:.2f} litros a um valor de R${valor:.2f}')
            print(f'Sobraram na bomba: {self.quant_combustivel:.2f} litros de {self.tipo_combustivel}')

    def adicionar_combustivel_bomba(self, quantidade):
        if quantidade >= 0:
            self.quant_combustivel + quantidade
        else:
            print('Alerta! você está tirando combustivel dessa bomba!')


x = BombaCombustivel('Gasolina', 4.5, 100)
x.abastecer_por_litro(10)
x.abastecer_por_litro(15)
x.abastecer_por_valor(30)
x.abastecer_por_litro(30)
x.abastecer_por_litro(40)
x.adicionar_combustivel_bomba(50)
x.abastecer_por_litro(30)
x.adicionar_combustivel_bomba(-10)
