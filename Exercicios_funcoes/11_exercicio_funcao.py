"""

Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato
D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

"""
import datetime

data = input('Informe uma data (d/mm/yyyy): ')


# strptime:converte a str pra data, strftime: formata

def dado_data(data_n):
    try:
        d = datetime.datetime.strptime(data_n, "%d/%m/%Y").strftime("%d de %B de %Y")
        print(d)
    except ValueError:
        print('NULL')


dado_data(data)
