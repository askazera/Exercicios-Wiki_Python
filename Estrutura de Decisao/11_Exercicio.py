"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para
desenvolver o programa que calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:

a) salários até R$ 280,00 (incluindo) : aumento de 20%
b) salários entre R$ 281,00 e R$ 700,00 : aumento de 15%
c) salários entre R$ 701,00 e R$ 1500,00 : aumento de 10%
d) salários de R$ 1501,00 em diante : aumento de 5%

Após o aumento ser realizado, informe na tela:

e) salário antes do reajuste;
f) percentual de aumento aplicado;
g) valor do aumento;
h) novo salário, após o aumento.

"""

salary = float(input('salário do colaborador:'))

if salary <= 280:
    print('Salário antes do reajuste:', salary)
    print('Percentual de aumento:', '20%')
    print('Valor do aumento:', (salary*(1+0.2)) - salary)
    print('Novo salário após o aumento:', salary*(1+0.2))

elif 281 <= salary <= 700:
    print('Salário antes do reajuste:', salary)
    print('Percentual de aumento:', '15%')
    print('Valor do aumento:', (salary * (1 + 0.15)) - salary)
    print('Novo salário após o aumento:', salary * (1 + 0.15))

elif 701 <= salary <= 1500:
    print('Salário antes do reajuste:', salary)
    print('Percentual de aumento:', '10%')
    print('Valor do aumento:', round(salary * (1 + 0.1)) - salary)
    print('Novo salário após o aumento:', round(salary * (1 + 0.1)))

else:
    print('Salário antes do reajuste:', salary)
    print('Percentual de aumento:', '5%')
    print('Valor do aumento:', round(salary * (1 + 0.05)) - salary)
    print('Novo salário após o aumento:', round(salary * (1 + 0.05)))
