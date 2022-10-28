"""

Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter
14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e
uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para
efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o
usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.

"""
while True:

    horas = int(input('Informe a hora: '))
    minutos = input('Informe os minutos em formato digital: ')
    info = input('Informe \'A\' para AM e \'P\' para PM:').upper()

    def conversao(horas):
     return horas - 12

    def saida(horas, minutos, info):
        if horas <= 12:
            if info == 'A':
                print(f'{horas}:{minutos} AM')
            else:
                print(f'{horas}:{minutos} PM')
        if horas > 12:
            if info == 'P':
                print(f'{conversao(horas)}:{minutos} PM')
            else:
                print('Horário inexistente')

    saida(horas,minutos,info)