"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em
Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

"""

tamanho = int(input('tamanho do arquivo em MB:'))
velocidade = float(input('velocidade do link em Mbps:'))

print('Tempo aproximado de download:', round(tamanho/(velocidade/8)/60 + 0.5))
