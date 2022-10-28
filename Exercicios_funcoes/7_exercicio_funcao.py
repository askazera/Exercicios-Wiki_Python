"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta.
O programa deverá solicitar ao usuário o valor da prestação e o número de dias em atraso e passar estes valores para a
função valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que a chamou. O programa
deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de
prestação e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa
deverá ser encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de prestações pagas no dia.
O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, cobrar o valor da prestação.
Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.

"""

cont = 0
prestaco =[]
while True:
    cont += 1
    valor_prestacao = float(input('Informe o valor da prestação: ' ))
    if valor_prestacao == 0:
        cont -= 1
        print('##Relatório do dia##')
        print('Quantidade de Prestações pagas:', cont)
        break
    dias_atrasados = int(input('Informa os dias em atraso: '))
    def valor_pagamento(valor_prestacao, dias_atrasados):
        if dias_atrasados == 0:
            return valor_prestacao
        # calculo do valor de juros por dia sobre o valor com multa + valor com multa
        calculo = valor_prestacao * 1.03 + ((valor_prestacao*1.03)*(dias_atrasados*0.001))
        return calculo
    prestaco.append(valor_pagamento(valor_prestacao,dias_atrasados))
    print(f'Valor a ser pago R${valor_pagamento(valor_prestacao,dias_atrasados):.2f} referente à {dias_atrasados}'
          f' dias em atraso')

print('{:.2f}'.format(sum(prestaco)))