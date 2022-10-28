"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:

a) salário bruto.
b) quanto pagou ao INSS.
c) quanto pagou ao sindicato.
d) salário líquido.
e) calcule os descontos e o salário líquido, conforme a tabela abaixo:

+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$

Obs.: Salário Bruto - Descontos = Salário Líquido.

"""
ganho_hora = float(input('ganho por hora:'))
horas_trabalhadas = int(input('horas trabalhadas no mês:'))
salario_bruto = ganho_hora*horas_trabalhadas

ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05

print('Salário Bruto:', 'R$', salario_bruto)
print('Valor do desconto do IR (11%):', 'R$', ir)
print('Valor do desconto do INSS (8%):', 'R$', inss)
print('Valor do desconto do Sindicato (5%):', 'R$', sindicato)
print('Salário Líquido:', 'R$', salario_bruto - ir - inss - sindicato)
