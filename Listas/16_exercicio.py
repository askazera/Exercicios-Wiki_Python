'''

Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.

'''

salarios = []

contagem_posicao = [0]*9

count = 0

for _ in range(3):
    count += 1
    venda = int(input(f'Venda bruta semanal. Vendedor {count}:'))
    calculo_salario = int(200+(venda*0.09))
    salarios.append(calculo_salario)
    print(f'Salario da semana: {calculo_salario}')
    print(salarios)

for salario in salarios:
    indice = salario // 100 - 2    # calcula a posição do salario na lista, começando de 0,
    # '-2' pois o salario começa de 200
    indice_maximo = len(contagem_posicao) - 1
    indice = min(indice, indice_maximo)
    contagem_posicao[indice] += 1  # conta quantas vezes o salario aparece na mesma posição (ex: duas pessoas ganham 380)


print('Numero de pessoas em cada intervalo de salario:', contagem_posicao)