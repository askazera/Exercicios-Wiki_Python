"""

Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um
relatório dos endereços IP válidos e inválidos. O arquivo de entrada possui o seguinte formato: 200.135.80.9
192.168.1.1 8.35.67.74 257.32.4.5 85.345.1.2 1.2.3.4 9.8.234.5 192.168.0.256 O arquivo de saída possui o seguinte
formato: [Endereços válidos:] 200.135.80.9 192.168.1.1 8.35.67.74 1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256
"""
validos = []
invalidos = []

with open('ip.txt', 'r') as file:
    for i in file:
        ip = (i.split('.'))
        if len(ip) != 4:
            invalidos.append(i)
        for numero in ip:
            if int(numero) >= 255:
                invalidos.append(i)
        if i not in invalidos:
            validos.append(i)
print('Inválidos:', invalidos)
print('Válidos:', validos)

with open('validacao_ip.txt', 'w') as arquivo:
    arquivo.writelines('[Endereços válidos]:\n')
    arquivo.writelines(validos)
    arquivo.writelines('\n[Endereços Inválidos]:\n')
    arquivo.writelines(invalidos)
