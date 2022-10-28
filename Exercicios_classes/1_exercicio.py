"""

Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""


class CirculoBola:
    def __init__(self):  # atributos
        self.cor = 'Roxo'
        self.circunferencia = 14
        self.material = 'plástico'

    def mostra_cor(self):  # primeiro metodo
        return self.cor  # retorna a cor

    def troca_cor(self, cor):  # segundo metodo
        self.cor = cor  # recebe a cor desejada como argumento
        return cor


x = CirculoBola()
print('Cor do círculo:', x.mostra_cor())
print('Nova cor do círculo:', x.troca_cor('Azul'))
