"""

Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""


class Quadrado:
    def __init__(self, lado=2):
        self.lado = lado

    def calculo_area(self):
        return self.lado ** 2


x = Quadrado(3)  # posso mudar o valor diretamente na classe se desejar, caso nao queria pegar o atributo de __init__

print(x.calculo_area())
