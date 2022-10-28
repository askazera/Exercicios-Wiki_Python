"""

Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a
quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função
“altera” o valor de custo para incluir o imposto sobre vendas.

"""

taxa_imposto = float(input('Taxa de imposto sobre vendas: '))
custo = float(input('Informe o custo do item: '))


def soma_imposto(taxa_imposto, custo):
    calculo = custo + (custo * taxa_imposto / 100)
    return calculo


print('Valor final do item com imposto: R${:.2f}'.format(soma_imposto(taxa_imposto, custo)))
