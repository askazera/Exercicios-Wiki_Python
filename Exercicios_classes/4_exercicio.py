"""

Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a
idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""


class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):  # encapsulamento
        if self.idade < 21:
            self.altura += 0.05
        self.idade += 1  # contar os anos a medida que for envelhecendo


x = Pessoa('aska', 13, 53, 1.60)

for i in range(22):
    x.envelhecer()
    print(f'Nome: {x.nome}, idade:{x.idade} anos, altura:{x.altura:>.2f} cm')
