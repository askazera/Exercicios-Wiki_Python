"""

Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:

Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.


        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00


"""

valor_hora = float(input('valor da hora trabalhada:'))
horas_mes = float(input('horas trabalhadas no mês:'))

salario_bruto = valor_hora*horas_mes
INSS = salario_bruto * 0.1
FGTS = salario_bruto * 0.11
Sindicato = salario_bruto * 0.03


if salario_bruto <= 900:

    print('Salário bruto:', salario_bruto)
    print('Desconto do IR:', 'Isento')
    print('Desconto do FGTS:', FGTS)
    print('Desconto do Sindicato:', Sindicato)
    print('Desconto INSS:', INSS)
    print('Total de descontos:', FGTS + Sindicato + INSS)
    print('Salário Líquido:', salario_bruto - FGTS - Sindicato - INSS)

elif 900 < salario_bruto <= 1500:
    Desc_IR = (salario_bruto - salario_bruto * (1-0.05))

    print('Salário bruto:', salario_bruto)
    print('Desconto do IR:', Desc_IR)
    print('Desconto do FGTS:', FGTS)
    print('Desconto do Sindicato:', Sindicato)
    print('Desconto INSS:', INSS)
    print('Total de descontos:', FGTS + Sindicato + INSS)
    print('Salário Líquido:', salario_bruto - FGTS - Sindicato - INSS)

elif 1500 < salario_bruto <= 2500:
    Desc_IR = (salario_bruto - salario_bruto * (1-0.1))

    print('Salário bruto:', salario_bruto)
    print('Desconto do IR:', Desc_IR)
    print('Desconto do FGTS:', FGTS)
    print('Desconto do Sindicato:', Sindicato)
    print('Desconto INSS:', INSS)
    print('Total de descontos:', FGTS + Sindicato + INSS)
    print('Salário Líquido:', salario_bruto - FGTS - Sindicato - INSS)
else:
    Desc_IR = (salario_bruto - salario_bruto * (1 - 0.2))

    print('Salário bruto:', salario_bruto)
    print('Desconto do IR:', Desc_IR)
    print('Desconto do FGTS:', FGTS)
    print('Desconto do Sindicato:', Sindicato)
    print('Desconto INSS:', INSS)
    print('Total de descontos:', FGTS + Sindicato + INSS)
    print('Salário Líquido:', salario_bruto - FGTS - Sindicato - INSS)
